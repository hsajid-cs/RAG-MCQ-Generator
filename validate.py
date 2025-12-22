"""MCQ Validation Script with Gemini-Powered Detailed Reporting.

This script validates MCQ files for:
1. Uniqueness (duplicate questions)
2. Distractor quality (ensuring wrong answers are plausible)
3. Math verification (for mathematics/physics questions)
4. Citation checker (verifying file references exist)

Generates a comprehensive validation report using Gemini API.
"""

import json
import os
import re
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import difflib

# replace direct import with guarded import
try:
    import google.generativeai as genai
except Exception:
    genai = None

# Configuration
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash-lite"
MCQ_FOLDER = "mcqs"
CORPUS_FOLDER = "corpus"
VALIDATION_FOLDER = "validation"

# Batch processing configuration
BATCH_SIZE = 10  # Process MCQs in batches to avoid overwhelming the model
MAX_DUPLICATES_IN_REPORT = 5  # Limit duplicates shown in full report
MAX_ISSUES_PER_CATEGORY = 5  # Limit issues shown per validation category
API_RATE_LIMIT_DELAY = 1.0  # Seconds to wait between API calls

# Configure Gemini if available and key provided; keep import safe for environments without Gemini
if genai is not None and GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception:
        # Leave genai usable downstream; actual calls will raise with clearer message
        pass


def load_mcq_file(filepath: str) -> List[Dict[str, Any]]:
    """Load MCQ JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_uniqueness(mcqs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Check for duplicate questions across all MCQs (including passage for SAT)."""
    seen_questions = {}
    duplicates = []
    
    for idx, mcq in enumerate(mcqs):
        # For SAT questions, include passage in uniqueness check
        question = mcq.get('question', '').strip().lower()
        passage = mcq.get('passage', '').strip().lower()
        
        # Create composite key for SAT questions that have passages
        if passage:
            composite_key = f"{passage[:200]}|||{question}"  # Use first 200 chars of passage
        else:
            composite_key = question
        
        if composite_key in seen_questions:
            duplicates.append({
                'question': mcq.get('question', ''),
                'passage_preview': passage[:100] if passage else 'N/A',
                'first_occurrence': seen_questions[composite_key],
                'duplicate_at': idx,
                'subject': mcq.get('subject', mcq.get('chapter', 'N/A')),
                'topic': mcq.get('topic', 'N/A')
            })
        else:
            seen_questions[composite_key] = idx
    
    return {
        'total_questions': len(mcqs),
        'unique_questions': len(seen_questions),
        'duplicate_count': len(duplicates),
        'duplicates': duplicates
    }


def check_distractors(mcqs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze distractor quality."""
    issues = []
    
    for idx, mcq in enumerate(mcqs):
        choices = mcq.get('choices', [])
        answer = mcq.get('answer', '')
        question = mcq.get('question', '')
        
        # Check if there are enough choices
        if len(choices) < 4:
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Insufficient choices',
                'details': f'Only {len(choices)} choices provided'
            })
            continue  # subsequent checks assume 4 choices
        
        # Normalize choice text
        norm_simple = [c.strip() for c in choices]
        norm_cmp = [re.sub(r'[\W_]+', ' ', c).strip().lower() for c in choices]
        
        # Check for exact duplicates
        unique_choices = set([c.strip().lower() for c in choices])
        if len(unique_choices) < len(choices):
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Duplicate choices',
                'details': 'Some answer choices are identical'
            })
        
        # Check for near duplicates (punctuation/whitespace-insensitive)
        if len(set(norm_cmp)) < len(norm_cmp):
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Near-duplicate choices',
                'details': 'Some choices differ only by case/punctuation'
            })
        
        # Highly similar choices (SequenceMatcher)
        sim_pairs = []
        for i in range(len(norm_cmp)):
            for j in range(i + 1, len(norm_cmp)):
                sim = difflib.SequenceMatcher(None, norm_cmp[i], norm_cmp[j]).ratio()
                if sim > 0.9:
                    sim_pairs.append((i, j, round(sim, 2)))
        if sim_pairs:
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Highly similar distractors',
                'details': f'Choice pairs too similar: {sim_pairs}'
            })
        
        # Banned forms
        banned = {'none of the above', 'all of the above', 'none of these', 'all of these'}
        if any(any(b in c.lower() for b in banned) for c in choices):
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Banned choices detected',
                'details': 'Contains "None/All of the above/these"'
            })
        
        # Length imbalance
        lens = [len(c) for c in norm_simple]
        if min(lens) > 0 and (max(lens) / max(1, min(lens)) > 3):
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Length imbalance',
                'details': f'Choice length ratio too high: max={max(lens)}, min={min(lens)}'
            })
        
        # Check if answer is valid
        valid_answers = ['A', 'B', 'C', 'D']
        if answer not in valid_answers:
            issues.append({
                'index': idx,
                'question': question,
                'issue': 'Invalid answer label',
                'details': f'Answer "{answer}" not in {valid_answers}'
            })
        else:
            ans_idx = ord(answer) - 65
            if not (0 <= ans_idx < len(choices)):
                issues.append({
                    'index': idx,
                    'question': question,
                    'issue': 'Answer index out of range',
                    'details': f'Answer "{answer}" does not map into provided choices'
                })
        
        # Numeric plausibility checks (all numeric choices)
        is_numeric = all(re.fullmatch(r'\s*[-+]?\d+(\.\d+)?\s*', c or '') for c in choices if isinstance(c, str))
        if is_numeric and answer in valid_answers:
            try:
                ans_idx = ord(answer) - 65
                correct_val = float(choices[ans_idx])
                distractor_vals = []
                for i, c in enumerate(choices):
                    if i == ans_idx:
                        continue
                    distractor_vals.append(float(c))
                deltas = [abs(v - correct_val) for v in distractor_vals]
                
                # Distinctness of distractors
                if len(set(round(d, 6) for d in deltas)) < len(deltas):
                    issues.append({
                        'index': idx,
                        'question': question,
                        'issue': 'Numeric distractors too similar',
                        'details': f'Deltas to correct answer not sufficiently distinct: {deltas}'
                    })
                
                # Avoid trivial or zero deltas
                if any(d == 0 for d in deltas):
                    issues.append({
                        'index': idx,
                        'question': question,
                        'issue': 'Duplicate numeric value',
                        'details': 'A distractor equals the correct numeric answer'
                    })
            except Exception:
                # Ignore parse errors silently for numeric-only check
                pass
    
    return {
        'total_checked': len(mcqs),
        'issues_found': len(issues),
        'issues': issues
    }


def check_math_validity(mcqs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Check mathematical expressions for validity."""
    math_issues = []
    
    # Patterns that might indicate math content
    math_patterns = [
        r'\d+\s*[\+\-\*\/\^]\s*\d+',  # Basic arithmetic
        r'[a-z]\^?\d',  # Variables with exponents
        r'\\[a-zA-Z]+',  # LaTeX commands
        r'\$.*?\$',  # Inline math
        r'\d+\s*[=<>]\s*\d+',  # Equations/inequalities
    ]
    
    for idx, mcq in enumerate(mcqs):
        subject = mcq.get('subject', mcq.get('chapter', ''))
        
        # Only check math/physics questions
        if 'math' not in str(subject).lower() and 'physics' not in str(subject).lower():
            continue
        
        question = mcq.get('question', '')
        choices = mcq.get('choices', [])
        rationale = mcq.get('rationale', '')
        
        # Check for unbalanced parentheses
        for text_field, field_name in [(question, 'question'), (rationale, 'rationale')]:
            if text_field.count('(') != text_field.count(')'):
                math_issues.append({
                    'index': idx,
                    'question': question[:100],
                    'issue': 'Unbalanced parentheses',
                    'field': field_name
                })
            
            if text_field.count('[') != text_field.count(']'):
                math_issues.append({
                    'index': idx,
                    'question': question[:100],
                    'issue': 'Unbalanced brackets',
                    'field': field_name
                })
        
        # Check for broken math notation
        if '\\' in question or '\\' in rationale:
            # Might be LaTeX - check for common errors
            for text_field, field_name in [(question, 'question'), (rationale, 'rationale')]:
                if '\\frac{' in text_field:
                    # Check if frac is complete
                    frac_count = text_field.count('\\frac{')
                    brace_after_frac = len(re.findall(r'\\frac\{[^}]*\}\{[^}]*\}', text_field))
                    if frac_count != brace_after_frac:
                        math_issues.append({
                            'index': idx,
                            'question': question[:100],
                            'issue': 'Incomplete LaTeX \\frac command',
                            'field': field_name
                        })
    
    return {
        'math_questions_checked': sum(1 for mcq in mcqs if 'math' in str(mcq.get('subject', mcq.get('chapter', ''))).lower() or 'physics' in str(mcq.get('subject', mcq.get('chapter', ''))).lower()),
        'issues_found': len(math_issues),
        'issues': math_issues
    }


def check_citations(mcqs: List[Dict[str, Any]], corpus_root: str = CORPUS_FOLDER) -> Dict[str, Any]:
    """Verify that cited files actually exist."""
    citation_issues = []
    
    for idx, mcq in enumerate(mcqs):
        # Handle both single citation and citations list
        citations = []
        if 'citation' in mcq:
            citations = [mcq['citation']]
        elif 'citations' in mcq:
            citations = mcq['citations']
        
        question = mcq.get('question', '')
        
        for citation in citations:
            # Normalize path separators - convert forward slashes to OS-specific separators
            # This handles citations stored with forward slashes on Windows
            normalized_citation = citation.replace('/', os.sep).replace('\\', os.sep)
            
            # Build full path
            citation_path = Path(corpus_root) / normalized_citation
            
            if not citation_path.exists():
                citation_issues.append({
                    'index': idx,
                    'question': question[:100],
                    'citation': citation,
                    'expected_path': str(citation_path),
                    'issue': 'File not found'
                })
    
    return {
        'total_citations_checked': sum(len(mcq.get('citations', [])) + (1 if 'citation' in mcq else 0) for mcq in mcqs),
        'issues_found': len(citation_issues),
        'issues': citation_issues
    }


def call_gemini(prompt: str, temperature: float = 0.3, retry_count: int = 3) -> str:
    """Call Gemini API to generate detailed report with retry logic and rate limiting."""
    
    for attempt in range(retry_count):
        try:
            # Rate limiting - wait before making API call
            if attempt > 0:
                wait_time = API_RATE_LIMIT_DELAY * (2 ** attempt)  # Exponential backoff
                print(f"  Retrying in {wait_time:.1f} seconds...")
                time.sleep(wait_time)
            
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=8192,
                )
            )
            
            # Rate limiting - wait after successful call
            time.sleep(API_RATE_LIMIT_DELAY)
            
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            
            if "429" in error_msg or "quota" in error_msg.lower() or "rate" in error_msg.lower():
                print(f"  Rate limit hit (attempt {attempt + 1}/{retry_count})")
                if attempt < retry_count - 1:
                    continue
            elif "500" in error_msg or "503" in error_msg:
                print(f"  Server error (attempt {attempt + 1}/{retry_count})")
                if attempt < retry_count - 1:
                    continue
            
            if attempt == retry_count - 1:
                return f"Error calling Gemini API after {retry_count} attempts: {error_msg}"
    
    return "Error: Failed to get response from Gemini API"


def generate_gemini_report(validation_results: Dict[str, Any]) -> str:
    """Generate a detailed validation report using Gemini with optimized payload."""
    
    # Prepare summarized data to avoid overwhelming the model
    summary_data = {
        'total_mcqs': validation_results['total_mcqs'],
        'files': validation_results['files_analyzed'],
        'uniqueness': {
            'total': validation_results['uniqueness']['total_questions'],
            'unique': validation_results['uniqueness']['unique_questions'],
            'duplicates': validation_results['uniqueness']['duplicate_count'],
            'sample_duplicates': validation_results['uniqueness']['duplicates'][:5]  # Limit to 5 samples
        },
        'distractors': {
            'checked': validation_results['distractors']['total_checked'],
            'issues': validation_results['distractors']['issues_found'],
            'sample_issues': validation_results['distractors']['issues'][:5]  # Limit to 5 samples
        },
        'math': {
            'checked': validation_results['math_validity']['math_questions_checked'],
            'issues': validation_results['math_validity']['issues_found'],
            'sample_issues': validation_results['math_validity']['issues'][:5]  # Limit to 5 samples
        },
        'citations': {
            'checked': validation_results['citations']['total_citations_checked'],
            'issues': validation_results['citations']['issues_found'],
            'sample_issues': validation_results['citations']['issues'][:5]  # Limit to 5 samples
        }
    }
    
    prompt = f"""You are an expert educational content quality analyst. Generate a comprehensive, professional validation report for MCQ (Multiple Choice Question) datasets.

Here is a summary of validation results from automated checks:

{json.dumps(summary_data, indent=2)}

Generate a detailed report with the following sections:

1. **EXECUTIVE SUMMARY**: Brief overview of overall quality and key findings

2. **UNIQUENESS ANALYSIS**: 
   - Assess the duplicate rate
   - Highlight any patterns in duplicates
   - Provide recommendations

3. **DISTRACTOR QUALITY ASSESSMENT**:
   - Evaluate the quality and diversity of wrong answer choices
   - Identify common issues
   - Suggest improvements

4. **MATHEMATICAL VALIDITY**:
   - Comment on mathematical notation and correctness
   - Highlight any critical errors
   - Recommend fixes

5. **CITATION INTEGRITY**:
   - Assess the citation coverage and accuracy
   - List missing files that need attention
   - Recommendations for fixing broken citations

6. **OVERALL QUALITY SCORE**: Rate the MCQ dataset quality from 0-100 with justification

7. **ACTION ITEMS**: Prioritized list of fixes needed

8. **RECOMMENDATIONS**: Strategic suggestions for improving MCQ quality going forward

Make the report professional, actionable, and easy to understand. Use markdown formatting.
"""
    
    return call_gemini(prompt)


def validate_mcq_folder(folder_path: str = MCQ_FOLDER) -> Dict[str, Any]:
    """Validate all MCQ files in the folder with batch processing."""
    
    mcq_files = list(Path(folder_path).glob("*.json"))
    
    if not mcq_files:
        print(f"No JSON files found in {folder_path}")
        return {}
    
    all_mcqs = []
    files_analyzed = []
    
    print(f"Found {len(mcq_files)} MCQ file(s) to validate...")
    
    for mcq_file in mcq_files:
        print(f"Loading {mcq_file.name}...")
        mcqs = load_mcq_file(str(mcq_file))
        all_mcqs.extend(mcqs)
        files_analyzed.append({
            'filename': mcq_file.name,
            'question_count': len(mcqs)
        })
    
    total_mcqs = len(all_mcqs)
    print(f"\nTotal MCQs loaded: {total_mcqs}")
    
    # Process in batches to avoid overwhelming memory/processing
    num_batches = (total_mcqs + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"Processing in {num_batches} batch(es) of up to {BATCH_SIZE} questions each...\n")
    
    # Initialize combined results
    all_uniqueness_duplicates = []
    all_distractor_issues = []
    all_math_issues = []
    all_citation_issues = []
    seen_questions = {}
    total_citations = 0
    math_questions_count = 0
    
    for batch_idx in range(num_batches):
        start_idx = batch_idx * BATCH_SIZE
        end_idx = min((batch_idx + 1) * BATCH_SIZE, total_mcqs)
        batch = all_mcqs[start_idx:end_idx]
        
        print(f"Processing batch {batch_idx + 1}/{num_batches} (questions {start_idx + 1}-{end_idx})...")
        
        # Uniqueness check for this batch
        for idx, mcq in enumerate(batch):
            global_idx = start_idx + idx
            question = mcq.get('question', '').strip().lower()
            
            if question in seen_questions:
                all_uniqueness_duplicates.append({
                    'question': mcq.get('question', ''),
                    'first_occurrence': seen_questions[question],
                    'duplicate_at': global_idx,
                    'subject': mcq.get('subject', mcq.get('chapter', 'N/A')),
                    'topic': mcq.get('topic', 'N/A')
                })
            else:
                seen_questions[question] = global_idx
        
        # Distractor check for this batch
        distractor_batch_result = check_distractors(batch)
        for issue in distractor_batch_result['issues']:
            issue['index'] = start_idx + issue['index']  # Adjust to global index
            all_distractor_issues.append(issue)
        
        # Math check for this batch
        math_batch_result = check_math_validity(batch)
        math_questions_count += math_batch_result['math_questions_checked']
        for issue in math_batch_result['issues']:
            issue['index'] = start_idx + issue['index']  # Adjust to global index
            all_math_issues.append(issue)
        
        # Citation check for this batch
        citation_batch_result = check_citations(batch)
        total_citations += citation_batch_result['total_citations_checked']
        for issue in citation_batch_result['issues']:
            issue['index'] = start_idx + issue['index']  # Adjust to global index
            all_citation_issues.append(issue)
    
    # Compile final results
    uniqueness_results = {
        'total_questions': total_mcqs,
        'unique_questions': len(seen_questions),
        'duplicate_count': len(all_uniqueness_duplicates),
        'duplicates': all_uniqueness_duplicates
    }
    
    distractor_results = {
        'total_checked': total_mcqs,
        'issues_found': len(all_distractor_issues),
        'issues': all_distractor_issues
    }
    
    math_results = {
        'math_questions_checked': math_questions_count,
        'issues_found': len(all_math_issues),
        'issues': all_math_issues
    }
    
    citation_results = {
        'total_citations_checked': total_citations,
        'issues_found': len(all_citation_issues),
        'issues': all_citation_issues
    }
    
    validation_results = {
        'files_analyzed': files_analyzed,
        'total_mcqs': total_mcqs,
        'uniqueness': uniqueness_results,
        'distractors': distractor_results,
        'math_validity': math_results,
        'citations': citation_results
    }
    
    print("✓ Batch processing complete!\n")
    
    return validation_results


def save_report(report: str, filename: str = "validation_report.md"):
    """Save the validation report to a file."""
    # Ensure validation folder exists
    os.makedirs(VALIDATION_FOLDER, exist_ok=True)
    
    # Save to validation folder
    filepath = os.path.join(VALIDATION_FOLDER, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\nReport saved to {filepath}")


def validate_single_file(mcq_file: Path) -> Dict[str, Any]:
    """Validate a single MCQ file and generate report."""
    print(f"\n{'='*70}")
    print(f"Validating: {mcq_file.name}")
    print("="*70)
    
    # Load MCQs
    mcqs = load_mcq_file(str(mcq_file))
    total_mcqs = len(mcqs)
    print(f"Loaded {total_mcqs} questions from {mcq_file.name}")
    
    # Determine subject from filename
    subject = mcq_file.stem.replace('_mcqs', '').replace('_', ' ').title()
    
    # Process in batches
    num_batches = (total_mcqs + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"Processing in {num_batches} batch(es)...\n")
    
    # Initialize combined results
    all_uniqueness_duplicates = []
    all_distractor_issues = []
    all_math_issues = []
    all_citation_issues = []
    seen_questions = {}
    total_citations = 0
    math_questions_count = 0
    
    for batch_idx in range(num_batches):
        start_idx = batch_idx * BATCH_SIZE
        end_idx = min((batch_idx + 1) * BATCH_SIZE, total_mcqs)
        batch = mcqs[start_idx:end_idx]
        
        print(f"  Batch {batch_idx + 1}/{num_batches} (Q{start_idx + 1}-{end_idx})...")
        
        # Uniqueness check for this batch
        for idx, mcq in enumerate(batch):
            global_idx = start_idx + idx
            question = mcq.get('question', '').strip().lower()
            passage = mcq.get('passage', '').strip().lower()
            
            # Create composite key for SAT questions
            if passage:
                composite_key = f"{passage[:200]}|||{question}"
            else:
                composite_key = question
            
            if composite_key in seen_questions:
                all_uniqueness_duplicates.append({
                    'question': mcq.get('question', ''),
                    'passage_preview': passage[:100] if passage else 'N/A',
                    'first_occurrence': seen_questions[composite_key],
                    'duplicate_at': global_idx,
                    'subject': mcq.get('subject', mcq.get('chapter', 'N/A')),
                    'topic': mcq.get('topic', 'N/A')
                })
            else:
                seen_questions[composite_key] = global_idx
        
        # Distractor check
        distractor_batch_result = check_distractors(batch)
        for issue in distractor_batch_result['issues']:
            issue['index'] = start_idx + issue['index']
            all_distractor_issues.append(issue)
        
        # Math check
        math_batch_result = check_math_validity(batch)
        math_questions_count += math_batch_result['math_questions_checked']
        for issue in math_batch_result['issues']:
            issue['index'] = start_idx + issue['index']
            all_math_issues.append(issue)
        
        # Citation check
        citation_batch_result = check_citations(batch)
        total_citations += citation_batch_result['total_citations_checked']
        for issue in citation_batch_result['issues']:
            issue['index'] = start_idx + issue['index']
            all_citation_issues.append(issue)
    
    print("  ✓ Complete!")
    
    # Compile results
    validation_results = {
        'file': mcq_file.name,
        'subject': subject,
        'total_mcqs': total_mcqs,
        'uniqueness': {
            'total_questions': total_mcqs,
            'unique_questions': len(seen_questions),
            'duplicate_count': len(all_uniqueness_duplicates),
            'duplicates': all_uniqueness_duplicates
        },
        'distractors': {
            'total_checked': total_mcqs,
            'issues_found': len(all_distractor_issues),
            'issues': all_distractor_issues
        },
        'math_validity': {
            'math_questions_checked': math_questions_count,
            'issues_found': len(all_math_issues),
            'issues': all_math_issues
        },
        'citations': {
            'total_citations_checked': total_citations,
            'issues_found': len(all_citation_issues),
            'issues': all_citation_issues
        }
    }
    
    return validation_results


def generate_subject_report(validation_results: Dict[str, Any]) -> str:
    """Generate report for a single subject file."""
    subject = validation_results['subject']
    
    # Prepare summarized data
    summary_data = {
        'subject': subject,
        'file': validation_results['file'],
        'total_mcqs': validation_results['total_mcqs'],
        'uniqueness': {
            'total': validation_results['uniqueness']['total_questions'],
            'unique': validation_results['uniqueness']['unique_questions'],
            'duplicates': validation_results['uniqueness']['duplicate_count'],
            'sample_duplicates': validation_results['uniqueness']['duplicates'][:5]
        },
        'distractors': {
            'checked': validation_results['distractors']['total_checked'],
            'issues': validation_results['distractors']['issues_found'],
            'sample_issues': validation_results['distractors']['issues'][:5]
        },
        'math': {
            'checked': validation_results['math_validity']['math_questions_checked'],
            'issues': validation_results['math_validity']['issues_found'],
            'sample_issues': validation_results['math_validity']['issues'][:5]
        },
        'citations': {
            'checked': validation_results['citations']['total_citations_checked'],
            'issues': validation_results['citations']['issues_found'],
            'sample_issues': validation_results['citations']['issues'][:5]
        }
    }
    
    prompt = f"""You are an expert educational content quality analyst. Generate a comprehensive validation report for {subject} MCQ dataset.

Validation Summary:
{json.dumps(summary_data, indent=2)}

Generate a detailed report with:

1. **EXECUTIVE SUMMARY**: Brief overview of {subject} MCQ quality

2. **UNIQUENESS ANALYSIS**: 
   - Duplicate rate and patterns
   - Recommendations for {subject}

3. **DISTRACTOR QUALITY**: 
   - Quality of wrong answer choices
   - Subject-specific insights
   - Improvements needed

4. **MATHEMATICAL VALIDITY** (if applicable):
   - Math notation correctness
   - Critical errors

5. **CITATION INTEGRITY**:
   - Citation coverage
   - Missing source files

6. **QUALITY SCORE**: Rate 0-100 with justification

7. **ACTION ITEMS**: Prioritized fixes for {subject}

8. **RECOMMENDATIONS**: Strategic improvements

Use markdown formatting. Be specific to {subject} content."""
    
    return call_gemini(prompt)


def cite_check(mcq: Dict[str, Any], contexts: Optional[List[Dict[str, Any]]] = None) -> bool:
    """
    Strict citation gate.

    Returns True only if:
    - mcq has non-empty 'citations' OR
    - at least one retrieved context shares a meaningful substring/keywords with the MCQ
      (heuristic match between context text and question/rationale/solution).

    This function is intentionally conservative: generator should retry/regenerate items
    that fail this gate.
    """
    if not isinstance(mcq, dict):
        return False

    # build mcq content to search against
    parts = []
    for k in ("question", "question_text", "rationale", "solution_latex", "solution"):
        v = mcq.get(k)
        if v:
            parts.append(str(v))
    content = " ".join(parts).lower().strip()
    if not content:
        return False

    # 1) explicit citations -> accept
    cit = mcq.get("citations") or mcq.get("citation") or []
    if isinstance(cit, str) and cit.strip():
        return True
    if isinstance(cit, (list, tuple)) and len([c for c in cit if c]) > 0:
        return True

    # 2) check contexts (heuristic)
    if contexts:
        # prepare keyword set from content (long words)
        content_words = set(w for w in re.split(r"\W+", content) if len(w) > 4)
        for ctx in contexts:
            text = (ctx.get("text") or ctx.get("content") or ctx.get("snippet") or "").lower()
            if not text:
                continue
            # direct substring match of a meaningful prefix
            snippet = text.strip()[:120]
            if snippet and snippet in content:
                return True
            # keyword overlap: require at least 2 long-word overlaps
            ctx_words = set(w for w in re.split(r"\W+", text) if len(w) > 4)
            if len(content_words.intersection(ctx_words)) >= 2:
                return True

    # otherwise fail strict gate
    return False

def main():
    """Main validation workflow."""
    print("="*70)
    print("MCQ VALIDATION SYSTEM")
    print("="*70)
    print()
    
    # Ensure validation folder exists
    os.makedirs(VALIDATION_FOLDER, exist_ok=True)
    
    # Get all MCQ files
    mcq_files = list(Path(MCQ_FOLDER).glob("*.json"))
    
    if not mcq_files:
        print(f"No JSON files found in {MCQ_FOLDER}")
        return
    
    print(f"Found {len(mcq_files)} MCQ file(s) to validate\n")
    
    all_results = []
    
    # Validate each file separately
    for mcq_file in mcq_files:
        validation_results = validate_single_file(mcq_file)
        all_results.append(validation_results)
        
        # Generate summary for this subject
        print(f"\n  Summary for {validation_results['subject']}:")
        print(f"    Total MCQs: {validation_results['total_mcqs']}")
        print(f"    Unique: {validation_results['uniqueness']['unique_questions']}/{validation_results['uniqueness']['total_questions']}")
        print(f"    Duplicates: {validation_results['uniqueness']['duplicate_count']}")
        print(f"    Distractor Issues: {validation_results['distractors']['issues_found']}")
        print(f"    Math Issues: {validation_results['math_validity']['issues_found']}")
        print(f"    Citation Issues: {validation_results['citations']['issues_found']}")
        
        # Generate detailed report with Gemini for this subject
        print(f"\n  Generating AI report for {validation_results['subject']}...")
        gemini_report = generate_subject_report(validation_results)
        
        # Create full report for this subject
        subject_name = mcq_file.stem
        full_report = f"""# {validation_results['subject']} MCQ VALIDATION REPORT
File: {validation_results['file']}
Generated: {os.popen('echo %date% %time%').read().strip()}

---

{gemini_report}

---

## DETAILED VALIDATION DATA

### File Information
- Filename: {validation_results['file']}
- Total Questions: {validation_results['total_mcqs']}

### Uniqueness Results
- Total Questions: {validation_results['uniqueness']['total_questions']}
- Unique Questions: {validation_results['uniqueness']['unique_questions']}
- Duplicates: {validation_results['uniqueness']['duplicate_count']}

"""
        
        # Add duplicate details if any
        if validation_results['uniqueness']['duplicates']:
            full_report += "#### Duplicate Questions:\n"
            duplicates_to_show = min(MAX_DUPLICATES_IN_REPORT, len(validation_results['uniqueness']['duplicates']))
            for dup in validation_results['uniqueness']['duplicates'][:duplicates_to_show]:
                full_report += f"- **Q{dup['duplicate_at']}**: {dup['question'][:80]}...\n"
                full_report += f"  (First seen at index {dup['first_occurrence']})\n\n"
            
            if len(validation_results['uniqueness']['duplicates']) > MAX_DUPLICATES_IN_REPORT:
                remaining = len(validation_results['uniqueness']['duplicates']) - MAX_DUPLICATES_IN_REPORT
                full_report += f"*...and {remaining} more duplicates*\n\n"
        
        full_report += f"""
### Distractor Quality Results
- Total Checked: {validation_results['distractors']['total_checked']}
- Issues Found: {validation_results['distractors']['issues_found']}

"""
        
        # Add distractor issues if any
        if validation_results['distractors']['issues']:
            full_report += "#### Sample Issues:\n"
            issues_to_show = min(MAX_ISSUES_PER_CATEGORY, len(validation_results['distractors']['issues']))
            for issue in validation_results['distractors']['issues'][:issues_to_show]:
                full_report += f"- **Q{issue['index']}**: {issue['issue']} - {issue['details']}\n"
            
            if len(validation_results['distractors']['issues']) > MAX_ISSUES_PER_CATEGORY:
                remaining = len(validation_results['distractors']['issues']) - MAX_ISSUES_PER_CATEGORY
                full_report += f"\n*...and {remaining} more issues*\n"
        
        full_report += f"""
### Math Validity Results
- Math/Physics Questions Checked: {validation_results['math_validity']['math_questions_checked']}
- Issues Found: {validation_results['math_validity']['issues_found']}

"""
        
        # Add math issues if any
        if validation_results['math_validity']['issues']:
            full_report += "#### Math Issues:\n"
            issues_to_show = min(MAX_ISSUES_PER_CATEGORY, len(validation_results['math_validity']['issues']))
            for issue in validation_results['math_validity']['issues'][:issues_to_show]:
                full_report += f"- **Q{issue['index']}**: {issue['issue']} in {issue['field']}\n"
            
            if len(validation_results['math_validity']['issues']) > MAX_ISSUES_PER_CATEGORY:
                remaining = len(validation_results['math_validity']['issues']) - MAX_ISSUES_PER_CATEGORY
                full_report += f"\n*...and {remaining} more issues*\n"
        
        full_report += f"""
### Citation Verification Results
- Total Citations Checked: {validation_results['citations']['total_citations_checked']}
- Broken Citations: {validation_results['citations']['issues_found']}

"""
        
        # Add citation issues if any
        if validation_results['citations']['issues']:
            full_report += "#### Missing Citation Files:\n"
            issues_to_show = min(MAX_ISSUES_PER_CATEGORY, len(validation_results['citations']['issues']))
            for issue in validation_results['citations']['issues'][:issues_to_show]:
                full_report += f"- `{issue['citation']}` (Q{issue['index']})\n"
            
            if len(validation_results['citations']['issues']) > MAX_ISSUES_PER_CATEGORY:
                remaining = len(validation_results['citations']['issues']) - MAX_ISSUES_PER_CATEGORY
                full_report += f"\n*...and {remaining} more missing files*\n"
        
        # Save report for this subject
        report_filename = f"{subject_name}_report.md"
        save_report(full_report, report_filename)
    
    # Generate combined summary report
    print("\n" + "="*70)
    print("Generating Combined Summary Report...")
    print("="*70)
    
    total_mcqs = sum(r['total_mcqs'] for r in all_results)
    total_duplicates = sum(r['uniqueness']['duplicate_count'] for r in all_results)
    total_distractor_issues = sum(r['distractors']['issues_found'] for r in all_results)
    total_math_issues = sum(r['math_validity']['issues_found'] for r in all_results)
    total_citation_issues = sum(r['citations']['issues_found'] for r in all_results)
    
    summary_report = f"""# MCQ VALIDATION SUMMARY - ALL SUBJECTS
Generated: {os.popen('echo %date% %time%').read().strip()}

## Overview

Total MCQ Files Analyzed: {len(all_results)}
Total Questions: {total_mcqs}

## Summary by Subject

"""
    
    for result in all_results:
        summary_report += f"""### {result['subject']}
- File: `{result['file']}`
- Questions: {result['total_mcqs']}
- Duplicates: {result['uniqueness']['duplicate_count']}
- Distractor Issues: {result['distractors']['issues_found']}
- Math Issues: {result['math_validity']['issues_found']}
- Citation Issues: {result['citations']['issues_found']}
- Quality Score: See individual report

"""
    
    summary_report += f"""## Overall Statistics

- Total Duplicates Across All Files: {total_duplicates}
- Total Distractor Issues: {total_distractor_issues}
- Total Math Issues: {total_math_issues}
- Total Citation Issues: {total_citation_issues}

## Individual Reports

"""
    
    for result in all_results:
        subject_name = Path(result['file']).stem
        summary_report += f"- [{result['subject']}]({subject_name}_report.md)\n"
    
    summary_report += "\n---\n\n*Detailed individual reports available in the validation folder.*\n"
    
    save_report(summary_report, "00_summary_report.md")
    
    print("\n" + "="*70)
    print("VALIDATION COMPLETE!")
    print("="*70)
    print(f"\n📂 All reports saved to '{VALIDATION_FOLDER}/' folder:")
    print(f"   - 00_summary_report.md (combined summary)")
    for result in all_results:
        subject_name = Path(result['file']).stem
        print(f"   - {subject_name}_report.md")
    print()


if __name__ == "__main__":
    main()
