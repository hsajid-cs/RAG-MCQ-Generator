"""Adaptive Question Selection Module - IRT-based MCQ Selection

This module implements Item Response Theory (IRT) for adaptive question selection:
- Maintains θ (theta) parameters representing student ability per topic
- Estimates question difficulty based on performance data
- Balances topic coverage
- Provides AI-powered insights using Gemini API
"""

import json
import math
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from collections import defaultdict
import google.generativeai as genai


# Configuration
GEMINI_API_KEY = "AIzaSyAXXDD1M89vEiDL9uP5ke-viAOz7hmb8ck"
MODEL_NAME = "gemini-2.5-flash-lite"
genai.configure(api_key=GEMINI_API_KEY)


class AdaptiveSelector:
    """Adaptive question selection using IRT (Item Response Theory)."""
    
    def __init__(self, mcq_folder: str = "mcqs", profiles_folder: str = "student_profiles"):
        """Initialize the adaptive selector.
        
        Args:
            mcq_folder: Directory containing MCQ JSON files
            profiles_folder: Directory containing student profiles
        """
        self.mcq_folder = Path(mcq_folder)
        self.profiles_folder = Path(profiles_folder)
        
        self.all_mcqs: List[Dict[str, Any]] = []
        self.question_stats: Dict[str, Dict[str, Any]] = {}
        self.student_profile: Dict[str, Any] = {}
        
        # IRT parameters
        self.initial_theta = 0.0  # Starting ability (centered at 0)
        self.theta_range = (-3.0, 3.0)  # Typical range for theta
        
    def load_mcqs(self, subjects: Optional[List[str]] = None) -> None:
        """Load MCQs from JSON files.
        
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
                # Add unique ID and metadata
                for idx, mcq in enumerate(mcqs):
                    mcq['mcq_id'] = f"{mcq_file.stem}_{idx}"
                    mcq['source_file'] = mcq_file.stem
                self.all_mcqs.extend(mcqs)
        
        print(f"Loaded {len(self.all_mcqs)} MCQs for adaptive selection")
    
    def load_student_profile(self, student_name: str) -> bool:
        """Load student profile for adaptive selection.
        
        Args:
            student_name: Name of the student
            
        Returns:
            True if profile exists, False otherwise
        """
        profile_path = self.profiles_folder / f"{student_name}.json"
        
        if not profile_path.exists():
            return False
        
        with profile_path.open('r', encoding='utf-8') as f:
            self.student_profile = json.load(f)
        
        return True
    
    def estimate_question_difficulty(self, mcq_id: str) -> float:
        """Estimate difficulty of a question based on historical data.
        
        Uses IRT model where difficulty 'b' is estimated from success rate:
        - Higher success rate → easier question (lower b)
        - Lower success rate → harder question (higher b)
        
        Args:
            mcq_id: Unique question identifier
            
        Returns:
            Difficulty parameter (b) typically in range [-3, 3]
        """
        # Default difficulty if no data
        default_difficulty = 0.0
        
        # Gather statistics from all student profiles
        if mcq_id not in self.question_stats:
            self.question_stats[mcq_id] = {
                'attempts': 0,
                'correct': 0,
                'difficulty': default_difficulty
            }
            return default_difficulty
        
        stats = self.question_stats[mcq_id]
        attempts = stats.get('attempts', 0)
        correct = stats.get('correct', 0)
        
        if attempts == 0:
            return default_difficulty
        
        # Calculate success rate
        success_rate = correct / attempts
        
        # Convert success rate to difficulty using inverse logistic
        # success_rate = 1 / (1 + exp(-(theta - b)))
        # For average student (theta=0), b = -ln((1/success_rate) - 1)
        
        # Avoid edge cases
        success_rate = max(0.01, min(0.99, success_rate))
        
        # Calculate difficulty
        difficulty = -math.log((1 / success_rate) - 1)
        
        # Clamp to reasonable range
        difficulty = max(-3.0, min(3.0, difficulty))
        
        return difficulty
    
    def get_student_theta(self, topic: str) -> float:
        """Get student's ability (theta) for a specific topic.
        
        Args:
            topic: Topic name
            
        Returns:
            Theta value (ability parameter)
        """
        if not self.student_profile:
            return self.initial_theta
        
        # Check if we have theta tracking
        if 'theta_by_topic' not in self.student_profile:
            self.student_profile['theta_by_topic'] = {}
        
        # Return existing theta or initial value
        return self.student_profile['theta_by_topic'].get(topic, self.initial_theta)
    
    def update_student_theta(self, topic: str, correct: bool, difficulty: float) -> float:
        """Update student's theta based on response using IRT.
        
        Uses Maximum Likelihood Estimation (MLE) approach:
        - If correct: increase theta
        - If incorrect: decrease theta
        - Magnitude of change depends on difficulty and current theta
        
        Args:
            topic: Topic name
            correct: Whether student answered correctly
            difficulty: Question difficulty parameter
            
        Returns:
            Updated theta value
        """
        current_theta = self.get_student_theta(topic)
        
        # Calculate expected probability of correct answer
        # P(correct) = 1 / (1 + exp(-(theta - b)))
        prob_correct = 1 / (1 + math.exp(-(current_theta - difficulty)))
        
        # Update step size (learning rate)
        # Larger when question is well-matched to ability
        learning_rate = prob_correct * (1 - prob_correct)
        
        # Update theta based on response
        if correct:
            # Answered correctly: increase theta
            delta = learning_rate * (1 - prob_correct)
        else:
            # Answered incorrectly: decrease theta
            delta = -learning_rate * prob_correct
        
        # Apply update with dampening factor
        dampening = 0.3  # Prevents wild swings
        new_theta = current_theta + dampening * delta
        
        # Clamp to valid range
        new_theta = max(self.theta_range[0], min(self.theta_range[1], new_theta))
        
        # Update profile
        if 'theta_by_topic' not in self.student_profile:
            self.student_profile['theta_by_topic'] = {}
        self.student_profile['theta_by_topic'][topic] = new_theta
        
        return new_theta
    
    def calculate_question_score(self, mcq: Dict[str, Any], 
                                 target_theta: float,
                                 topic_coverage: Dict[str, int]) -> float:
        """Calculate selection score for a question.
        
        Balances:
        1. Difficulty matching (questions close to student ability)
        2. Topic balance (prefer under-practiced topics)
        3. Randomness (exploration vs exploitation)
        
        Args:
            mcq: MCQ dictionary
            target_theta: Target ability level
            topic_coverage: Count of questions per topic already selected
            
        Returns:
            Selection score (higher = better)
        """
        # Estimate difficulty
        difficulty = self.estimate_question_difficulty(mcq.get('mcq_id', ''))
        
        # 1. Difficulty matching score
        # Prefer questions close to student's ability
        difficulty_diff = abs(target_theta - difficulty)
        difficulty_score = math.exp(-difficulty_diff)  # Exponential decay
        
        # 2. Topic balance score
        topic = mcq.get('topic', 'Unknown')
        times_practiced = topic_coverage.get(topic, 0)
        # Prefer less-practiced topics
        balance_score = 1.0 / (1 + times_practiced)
        
        # 3. Combine scores
        # Weight: 70% difficulty matching, 30% topic balance
        final_score = 0.7 * difficulty_score + 0.3 * balance_score
        
        # 4. Add small random factor for exploration
        random_factor = random.uniform(0.95, 1.05)
        final_score *= random_factor
        
        return final_score
    
    def select_adaptive_questions(self, student_name: str, 
                                  num_questions: int = 10,
                                  subjects: Optional[List[str]] = None,
                                  focus_topics: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Select questions adaptively based on student ability.
        
        Args:
            student_name: Name of the student
            num_questions: Number of questions to select
            subjects: Filter by subjects
            focus_topics: Optional list of topics to focus on
            
        Returns:
            List of selected MCQs
        """
        # Load data
        self.load_mcqs(subjects)
        self.load_student_profile(student_name)
        
        if not self.all_mcqs:
            print("No MCQs available.")
            return []
        
        # Build global question statistics
        self._build_question_statistics()
        
        # Calculate average theta across topics (general ability)
        theta_values = list(self.student_profile.get('theta_by_topic', {}).values())
        avg_theta = sum(theta_values) / len(theta_values) if theta_values else self.initial_theta
        
        # Track topic coverage in this selection
        topic_coverage: Dict[str, int] = defaultdict(int)
        
        # Filter MCQs by focus topics if specified
        candidate_mcqs = self.all_mcqs
        if focus_topics:
            candidate_mcqs = [mcq for mcq in self.all_mcqs 
                            if mcq.get('topic', '') in focus_topics]
        
        # Score and rank questions
        scored_questions: List[Tuple[float, Dict[str, Any]]] = []
        
        for mcq in candidate_mcqs:
            topic = mcq.get('topic', 'Unknown')
            topic_theta = self.get_student_theta(topic)
            
            # Use topic-specific theta if available, else use average
            target_theta = topic_theta if topic in self.student_profile.get('theta_by_topic', {}) else avg_theta
            
            score = self.calculate_question_score(mcq, target_theta, topic_coverage)
            scored_questions.append((score, mcq))
        
        # Sort by score (descending)
        scored_questions.sort(key=lambda x: x[0], reverse=True)
        
        # Select top questions, updating topic coverage
        selected: List[Dict[str, Any]] = []
        for score, mcq in scored_questions:
            if len(selected) >= num_questions:
                break
            
            topic = mcq.get('topic', 'Unknown')
            topic_coverage[topic] += 1
            selected.append(mcq)
        
        return selected
    
    def _build_question_statistics(self) -> None:
        """Build global statistics for all questions from all student profiles."""
        self.question_stats = {}
        
        # Scan all student profiles
        for profile_file in self.profiles_folder.glob("*.json"):
            try:
                with profile_file.open('r', encoding='utf-8') as f:
                    profile = json.load(f)
                
                # Extract question responses from sessions
                for session in profile.get('sessions', []):
                    for question in session.get('questions', []):
                        # Build question ID (approximate)
                        q_text = question.get('question', '')[:50]
                        subject = question.get('subject', '')
                        mcq_id = f"{subject}_{hash(q_text)}"
                        
                        if mcq_id not in self.question_stats:
                            self.question_stats[mcq_id] = {
                                'attempts': 0,
                                'correct': 0,
                                'difficulty': 0.0
                            }
                        
                        self.question_stats[mcq_id]['attempts'] += 1
                        if question.get('is_correct', False):
                            self.question_stats[mcq_id]['correct'] += 1
            except:
                continue
        
        # Recalculate difficulty for all questions
        for mcq_id, stats in self.question_stats.items():
            stats['difficulty'] = self.estimate_question_difficulty(mcq_id)
    
    def generate_insights(self, student_name: str) -> str:
        """Generate AI-powered insights about student performance using Gemini.
        
        Args:
            student_name: Name of the student
            
        Returns:
            Insights text
        """
        if not self.load_student_profile(student_name):
            return "No profile found for student."
        
        # Prepare summary data
        total_attempted = self.student_profile.get('total_questions_attempted', 0)
        total_correct = self.student_profile.get('total_correct', 0)
        
        if total_attempted == 0:
            return "Not enough practice data to generate insights."
        
        accuracy = (total_correct / total_attempted) * 100
        
        # Theta by topic
        theta_by_topic = self.student_profile.get('theta_by_topic', {})
        
        # Topic performance
        topic_performance = self.student_profile.get('topic_performance', {})
        
        # Recent sessions
        recent_sessions = self.student_profile.get('sessions', [])[-3:]
        
        # Build prompt
        prompt = f"""You are an expert educational AI tutor. Analyze this student's performance and provide personalized insights.

Student: {student_name}

Overall Performance:
- Total Questions: {total_attempted}
- Accuracy: {accuracy:.1f}%
- Sessions Completed: {len(self.student_profile.get('sessions', []))}

Ability by Topic (θ values, range -3 to +3, higher is better):
{json.dumps(theta_by_topic, indent=2)}

Topic-wise Performance:
{json.dumps({k: f"{v['correct']}/{v['total']} ({(v['correct']/v['total']*100):.1f}%)" 
             for k, v in sorted(topic_performance.items(), key=lambda x: x[1]['total'], reverse=True)[:10]}, indent=2)}

Recent Session Trends:
{json.dumps([{
    'correct': s['correct_count'],
    'total': s['total_count'],
    'subjects': list(s.get('subject_breakdown', {}).keys())
} for s in recent_sessions], indent=2)}

Provide:
1. **Strengths**: What topics the student excels at
2. **Areas for Improvement**: Topics needing more practice
3. **Learning Trajectory**: Progress over recent sessions
4. **Recommendations**: 3-5 specific actionable study tips
5. **Next Steps**: Suggested topics to focus on next

Keep response concise (300-400 words), encouraging, and actionable."""

        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1024,
                )
            )
            return response.text
        except Exception as e:
            return f"Error generating insights: {e}"
    
    def get_recommended_difficulty_range(self, student_name: str, 
                                        topic: Optional[str] = None) -> Tuple[float, float]:
        """Get recommended difficulty range for question selection.
        
        Args:
            student_name: Name of the student
            topic: Specific topic (None for general)
            
        Returns:
            Tuple of (min_difficulty, max_difficulty)
        """
        self.load_student_profile(student_name)
        
        if topic:
            theta = self.get_student_theta(topic)
        else:
            # Use average theta
            theta_values = list(self.student_profile.get('theta_by_topic', {}).values())
            theta = sum(theta_values) / len(theta_values) if theta_values else self.initial_theta
        
        # Recommend questions within ±1 standard deviation of ability
        min_diff = theta - 1.0
        max_diff = theta + 1.0
        
        return (min_diff, max_diff)


def main():
    """Main entry point for testing adaptive selector."""
    print("="*70)
    print("ADAPTIVE QUESTION SELECTOR - DEMO")
    print("="*70)
    
    selector = AdaptiveSelector()
    
    # Example: Select adaptive questions
    student_name = input("\nEnter student name: ").strip()
    if not student_name:
        print("Name cannot be empty.")
        return
    
    num_questions = input("Number of questions (default 10): ").strip()
    num_questions = int(num_questions) if num_questions.isdigit() else 10
    
    # Select questions
    selected = selector.select_adaptive_questions(student_name, num_questions)
    
    print(f"\n{'='*70}")
    print(f"Selected {len(selected)} adaptive questions")
    print(f"{'='*70}")
    
    for idx, mcq in enumerate(selected, 1):
        topic = mcq.get('topic', 'Unknown')
        difficulty = selector.estimate_question_difficulty(mcq.get('mcq_id', ''))
        theta = selector.get_student_theta(topic)
        
        print(f"\n{idx}. {mcq.get('question', '')[:60]}...")
        print(f"   Topic: {topic}")
        print(f"   Difficulty: {difficulty:.2f} | Student θ: {theta:.2f}")
    
    # Generate insights
    print(f"\n{'='*70}")
    print("GENERATING AI INSIGHTS...")
    print(f"{'='*70}")
    
    insights = selector.generate_insights(student_name)
    print(f"\n{insights}")


if __name__ == "__main__":
    main()
