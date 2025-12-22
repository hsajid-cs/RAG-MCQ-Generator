"""Pilot Metrics Module - Statistical Analysis for MCQ Quality

This module implements pilot testing metrics for MCQ evaluation:
- P-value (difficulty index): Proportion of students answering correctly
- Discrimination index: How well the question differentiates strong from weak students
- Coverage analysis: Topic and skill coverage across the question bank

These metrics are essential for validating MCQ quality before deployment.
"""

import json
import math
import statistics
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import os

# Configuration
MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-lite")
# Read GEMINI API key from environment (do not hardcode)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
try:
    import google.generativeai as genai
except Exception:
    genai = None

if genai is not None and GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception:
        # non-fatal; calls to Gemini will raise if misconfigured
        pass


class PilotMetrics:
    """Calculate and analyze pilot metrics for MCQ quality assessment."""
    
    def __init__(self, profiles_folder: str = "student_profiles", 
                 mcq_folder: str = "mcqs"):
        """Initialize the pilot metrics analyzer.
        
        Args:
            profiles_folder: Directory containing student profiles
            mcq_folder: Directory containing MCQ JSON files
        """
        self.profiles_folder = Path(profiles_folder)
        self.mcq_folder = Path(mcq_folder)
        
        # Data structures
        self.question_responses: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        self.student_total_scores: Dict[str, Dict[str, Any]] = {}
        self.all_mcqs: List[Dict[str, Any]] = []
        
    def load_mcqs(self, subjects: Optional[List[str]] = None) -> None:
        """Load MCQ bank for reference.
        
        Args:
            subjects: List of subjects to include (None for all)
        """
        self.all_mcqs = []
        mcq_files = list(self.mcq_folder.glob("*.json"))
        
        for mcq_file in mcq_files:
            if subjects is not None:
                subject_name = mcq_file.stem.replace('_mcqs', '')
                if subject_name not in subjects:
                    continue
            
            with mcq_file.open('r', encoding='utf-8') as f:
                mcqs = json.load(f)
                for idx, mcq in enumerate(mcqs):
                    mcq['mcq_id'] = f"{mcq_file.stem}_{idx}"
                    mcq['source_file'] = mcq_file.stem
                self.all_mcqs.extend(mcqs)
        
        print(f"✓ Loaded {len(self.all_mcqs)} MCQs for analysis")
    
    def collect_student_responses(self) -> None:
        """Collect all student responses from profile files."""
        print("\n📊 Collecting student responses...")
        
        self.question_responses = defaultdict(list)
        self.student_total_scores = {}
        
        profile_files = list(self.profiles_folder.glob("*.json"))
        
        if not profile_files:
            print("⚠️  No student profiles found")
            return
        
        for profile_file in profile_files:
            try:
                with profile_file.open('r', encoding='utf-8') as f:
                    profile = json.load(f)
                
                student_name = profile.get('name', profile_file.stem)
                student_correct = 0
                student_total = 0
                
                # Process all sessions
                for session in profile.get('sessions', []):
                    for question_data in session.get('questions', []):
                        # Create question identifier
                        q_text = question_data.get('question', '')
                        subject = question_data.get('subject', '')
                        topic = question_data.get('topic', '')
                        
                        # Use hash for unique ID
                        q_id = f"{subject}_{topic}_{hash(q_text[:100])}"
                        
                        # Record response
                        response_record = {
                            'student': student_name,
                            'correct': question_data.get('is_correct', False),
                            'subject': subject,
                            'topic': topic,
                            'question': q_text[:100],  # Store preview
                            'time_taken': question_data.get('time_taken', 0)
                        }
                        
                        self.question_responses[q_id].append(response_record)
                        
                        student_total += 1
                        if response_record['correct']:
                            student_correct += 1
                
                # Store student overall performance
                if student_total > 0:
                    self.student_total_scores[student_name] = {
                        'total': student_total,
                        'correct': student_correct,
                        'accuracy': (student_correct / student_total) * 100
                    }
            
            except Exception as e:
                print(f"  ⚠️  Error reading {profile_file.name}: {e}")
                continue
        
        print(f"✓ Collected responses from {len(self.student_total_scores)} students")
        print(f"✓ Total unique questions answered: {len(self.question_responses)}")
    
    def calculate_p_value(self, q_id: str) -> Optional[float]:
        """Calculate p-value (difficulty index) for a question.
        
        P-value = (Number of correct responses) / (Total responses)
        
        Interpretation:
        - p > 0.75: Very easy
        - 0.60 < p ≤ 0.75: Easy
        - 0.40 < p ≤ 0.60: Moderate (ideal)
        - 0.25 < p ≤ 0.40: Difficult
        - p ≤ 0.25: Very difficult
        
        Args:
            q_id: Question identifier
            
        Returns:
            P-value (0.0 to 1.0) or None if insufficient data
        """
        responses = self.question_responses.get(q_id, [])
        
        if not responses:
            return None
        
        correct_count = sum(1 for r in responses if r['correct'])
        total_count = len(responses)
        
        return correct_count / total_count
    
    def calculate_discrimination_index(self, q_id: str, 
                                       method: str = 'point_biserial') -> Optional[float]:
        """Calculate discrimination index for a question.
        
        Discrimination measures how well a question differentiates between
        high-performing and low-performing students.
        
        Methods:
        1. 'point_biserial': Point-biserial correlation (preferred)
        2. 'upper_lower': Upper-lower 27% group method
        
        Interpretation (point-biserial):
        - D > 0.40: Excellent discrimination
        - 0.30 < D ≤ 0.40: Good discrimination
        - 0.20 < D ≤ 0.30: Moderate discrimination (needs review)
        - 0.10 < D ≤ 0.20: Poor discrimination (consider revision)
        - D ≤ 0.10: Very poor (consider removal)
        - Negative D: Problematic (low performers do better - major issue)
        
        Args:
            q_id: Question identifier
            method: Discrimination calculation method
            
        Returns:
            Discrimination index or None if insufficient data
        """
        responses = self.question_responses.get(q_id, [])
        
        if len(responses) < 10:  # Minimum sample size
            return None
        
        if method == 'point_biserial':
            return self._calculate_point_biserial(responses)
        elif method == 'upper_lower':
            return self._calculate_upper_lower_27(responses)
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def _calculate_point_biserial(self, responses: List[Dict[str, Any]]) -> Optional[float]:
        """Calculate point-biserial correlation coefficient.
        
        This correlates binary question scores (0/1) with total test scores.
        
        Args:
            responses: List of response records
            
        Returns:
            Point-biserial correlation coefficient
        """
        # Get student total scores for students who answered this question
        student_scores = []
        question_scores = []
        
        for response in responses:
            student_name = response['student']
            if student_name not in self.student_total_scores:
                continue
            
            total_score = self.student_total_scores[student_name]['correct']
            question_score = 1 if response['correct'] else 0
            
            student_scores.append(total_score)
            question_scores.append(question_score)
        
        if len(student_scores) < 10:
            return None
        
        # Calculate point-biserial correlation
        # r_pb = (M1 - M0) / SD * sqrt(p * q)
        # where M1 = mean of students who got it right
        #       M0 = mean of students who got it wrong
        #       SD = standard deviation of all scores
        #       p = proportion correct, q = 1 - p
        
        # Separate into correct and incorrect groups
        correct_group = [student_scores[i] for i in range(len(student_scores)) 
                        if question_scores[i] == 1]
        incorrect_group = [student_scores[i] for i in range(len(student_scores)) 
                          if question_scores[i] == 0]
        
        if not correct_group or not incorrect_group:
            return None
        
        M1 = statistics.mean(correct_group)
        M0 = statistics.mean(incorrect_group)
        
        # Standard deviation of all scores
        try:
            SD = statistics.stdev(student_scores)
        except statistics.StatisticsError:
            return None
        
        if SD == 0:
            return None
        
        # Proportions
        p = len(correct_group) / len(student_scores)
        q = 1 - p
        
        # Point-biserial correlation
        r_pb = ((M1 - M0) / SD) * math.sqrt(p * q)
        
        return r_pb
    
    def _calculate_upper_lower_27(self, responses: List[Dict[str, Any]]) -> Optional[float]:
        """Calculate discrimination using upper-lower 27% method.
        
        D = (P_upper - P_lower)
        where P_upper = proportion correct in top 27% of students
              P_lower = proportion correct in bottom 27% of students
        
        Args:
            responses: List of response records
            
        Returns:
            Discrimination index
        """
        if len(responses) < 20:  # Need reasonable sample
            return None
        
        # Get student scores
        student_data = []
        for response in responses:
            student_name = response['student']
            if student_name not in self.student_total_scores:
                continue
            
            total_score = self.student_total_scores[student_name]['correct']
            question_correct = response['correct']
            
            student_data.append({
                'total_score': total_score,
                'question_correct': question_correct
            })
        
        # Sort by total score
        student_data.sort(key=lambda x: x['total_score'], reverse=True)
        
        # Select upper and lower 27%
        group_size = max(1, int(len(student_data) * 0.27))
        upper_group = student_data[:group_size]
        lower_group = student_data[-group_size:]
        
        # Calculate proportions
        p_upper = sum(1 for s in upper_group if s['question_correct']) / len(upper_group)
        p_lower = sum(1 for s in lower_group if s['question_correct']) / len(lower_group)
        
        discrimination = p_upper - p_lower
        
        return discrimination
    
    def analyze_coverage(self) -> Dict[str, Any]:
        """Analyze topic and subject coverage in the question bank.
        
        Returns:
            Coverage analysis dictionary
        """
        print("\n📈 Analyzing coverage...")
        
        # Topic coverage
        topic_counts = defaultdict(int)
        topic_questions = defaultdict(list)
        
        # Subject coverage
        subject_counts = defaultdict(int)
        
        # Difficulty distribution (based on p-values)
        difficulty_distribution = {
            'very_easy': 0,      # p > 0.75
            'easy': 0,           # 0.60 < p ≤ 0.75
            'moderate': 0,       # 0.40 < p ≤ 0.60
            'difficult': 0,      # 0.25 < p ≤ 0.40
            'very_difficult': 0, # p ≤ 0.25
            'no_data': 0         # Not yet attempted
        }
        
        # Analyze each question
        for mcq in self.all_mcqs:
            mcq_id = mcq.get('mcq_id', '')
            subject = mcq.get('subject', mcq.get('chapter', 'Unknown'))
            topic = mcq.get('topic', 'Unknown')
            
            # Count by topic
            topic_counts[topic] += 1
            topic_questions[topic].append(mcq_id)
            
            # Count by subject
            subject_counts[subject] += 1
            
            # Classify difficulty
            p_value = self.calculate_p_value(mcq_id)
            if p_value is None:
                difficulty_distribution['no_data'] += 1
            elif p_value > 0.75:
                difficulty_distribution['very_easy'] += 1
            elif p_value > 0.60:
                difficulty_distribution['easy'] += 1
            elif p_value > 0.40:
                difficulty_distribution['moderate'] += 1
            elif p_value > 0.25:
                difficulty_distribution['difficult'] += 1
            else:
                difficulty_distribution['very_difficult'] += 1
        
        # Calculate coverage metrics
        coverage_analysis = {
            'total_questions': len(self.all_mcqs),
            'total_topics': len(topic_counts),
            'total_subjects': len(subject_counts),
            'topic_coverage': dict(topic_counts),
            'subject_coverage': dict(subject_counts),
            'difficulty_distribution': difficulty_distribution,
            'topic_balance': self._calculate_topic_balance(topic_counts),
            'questions_with_responses': len([q for q in self.question_responses.keys() 
                                            if len(self.question_responses[q]) > 0]),
            'response_coverage': (len([q for q in self.question_responses.keys() 
                                      if len(self.question_responses[q]) > 0]) / 
                                 len(self.all_mcqs) * 100) if self.all_mcqs else 0
        }
        
        return coverage_analysis
    
    def _calculate_topic_balance(self, topic_counts: Dict[str, int]) -> str:
        """Assess balance of topic distribution.
        
        Args:
            topic_counts: Dictionary of topic counts
            
        Returns:
            Balance assessment string
        """
        if not topic_counts:
            return "No topics"
        
        counts = list(topic_counts.values())
        mean_count = statistics.mean(counts)
        
        try:
            stdev_count = statistics.stdev(counts)
            cv = (stdev_count / mean_count) * 100  # Coefficient of variation
            
            if cv < 20:
                return "Excellent (very balanced)"
            elif cv < 40:
                return "Good (reasonably balanced)"
            elif cv < 60:
                return "Moderate (some imbalance)"
            else:
                return "Poor (significant imbalance)"
        except statistics.StatisticsError:
            return "Uniform (all topics equal)"
    
    def generate_pilot_report(self, min_responses: int = 5) -> Dict[str, Any]:
        """Generate comprehensive pilot metrics report.
        
        Args:
            min_responses: Minimum responses required for analysis
            
        Returns:
            Pilot report dictionary
        """
        print("\n" + "="*80)
        print("GENERATING PILOT METRICS REPORT")
        print("="*80)
        
        # Collect data
        self.collect_student_responses()
        
        # Analyze each question
        question_metrics = []
        
        print(f"\n🔍 Analyzing {len(self.question_responses)} questions...")
        
        for q_id, responses in self.question_responses.items():
            if len(responses) < min_responses:
                continue
            
            # Get question details
            sample_response = responses[0]
            
            # Calculate metrics
            p_value = self.calculate_p_value(q_id)
            discrimination = self.calculate_discrimination_index(q_id, method='point_biserial')
            
            # Classify
            difficulty_class = self._classify_difficulty(p_value)
            discrimination_class = self._classify_discrimination(discrimination)
            
            # Overall quality assessment
            quality = self._assess_question_quality(p_value, discrimination)
            
            question_metrics.append({
                'question_id': q_id,
                'question_preview': sample_response['question'],
                'subject': sample_response['subject'],
                'topic': sample_response['topic'],
                'responses_count': len(responses),
                'p_value': p_value,
                'difficulty_class': difficulty_class,
                'discrimination_index': discrimination,
                'discrimination_class': discrimination_class,
                'quality_rating': quality,
                'average_time': statistics.mean([r['time_taken'] for r in responses])
            })
        
        # Sort by quality (problems first)
        question_metrics.sort(key=lambda x: (
            0 if x['quality_rating'] == 'Problematic' else
            1 if x['quality_rating'] == 'Needs Review' else
            2 if x['quality_rating'] == 'Acceptable' else 3
        ))
        
        # Coverage analysis
        coverage = self.analyze_coverage()
        
        # Summary statistics
        summary = self._generate_summary_stats(question_metrics)
        
        # Compile report
        report = {
            'generated_at': datetime.now().isoformat(),
            'total_students': len(self.student_total_scores),
            'total_questions_analyzed': len(question_metrics),
            'summary_statistics': summary,
            'coverage_analysis': coverage,
            'question_metrics': question_metrics,
            'recommendations': self._generate_recommendations(question_metrics, coverage)
        }
        
        return report
    
    def _classify_difficulty(self, p_value: Optional[float]) -> str:
        """Classify difficulty based on p-value.
        
        Args:
            p_value: P-value (difficulty index)
            
        Returns:
            Difficulty classification
        """
        if p_value is None:
            return "Unknown"
        elif p_value > 0.75:
            return "Very Easy"
        elif p_value > 0.60:
            return "Easy"
        elif p_value > 0.40:
            return "Moderate"
        elif p_value > 0.25:
            return "Difficult"
        else:
            return "Very Difficult"
    
    def _classify_discrimination(self, disc: Optional[float]) -> str:
        """Classify discrimination quality.
        
        Args:
            disc: Discrimination index
            
        Returns:
            Discrimination classification
        """
        if disc is None:
            return "Unknown"
        elif disc < 0:
            return "Problematic (Negative)"
        elif disc <= 0.10:
            return "Very Poor"
        elif disc <= 0.20:
            return "Poor"
        elif disc <= 0.30:
            return "Moderate"
        elif disc <= 0.40:
            return "Good"
        else:
            return "Excellent"
    
    def _assess_question_quality(self, p_value: Optional[float], 
                                 discrimination: Optional[float]) -> str:
        """Assess overall question quality.
        
        Args:
            p_value: P-value (difficulty index)
            discrimination: Discrimination index
            
        Returns:
            Quality rating
        """
        if p_value is None or discrimination is None:
            return "Insufficient Data"
        
        # Problematic questions
        if discrimination < 0:
            return "Problematic"
        if discrimination < 0.10:
            return "Needs Review"
        if p_value < 0.20 or p_value > 0.90:
            return "Needs Review"
        
        # Good questions
        if discrimination >= 0.30 and 0.40 <= p_value <= 0.60:
            return "Excellent"
        if discrimination >= 0.20 and 0.30 <= p_value <= 0.70:
            return "Good"
        
        return "Acceptable"
    
    def _generate_summary_stats(self, question_metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary statistics for the report.
        
        Args:
            question_metrics: List of question metric dictionaries
            
        Returns:
            Summary statistics dictionary
        """
        if not question_metrics:
            return {}
        
        # P-value statistics
        p_values = [q['p_value'] for q in question_metrics if q['p_value'] is not None]
        
        # Discrimination statistics
        disc_values = [q['discrimination_index'] for q in question_metrics 
                      if q['discrimination_index'] is not None]
        
        # Quality distribution
        quality_dist = defaultdict(int)
        for q in question_metrics:
            quality_dist[q['quality_rating']] += 1
        
        # Difficulty distribution
        difficulty_dist = defaultdict(int)
        for q in question_metrics:
            difficulty_dist[q['difficulty_class']] += 1
        
        return {
            'p_value_stats': {
                'mean': statistics.mean(p_values) if p_values else None,
                'median': statistics.median(p_values) if p_values else None,
                'stdev': statistics.stdev(p_values) if len(p_values) > 1 else None,
                'min': min(p_values) if p_values else None,
                'max': max(p_values) if p_values else None
            },
            'discrimination_stats': {
                'mean': statistics.mean(disc_values) if disc_values else None,
                'median': statistics.median(disc_values) if disc_values else None,
                'stdev': statistics.stdev(disc_values) if len(disc_values) > 1 else None,
                'min': min(disc_values) if disc_values else None,
                'max': max(disc_values) if disc_values else None
            },
            'quality_distribution': dict(quality_dist),
            'difficulty_distribution': dict(difficulty_dist)
        }
    
    def _generate_recommendations(self, question_metrics: List[Dict[str, Any]], 
                                 coverage: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations.
        
        Args:
            question_metrics: List of question metrics
            coverage: Coverage analysis
            
        Returns:
            List of recommendation strings
        """
        recommendations = []
        
        # Check for problematic questions
        problematic = [q for q in question_metrics if q['quality_rating'] == 'Problematic']
        if problematic:
            recommendations.append(
                f"🔴 CRITICAL: {len(problematic)} questions have negative discrimination. "
                "These questions are answered correctly more often by low-performing students. "
                "Review answer keys and question wording immediately."
            )
        
        # Check for questions needing review
        needs_review = [q for q in question_metrics if q['quality_rating'] == 'Needs Review']
        if needs_review:
            recommendations.append(
                f"⚠️  {len(needs_review)} questions need review due to poor discrimination "
                "or extreme difficulty. Consider revising distractors or question clarity."
            )
        
        # Check difficulty distribution
        diff_dist = coverage.get('difficulty_distribution', {})
        moderate_pct = (diff_dist.get('moderate', 0) / max(1, sum(diff_dist.values()))) * 100
        if moderate_pct < 30:
            recommendations.append(
                f"📊 Only {moderate_pct:.1f}% of questions have moderate difficulty (ideal: 40-60%). "
                "Consider adjusting question difficulty for better assessment range."
            )
        
        # Check topic balance
        balance = coverage.get('topic_balance', '')
        if 'Poor' in balance or 'Moderate' in balance:
            recommendations.append(
                f"📚 Topic distribution is {balance.lower()}. "
                "Consider adding questions to under-represented topics for better coverage."
            )
        
        # Check response coverage
        response_coverage = coverage.get('response_coverage', 0)
        if response_coverage < 50:
            recommendations.append(
                f"📝 Only {response_coverage:.1f}% of questions have student responses. "
                "Need more pilot testing data for reliable metrics."
            )
        
        # Check discrimination quality
        disc_values = [q['discrimination_index'] for q in question_metrics 
                      if q['discrimination_index'] is not None]
        if disc_values:
            avg_disc = statistics.mean(disc_values)
            if avg_disc < 0.20:
                recommendations.append(
                    f"📉 Average discrimination index is {avg_disc:.2f} (low). "
                    "Many questions are not effectively differentiating student ability. "
                    "Focus on improving distractor quality."
                )
        
        if not recommendations:
            recommendations.append("✅ Overall question quality is good. Continue monitoring metrics.")
        
        return recommendations
    
    def save_report(self, report: Dict[str, Any], 
                   output_folder: str = "validation") -> None:
        """Save pilot metrics report to JSON and markdown files.
        
        Args:
            report: Report dictionary
            output_folder: Output directory
        """
        output_path = Path(output_folder)
        output_path.mkdir(exist_ok=True)
        
        # Save JSON
        json_path = output_path / "pilot_metrics.json"
        with json_path.open('w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Saved JSON report to {json_path}")
        
        # Generate markdown
        md_path = output_path / "pilot_metrics_report.md"
        markdown = self._generate_markdown_report(report)
        with md_path.open('w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✓ Saved Markdown report to {md_path}")
    
    def _generate_markdown_report(self, report: Dict[str, Any]) -> str:
        """Generate markdown formatted report.
        
        Args:
            report: Report dictionary
            
        Returns:
            Markdown string
        """
        md = f"""# MCQ Pilot Metrics Report

**Generated:** {report['generated_at']}  
**Students:** {report['total_students']}  
**Questions Analyzed:** {report['total_questions_analyzed']}

---

## Executive Summary

This report provides statistical analysis of MCQ quality based on pilot testing data.

### Key Metrics

- **P-value (Difficulty Index):** Proportion of students answering correctly
- **Discrimination Index:** How well questions differentiate strong from weak students
- **Coverage:** Topic and difficulty distribution across the question bank

---

## Summary Statistics

### P-Value (Difficulty) Statistics

"""
        
        p_stats = report['summary_statistics'].get('p_value_stats', {})
        if p_stats.get('mean') is not None:
            stdev_str = f"{p_stats['stdev']:.3f}" if p_stats.get('stdev') is not None else "N/A"
            md += f"""
- **Mean:** {p_stats['mean']:.3f}
- **Median:** {p_stats['median']:.3f}
- **Std Dev:** {stdev_str}
- **Range:** {p_stats['min']:.3f} - {p_stats['max']:.3f}
"""
        else:
            md += "\n*Insufficient data*\n"
        
        md += "\n### Discrimination Index Statistics\n\n"
        
        disc_stats = report['summary_statistics'].get('discrimination_stats', {})
        if disc_stats.get('mean') is not None:
            stdev_str = f"{disc_stats['stdev']:.3f}" if disc_stats.get('stdev') is not None else "N/A"
            md += f"""
- **Mean:** {disc_stats['mean']:.3f}
- **Median:** {disc_stats['median']:.3f}
- **Std Dev:** {stdev_str}
- **Range:** {disc_stats['min']:.3f} - {disc_stats['max']:.3f}
"""
        else:
            md += "\n*Insufficient data*\n"
        
        # Quality distribution
        md += "\n### Question Quality Distribution\n\n"
        quality_dist = report['summary_statistics'].get('quality_distribution', {})
        for quality, count in sorted(quality_dist.items()):
            md += f"- **{quality}:** {count}\n"
        
        # Difficulty distribution
        md += "\n### Difficulty Distribution\n\n"
        diff_dist = report['summary_statistics'].get('difficulty_distribution', {})
        for difficulty, count in sorted(diff_dist.items()):
            md += f"- **{difficulty}:** {count}\n"
        
        # Coverage analysis
        md += "\n---\n\n## Coverage Analysis\n\n"
        coverage = report.get('coverage_analysis', {})
        md += f"""
- **Total Questions:** {coverage.get('total_questions', 0)}
- **Total Topics:** {coverage.get('total_topics', 0)}
- **Total Subjects:** {coverage.get('total_subjects', 0)}
- **Questions with Responses:** {coverage.get('questions_with_responses', 0)}
- **Response Coverage:** {coverage.get('response_coverage', 0):.1f}%
- **Topic Balance:** {coverage.get('topic_balance', 'Unknown')}

### Subject Distribution

"""
        
        subject_coverage = coverage.get('subject_coverage', {})
        for subject, count in sorted(subject_coverage.items(), key=lambda x: x[1], reverse=True):
            md += f"- **{subject}:** {count} questions\n"
        
        md += "\n### Top 10 Topics by Question Count\n\n"
        topic_coverage = coverage.get('topic_coverage', {})
        sorted_topics = sorted(topic_coverage.items(), key=lambda x: x[1], reverse=True)[:10]
        for topic, count in sorted_topics:
            md += f"- **{topic[:50]}:** {count} questions\n"
        
        # Recommendations
        md += "\n---\n\n## Recommendations\n\n"
        for idx, rec in enumerate(report.get('recommendations', []), 1):
            md += f"{idx}. {rec}\n\n"
        
        # Detailed question metrics (top issues)
        md += "\n---\n\n## Detailed Question Analysis\n\n"
        md += "### Questions Requiring Attention (Top 20)\n\n"
        
        question_metrics = report.get('question_metrics', [])
        problem_questions = [q for q in question_metrics 
                           if q['quality_rating'] in ['Problematic', 'Needs Review']][:20]
        
        if problem_questions:
            md += "| Preview | Subject | Topic | Responses | P-Value | Difficulty | Discrimination | Quality |\n"
            md += "|---------|---------|-------|-----------|---------|------------|----------------|----------|\n"
            
            for q in problem_questions:
                preview = q['question_preview'][:40] + "..."
                md += f"| {preview} | {q['subject'][:15]} | {q['topic'][:15]} | "
                md += f"{q['responses_count']} | {q['p_value']:.3f} | {q['difficulty_class']} | "
                md += f"{q['discrimination_index']:.3f} | {q['quality_rating']} |\n"
        else:
            md += "\n*No problematic questions identified!*\n"
        
        # Best performing questions
        md += "\n### Best Performing Questions (Top 10)\n\n"
        excellent_questions = [q for q in question_metrics 
                              if q['quality_rating'] in ['Excellent', 'Good']][:10]
        
        if excellent_questions:
            md += "| Preview | Subject | Topic | Responses | P-Value | Discrimination | Quality |\n"
            md += "|---------|---------|-------|-----------|---------|----------------|----------|\n"
            
            for q in excellent_questions:
                preview = q['question_preview'][:40] + "..."
                md += f"| {preview} | {q['subject'][:15]} | {q['topic'][:15]} | "
                md += f"{q['responses_count']} | {q['p_value']:.3f} | "
                md += f"{q['discrimination_index']:.3f} | {q['quality_rating']} |\n"
        
        md += "\n---\n\n## Interpretation Guide\n\n"
        md += """
### P-Value (Difficulty Index)

- **> 0.75:** Very Easy
- **0.60 - 0.75:** Easy
- **0.40 - 0.60:** Moderate (Ideal for most assessments)
- **0.25 - 0.40:** Difficult
- **< 0.25:** Very Difficult

### Discrimination Index (Point-Biserial)

- **> 0.40:** Excellent discrimination
- **0.30 - 0.40:** Good discrimination
- **0.20 - 0.30:** Moderate (needs review)
- **0.10 - 0.20:** Poor (consider revision)
- **< 0.10:** Very poor (consider removal)
- **Negative:** Problematic (major issue - review answer key)

### Quality Ratings

- **Excellent:** Strong discrimination + moderate difficulty
- **Good:** Acceptable discrimination + reasonable difficulty
- **Acceptable:** Meets minimum standards
- **Needs Review:** Poor discrimination or extreme difficulty
- **Problematic:** Negative discrimination or critical issues

---

*Report generated by MCQ Pilot Metrics Analyzer*
"""
        
        return md


def main():
    """Main entry point for pilot metrics analysis."""
    print("="*80)
    print("MCQ PILOT METRICS ANALYZER")
    print("="*80)
    print("\nThis tool analyzes MCQ quality using statistical metrics:")
    print("- P-value (difficulty index)")
    print("- Discrimination index")
    print("- Coverage analysis")
    print()
    
    # Initialize analyzer
    analyzer = PilotMetrics()
    
    # Load MCQ bank
    print("Loading MCQ bank...")
    analyzer.load_mcqs()
    
    # Generate report
    print("\nAnalyzing pilot data...")
    report = analyzer.generate_pilot_report(min_responses=3)
    
    # Display summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Students analyzed: {report['total_students']}")
    print(f"   Questions analyzed: {report['total_questions_analyzed']}")
    
    # Show key recommendations
    print(f"\n🎯 Key Recommendations:")
    for idx, rec in enumerate(report.get('recommendations', []), 1):
        print(f"\n{idx}. {rec}")
    
    # Save report
    print("\n" + "="*80)
    analyzer.save_report(report)
    
    print("\n✅ Pilot metrics analysis complete!")
    print("   Check the 'validation' folder for detailed reports.")


if __name__ == "__main__":
    main()
