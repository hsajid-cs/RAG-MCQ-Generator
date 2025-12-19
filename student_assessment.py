"""Student Assessment Module - Interactive MCQ Practice System

This module provides an interactive interface for students to:
- Practice MCQs with immediate feedback
- Track performance metrics
- Get personalized insights
- Build learning profiles over time
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import random


class StudentAssessment:
    """Interactive MCQ assessment system for students."""
    
    def __init__(self, mcq_folder: str = "mcqs", profiles_folder: str = "student_profiles"):
        """Initialize the assessment system.
        
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
        self.all_mcqs: List[Dict[str, Any]] = []
        
    def load_mcqs(self, subjects: Optional[List[str]] = None) -> None:
        """Load MCQs from JSON files.
        
        Args:
            subjects: List of subject names to load (e.g., ['mathematics', 'physics'])
                     If None, loads all available subjects
        """
        self.all_mcqs = []
        mcq_files = list(self.mcq_folder.glob("*.json"))
        
        for mcq_file in mcq_files:
            # Check if this subject should be loaded
            if subjects is not None:
                subject_name = mcq_file.stem.replace('_mcqs', '')
                if subject_name not in subjects:
                    continue
            
            with mcq_file.open('r', encoding='utf-8') as f:
                mcqs = json.load(f)
                # Add metadata
                for mcq in mcqs:
                    mcq['source_file'] = mcq_file.stem
                self.all_mcqs.extend(mcqs)
        
        print(f"Loaded {len(self.all_mcqs)} MCQs")
    
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
            print(f"Welcome back, {student_name}!")
        else:
            self.student_profile = {
                'name': student_name,
                'created_at': datetime.now().isoformat(),
                'sessions': [],
                'total_questions_attempted': 0,
                'total_correct': 0,
                'topic_performance': {},
                'subject_performance': {}
            }
            print(f"Creating new profile for {student_name}")
    
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
        print("\n" + "="*70)
        print(f"Question {question_num}/{total}")
        print("="*70)
        
        # Display subject and topic
        if 'subject' in mcq:
            print(f"Subject: {mcq['subject']}")
        if 'chapter' in mcq:
            print(f"Chapter: {mcq['chapter']}")
        if 'topic' in mcq:
            print(f"Topic: {mcq['topic']}")
        
        # Display passage if exists (for SAT English)
        if 'passage' in mcq and mcq['passage']:
            print(f"\nPassage:")
            print("-" * 70)
            print(mcq['passage'])
            print("-" * 70)
        
        # Display question
        print(f"\nQuestion: {mcq['question']}")
        print()
        
        # Display choices
        choices = mcq.get('choices', [])
        for idx, choice in enumerate(choices):
            label = chr(65 + idx)  # A, B, C, D
            print(f"{label}. {choice}")
    
    def get_student_answer(self) -> str:
        """Get answer from student.
        
        Returns:
            Student's answer (A, B, C, or D)
        """
        while True:
            answer = input("\nYour answer (A/B/C/D) or 'q' to quit: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D', 'Q']:
                return answer
            print("Invalid input. Please enter A, B, C, D, or Q to quit.")
    
    def evaluate_answer(self, mcq: Dict[str, Any], student_answer: str) -> bool:
        """Evaluate student's answer and provide feedback.
        
        Args:
            mcq: MCQ dictionary
            student_answer: Student's answer
            
        Returns:
            True if correct, False otherwise
        """
        correct_answer = mcq.get('answer', '')
        is_correct = (student_answer == correct_answer)
        
        print("\n" + "-"*70)
        if is_correct:
            print("✓ CORRECT!")
        else:
            print(f"✗ INCORRECT. The correct answer is: {correct_answer}")
        
        # Display rationale
        if 'rationale' in mcq:
            print(f"\nExplanation: {mcq['rationale']}")
        
        # Show correct choice text
        choices = mcq.get('choices', [])
        if correct_answer in ['A', 'B', 'C', 'D']:
            choice_idx = ord(correct_answer) - 65
            if 0 <= choice_idx < len(choices):
                print(f"Correct answer: {correct_answer}. {choices[choice_idx]}")
        
        print("-"*70)
        
        return is_correct
    
    def run_practice_session(self, num_questions: int = 10, 
                            subjects: Optional[List[str]] = None,
                            shuffle: bool = True) -> None:
        """Run an interactive practice session.
        
        Args:
            num_questions: Number of questions for this session
            subjects: List of subjects to include (None for all)
            shuffle: Whether to shuffle questions
        """
        # Load MCQs if not already loaded
        if not self.all_mcqs:
            self.load_mcqs(subjects)
        
        if not self.all_mcqs:
            print("No MCQs available. Please generate MCQs first.")
            return
        
        # Select questions
        available_mcqs = self.all_mcqs.copy()
        if shuffle:
            random.shuffle(available_mcqs)
        
        selected_mcqs = available_mcqs[:num_questions]
        
        # Initialize session data
        self.session_data = {
            'start_time': datetime.now().isoformat(),
            'questions': [],
            'correct_count': 0,
            'total_count': len(selected_mcqs),
            'subject_breakdown': {},
            'topic_breakdown': {}
        }
        
        print(f"\n{'='*70}")
        print(f"Starting practice session with {len(selected_mcqs)} questions")
        print(f"{'='*70}")
        
        # Ask each question
        for idx, mcq in enumerate(selected_mcqs, 1):
            start_time = time.time()
            
            self.display_question(mcq, idx, len(selected_mcqs))
            student_answer = self.get_student_answer()
            
            if student_answer == 'Q':
                print("\nSession ended by user.")
                break
            
            end_time = time.time()
            time_taken = end_time - start_time
            
            is_correct = self.evaluate_answer(mcq, student_answer)
            
            # Record question data
            question_data = {
                'question': mcq.get('question', '')[:100] + '...',
                'subject': mcq.get('subject', mcq.get('chapter', 'Unknown')),
                'topic': mcq.get('topic', 'Unknown'),
                'correct_answer': mcq.get('answer', ''),
                'student_answer': student_answer,
                'is_correct': is_correct,
                'time_taken': round(time_taken, 2)
            }
            
            self.session_data['questions'].append(question_data)
            
            if is_correct:
                self.session_data['correct_count'] += 1
            
            # Update breakdowns
            subject = question_data['subject']
            topic = question_data['topic']
            
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
                input("\nPress Enter for next question...")
        
        # End session
        self.session_data['end_time'] = datetime.now().isoformat()
        self.display_session_summary()
        self.update_profile()
        self.save_profile()
    
    def display_session_summary(self) -> None:
        """Display summary of the practice session."""
        print("\n" + "="*70)
        print("SESSION SUMMARY")
        print("="*70)
        
        correct = self.session_data['correct_count']
        total = len(self.session_data['questions'])
        
        if total == 0:
            print("No questions were attempted.")
            return
        
        accuracy = (correct / total) * 100
        
        print(f"\nOverall Performance:")
        print(f"  Correct: {correct}/{total} ({accuracy:.1f}%)")
        
        # Subject breakdown
        if self.session_data['subject_breakdown']:
            print(f"\nPerformance by Subject:")
            for subject, stats in self.session_data['subject_breakdown'].items():
                subj_acc = (stats['correct'] / stats['total']) * 100
                print(f"  {subject}: {stats['correct']}/{stats['total']} ({subj_acc:.1f}%)")
        
        # Topic breakdown
        if self.session_data['topic_breakdown']:
            print(f"\nPerformance by Topic:")
            for topic, stats in sorted(self.session_data['topic_breakdown'].items()):
                topic_acc = (stats['correct'] / stats['total']) * 100
                print(f"  {topic[:50]}: {stats['correct']}/{stats['total']} ({topic_acc:.1f}%)")
        
        # Average time per question
        total_time = sum(q['time_taken'] for q in self.session_data['questions'])
        avg_time = total_time / total if total > 0 else 0
        print(f"\nAverage time per question: {avg_time:.1f} seconds")
        
        print("="*70)
    
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
    
    def show_student_stats(self) -> None:
        """Display comprehensive student statistics."""
        if not self.student_profile:
            print("No profile loaded.")
            return
        
        print("\n" + "="*70)
        print(f"STUDENT PROFILE: {self.student_profile.get('name', 'Unknown')}")
        print("="*70)
        
        total = self.student_profile.get('total_questions_attempted', 0)
        correct = self.student_profile.get('total_correct', 0)
        
        if total == 0:
            print("\nNo practice sessions completed yet.")
            return
        
        accuracy = (correct / total) * 100
        print(f"\nOverall Statistics:")
        print(f"  Total Questions: {total}")
        print(f"  Total Correct: {correct}")
        print(f"  Overall Accuracy: {accuracy:.1f}%")
        print(f"  Sessions Completed: {len(self.student_profile.get('sessions', []))}")
        
        # Subject performance
        print(f"\nPerformance by Subject:")
        for subject, stats in self.student_profile.get('subject_performance', {}).items():
            subj_acc = (stats['correct'] / stats['total']) * 100
            print(f"  {subject}: {stats['correct']}/{stats['total']} ({subj_acc:.1f}%)")
        
        # Top topics
        print(f"\nTop 10 Topics Practiced:")
        topic_perf = self.student_profile.get('topic_performance', {})
        sorted_topics = sorted(topic_perf.items(), key=lambda x: x[1]['total'], reverse=True)[:10]
        for topic, stats in sorted_topics:
            topic_acc = (stats['correct'] / stats['total']) * 100
            print(f"  {topic[:45]}: {stats['correct']}/{stats['total']} ({topic_acc:.1f}%)")
        
        print("="*70)


def main():
    """Main entry point for student assessment."""
    print("="*70)
    print("STUDENT MCQ PRACTICE SYSTEM")
    print("="*70)
    
    # Get student name
    student_name = input("\nEnter your name: ").strip()
    if not student_name:
        print("Name cannot be empty.")
        return
    
    # Initialize assessment
    assessment = StudentAssessment()
    assessment.load_or_create_profile(student_name)
    
    # Main menu
    while True:
        print("\n" + "="*70)
        print("MAIN MENU")
        print("="*70)
        print("1. Start Practice Session")
        print("2. View My Statistics")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            # Configure session
            print("\nSession Configuration:")
            
            # Number of questions
            num_input = input("Number of questions (default 10): ").strip()
            num_questions = int(num_input) if num_input.isdigit() else 10
            
            # Subject selection
            print("\nAvailable subjects: mathematics, physics, sat_english")
            subject_input = input("Enter subjects (comma-separated, or leave empty for all): ").strip()
            subjects = None
            if subject_input:
                subjects = [s.strip() for s in subject_input.split(',')]
            
            # Run session
            assessment.run_practice_session(num_questions=num_questions, subjects=subjects)
        
        elif choice == '2':
            assessment.show_student_stats()
        
        elif choice == '3':
            print("\nGoodbye! Keep practicing!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
