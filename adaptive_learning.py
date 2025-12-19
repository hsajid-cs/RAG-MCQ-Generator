"""Adaptive Learning System - Integrated MCQ Practice with IRT

This module combines student assessment with adaptive question selection:
- Uses IRT-based difficulty estimation and student ability tracking
- Updates θ parameters in real-time based on responses
- Provides personalized question selection
- Generates AI-powered learning insights
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import random

# Import our modules
from adaptive_selector import AdaptiveSelector


class AdaptiveLearningSystem:
    """Integrated adaptive learning system with IRT and AI insights."""
    
    def __init__(self, mcq_folder: str = "mcqs", profiles_folder: str = "student_profiles"):
        """Initialize the adaptive learning system.
        
        Args:
            mcq_folder: Directory containing MCQ JSON files
            profiles_folder: Directory to store student profiles
        """
        self.mcq_folder = Path(mcq_folder)
        self.profiles_folder = Path(profiles_folder)
        self.profiles_folder.mkdir(exist_ok=True)
        
        self.student_name: Optional[str] = None
        self.student_profile: Dict[str, Any] = {}
        self.session_data: Dict[str, Any] = {}
        
        # Initialize adaptive selector
        self.selector = AdaptiveSelector(mcq_folder, profiles_folder)
    
    def load_or_create_profile(self, student_name: str) -> None:
        """Load existing student profile or create a new one.
        
        Args:
            student_name: Name of the student
        """
        self.student_name = student_name
        profile_path = self.profiles_folder / f"{student_name}.json"
        
        if profile_path.exists():
            with profile_path.open('r', encoding='utf-8') as f:
                self.student_profile = json.load(f)
            print(f"✓ Welcome back, {student_name}!")
            
            # Show quick stats
            total = self.student_profile.get('total_questions_attempted', 0)
            if total > 0:
                correct = self.student_profile.get('total_correct', 0)
                accuracy = (correct / total) * 100
                print(f"  Your overall accuracy: {accuracy:.1f}% ({correct}/{total})")
        else:
            self.student_profile = {
                'name': student_name,
                'created_at': datetime.now().isoformat(),
                'sessions': [],
                'total_questions_attempted': 0,
                'total_correct': 0,
                'topic_performance': {},
                'subject_performance': {},
                'theta_by_topic': {}  # IRT ability parameters
            }
            print(f"✓ Creating new profile for {student_name}")
    
    def save_profile(self) -> None:
        """Save student profile to disk."""
        if not self.student_name:
            return
        
        profile_path = self.profiles_folder / f"{self.student_name}.json"
        with profile_path.open('w', encoding='utf-8') as f:
            json.dump(self.student_profile, f, indent=2, ensure_ascii=False)
    
    def display_question(self, mcq: Dict[str, Any], question_num: int, total: int) -> None:
        """Display a single MCQ to the student.
        
        Args:
            mcq: MCQ dictionary
            question_num: Current question number
            total: Total number of questions in session
        """
        print("\n" + "="*80)
        print(f"Question {question_num}/{total}")
        print("="*80)
        
        # Display metadata
        if 'subject' in mcq:
            print(f"📚 Subject: {mcq['subject']}")
        if 'chapter' in mcq:
            print(f"📖 Chapter: {mcq['chapter']}")
        if 'topic' in mcq:
            topic = mcq['topic']
            print(f"🎯 Topic: {topic}")
            
            # Show student's current ability for this topic
            theta = self.student_profile.get('theta_by_topic', {}).get(topic)
            if theta is not None:
                print(f"   Your ability (θ): {theta:.2f}")
        
        # Display passage if exists (for SAT English)
        if 'passage' in mcq and mcq['passage']:
            print(f"\n📄 Passage:")
            print("-" * 80)
            print(mcq['passage'])
            print("-" * 80)
        
        # Display question
        print(f"\n❓ {mcq['question']}")
        print()
        
        # Display choices
        choices = mcq.get('choices', [])
        for idx, choice in enumerate(choices):
            label = chr(65 + idx)  # A, B, C, D
            print(f"   {label}. {choice}")
    
    def get_student_answer(self) -> str:
        """Get answer from student.
        
        Returns:
            Student's answer (A, B, C, or D) or 'Q' to quit
        """
        while True:
            answer = input("\n➤ Your answer (A/B/C/D) or 'q' to quit: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D', 'Q']:
                return answer
            print("❌ Invalid input. Please enter A, B, C, D, or Q.")
    
    def evaluate_and_update(self, mcq: Dict[str, Any], student_answer: str) -> bool:
        """Evaluate answer, provide feedback, and update student ability.
        
        Args:
            mcq: MCQ dictionary
            student_answer: Student's answer
            
        Returns:
            True if correct, False otherwise
        """
        correct_answer = mcq.get('answer', '')
        is_correct = (student_answer == correct_answer)
        
        print("\n" + "-"*80)
        if is_correct:
            print("✅ CORRECT! Well done!")
        else:
            print(f"❌ INCORRECT. The correct answer is: {correct_answer}")
        
        # Display rationale
        if 'rationale' in mcq:
            print(f"\n💡 Explanation:")
            print(f"   {mcq['rationale']}")
        
        # Show correct choice text
        choices = mcq.get('choices', [])
        if correct_answer in ['A', 'B', 'C', 'D']:
            choice_idx = ord(correct_answer) - 65
            if 0 <= choice_idx < len(choices):
                print(f"\n✓ Correct answer: {correct_answer}. {choices[choice_idx]}")
        
        # Update IRT parameters
        topic = mcq.get('topic', 'Unknown')
        difficulty = self.selector.estimate_question_difficulty(mcq.get('mcq_id', ''))
        
        # Update theta
        old_theta = self.selector.get_student_theta(topic)
        new_theta = self.selector.update_student_theta(topic, is_correct, difficulty)
        
        # Update the main profile's theta
        if 'theta_by_topic' not in self.student_profile:
            self.student_profile['theta_by_topic'] = {}
        self.student_profile['theta_by_topic'][topic] = new_theta
        
        # Show theta update
        theta_change = new_theta - old_theta
        if theta_change > 0:
            print(f"\n📈 Your ability in '{topic}' increased: {old_theta:.2f} → {new_theta:.2f} (+{theta_change:.2f})")
        elif theta_change < 0:
            print(f"\n📉 Your ability in '{topic}' adjusted: {old_theta:.2f} → {new_theta:.2f} ({theta_change:.2f})")
        else:
            print(f"\n📊 Your ability in '{topic}': {new_theta:.2f} (no change)")
        
        print("-"*80)
        
        return is_correct
    
    def run_adaptive_session(self, num_questions: int = 10,
                           subjects: Optional[List[str]] = None,
                           focus_topics: Optional[List[str]] = None) -> None:
        """Run an adaptive practice session with IRT-based question selection.
        
        Args:
            num_questions: Number of questions for this session
            subjects: List of subjects to include
            focus_topics: Optional topics to focus on
        """
        if not self.student_name:
            print("❌ No student profile loaded.")
            return
        
        # Select adaptive questions
        print(f"\n🔍 Selecting {num_questions} adaptive questions based on your ability...")
        
        # Update selector's student profile
        self.selector.student_profile = self.student_profile
        
        selected_mcqs = self.selector.select_adaptive_questions(
            self.student_name,
            num_questions,
            subjects,
            focus_topics
        )
        
        if not selected_mcqs:
            print("❌ No questions available. Please check MCQ files.")
            return
        
        # Initialize session data
        self.session_data = {
            'start_time': datetime.now().isoformat(),
            'questions': [],
            'correct_count': 0,
            'total_count': len(selected_mcqs),
            'subject_breakdown': {},
            'topic_breakdown': {},
            'theta_changes': {}
        }
        
        print(f"\n{'='*80}")
        print(f"🎓 ADAPTIVE PRACTICE SESSION")
        print(f"   {len(selected_mcqs)} questions selected based on your current ability")
        print(f"{'='*80}")
        
        # Ask each question
        for idx, mcq in enumerate(selected_mcqs, 1):
            start_time = time.time()
            
            self.display_question(mcq, idx, len(selected_mcqs))
            student_answer = self.get_student_answer()
            
            if student_answer == 'Q':
                print("\n⚠️  Session ended by user.")
                break
            
            end_time = time.time()
            time_taken = end_time - start_time
            
            is_correct = self.evaluate_and_update(mcq, student_answer)
            
            # Record question data
            topic = mcq.get('topic', 'Unknown')
            question_data = {
                'question': mcq.get('question', '')[:100] + '...',
                'subject': mcq.get('subject', mcq.get('chapter', 'Unknown')),
                'topic': topic,
                'correct_answer': mcq.get('answer', ''),
                'student_answer': student_answer,
                'is_correct': is_correct,
                'time_taken': round(time_taken, 2),
                'difficulty': self.selector.estimate_question_difficulty(mcq.get('mcq_id', '')),
                'theta_before': self.selector.get_student_theta(topic),
                'theta_after': self.student_profile.get('theta_by_topic', {}).get(topic, 0.0)
            }
            
            self.session_data['questions'].append(question_data)
            
            if is_correct:
                self.session_data['correct_count'] += 1
            
            # Update breakdowns
            subject = question_data['subject']
            
            if subject not in self.session_data['subject_breakdown']:
                self.session_data['subject_breakdown'][subject] = {'correct': 0, 'total': 0}
            self.session_data['subject_breakdown'][subject]['total'] += 1
            if is_correct:
                self.session_data['subject_breakdown'][subject]['correct'] += 1
            
            if topic not in self.session_data['topic_breakdown']:
                self.session_data['topic_breakdown'][topic] = {'correct': 0, 'total': 0}
            self.session_data['topic_breakdown'][topic]['total'] += 1
            if is_correct:
                self.session_data['topic_breakdown'][topic]['correct'] += 1
            
            # Pause between questions
            if idx < len(selected_mcqs):
                input("\n➤ Press Enter for next question...")
        
        # End session
        self.session_data['end_time'] = datetime.now().isoformat()
        self.display_session_summary()
        self.update_profile()
        self.save_profile()
    
    def display_session_summary(self) -> None:
        """Display comprehensive session summary with IRT insights."""
        print("\n" + "="*80)
        print("📊 SESSION SUMMARY")
        print("="*80)
        
        correct = self.session_data['correct_count']
        total = len(self.session_data['questions'])
        
        if total == 0:
            print("No questions were attempted.")
            return
        
        accuracy = (correct / total) * 100
        
        print(f"\n🎯 Overall Performance:")
        print(f"   Correct: {correct}/{total} ({accuracy:.1f}%)")
        
        # Subject breakdown
        if self.session_data['subject_breakdown']:
            print(f"\n📚 Performance by Subject:")
            for subject, stats in self.session_data['subject_breakdown'].items():
                subj_acc = (stats['correct'] / stats['total']) * 100
                print(f"   {subject}: {stats['correct']}/{stats['total']} ({subj_acc:.1f}%)")
        
        # Topic breakdown with theta changes
        if self.session_data['topic_breakdown']:
            print(f"\n🎯 Performance by Topic (with ability changes):")
            for topic, stats in sorted(self.session_data['topic_breakdown'].items()):
                topic_acc = (stats['correct'] / stats['total']) * 100
                
                # Calculate theta change for this topic
                topic_questions = [q for q in self.session_data['questions'] if q['topic'] == topic]
                if topic_questions:
                    theta_start = topic_questions[0]['theta_before']
                    theta_end = topic_questions[-1]['theta_after']
                    theta_change = theta_end - theta_start
                    change_indicator = "↑" if theta_change > 0 else "↓" if theta_change < 0 else "→"
                    
                    print(f"   {topic[:50]}: {stats['correct']}/{stats['total']} ({topic_acc:.1f}%) "
                          f"| θ: {theta_start:.2f} {change_indicator} {theta_end:.2f}")
        
        # Average metrics
        total_time = sum(q['time_taken'] for q in self.session_data['questions'])
        avg_time = total_time / total if total > 0 else 0
        
        avg_difficulty = sum(q['difficulty'] for q in self.session_data['questions']) / total if total > 0 else 0
        
        print(f"\n⏱️  Average time per question: {avg_time:.1f} seconds")
        print(f"📊 Average question difficulty: {avg_difficulty:.2f}")
        
        print("="*80)
    
    def update_profile(self) -> None:
        """Update student profile with session data."""
        # Add session to history
        self.student_profile['sessions'].append(self.session_data)
        
        # Update totals
        self.student_profile['total_questions_attempted'] += len(self.session_data['questions'])
        self.student_profile['total_correct'] += self.session_data['correct_count']
        
        # Update subject performance
        for subject, stats in self.session_data['subject_breakdown'].items():
            if subject not in self.student_profile['subject_performance']:
                self.student_profile['subject_performance'][subject] = {'correct': 0, 'total': 0}
            self.student_profile['subject_performance'][subject]['correct'] += stats['correct']
            self.student_profile['subject_performance'][subject]['total'] += stats['total']
        
        # Update topic performance
        for topic, stats in self.session_data['topic_breakdown'].items():
            if topic not in self.student_profile['topic_performance']:
                self.student_profile['topic_performance'][topic] = {'correct': 0, 'total': 0}
            self.student_profile['topic_performance'][topic]['correct'] += stats['correct']
            self.student_profile['topic_performance'][topic]['total'] += stats['total']
        
        # Update last activity
        self.student_profile['last_activity'] = datetime.now().isoformat()
    
    def show_student_dashboard(self) -> None:
        """Display comprehensive student dashboard with IRT metrics."""
        if not self.student_profile:
            print("No profile loaded.")
            return
        
        print("\n" + "="*80)
        print(f"👤 STUDENT DASHBOARD: {self.student_profile.get('name', 'Unknown')}")
        print("="*80)
        
        total = self.student_profile.get('total_questions_attempted', 0)
        correct = self.student_profile.get('total_correct', 0)
        
        if total == 0:
            print("\n⚠️  No practice sessions completed yet.")
            return
        
        accuracy = (correct / total) * 100
        print(f"\n📊 Overall Statistics:")
        print(f"   Total Questions: {total}")
        print(f"   Total Correct: {correct}")
        print(f"   Overall Accuracy: {accuracy:.1f}%")
        print(f"   Sessions Completed: {len(self.student_profile.get('sessions', []))}")
        
        # Ability (theta) by topic
        theta_by_topic = self.student_profile.get('theta_by_topic', {})
        if theta_by_topic:
            print(f"\n🎯 Ability Levels by Topic (θ values):")
            sorted_topics = sorted(theta_by_topic.items(), key=lambda x: x[1], reverse=True)
            for topic, theta in sorted_topics[:10]:
                # Color code based on ability
                if theta >= 1.0:
                    indicator = "🟢 Strong"
                elif theta >= 0:
                    indicator = "🟡 Good"
                elif theta >= -1.0:
                    indicator = "🟠 Developing"
                else:
                    indicator = "🔴 Needs Work"
                
                print(f"   {indicator} | {topic[:45]}: θ = {theta:.2f}")
        
        # Subject performance
        print(f"\n📚 Performance by Subject:")
        for subject, stats in self.student_profile.get('subject_performance', {}).items():
            subj_acc = (stats['correct'] / stats['total']) * 100
            print(f"   {subject}: {stats['correct']}/{stats['total']} ({subj_acc:.1f}%)")
        
        print("="*80)
    
    def get_ai_insights(self) -> None:
        """Generate and display AI-powered learning insights."""
        if not self.student_name:
            print("❌ No student profile loaded.")
            return
        
        print("\n" + "="*80)
        print("🤖 GENERATING AI-POWERED INSIGHTS...")
        print("="*80)
        print("⏳ Please wait, analyzing your learning patterns...")
        
        insights = self.selector.generate_insights(self.student_name)
        
        print("\n" + "="*80)
        print("💡 PERSONALIZED LEARNING INSIGHTS")
        print("="*80)
        print(insights)
        print("="*80)


def main():
    """Main entry point for adaptive learning system."""
    print("="*80)
    print("🎓 ADAPTIVE LEARNING SYSTEM - IRT-Based MCQ Practice")
    print("="*80)
    
    # Get student name
    student_name = input("\n➤ Enter your name: ").strip()
    if not student_name:
        print("❌ Name cannot be empty.")
        return
    
    # Initialize system
    system = AdaptiveLearningSystem()
    system.load_or_create_profile(student_name)
    
    # Main menu
    while True:
        print("\n" + "="*80)
        print("📋 MAIN MENU")
        print("="*80)
        print("1. 🎯 Start Adaptive Practice Session")
        print("2. 📊 View My Dashboard")
        print("3. 💡 Get AI Learning Insights")
        print("4. 🚪 Exit")
        
        choice = input("\n➤ Select an option (1-4): ").strip()
        
        if choice == '1':
            # Configure session
            print("\n⚙️  Session Configuration:")
            
            # Number of questions
            num_input = input("   Number of questions (default 10): ").strip()
            num_questions = int(num_input) if num_input.isdigit() else 10
            
            # Subject selection
            print("\n   Available subjects: mathematics, physics, sat_english")
            subject_input = input("   Enter subjects (comma-separated, or leave empty for all): ").strip()
            subjects = None
            if subject_input:
                subjects = [s.strip() for s in subject_input.split(',')]
            
            # Run adaptive session
            system.run_adaptive_session(num_questions=num_questions, subjects=subjects)
        
        elif choice == '2':
            system.show_student_dashboard()
        
        elif choice == '3':
            system.get_ai_insights()
        
        elif choice == '4':
            print("\n✅ Goodbye! Keep learning and improving!")
            print("   Your progress has been saved. 📝")
            break
        
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
