import os
import random
import difflib
import csv
import logging

# Configure logging for debugging and errors
logging.basicConfig(filename="quiz_application.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class QuizApp:
    def __init__(self):
        """Initialize the application"""
        self.notes_dir = "notes"  # Directory to store topic-based notes
        self.quiz_score = 0
        self.total_questions = 0
        self.report_file = "quiz_report.csv"  # File to save quiz results

    def search_notes(self, topic):
        """Search for notes related to the given topic"""
        notes = []
        topic_filename = topic.replace(" ", "_").lower() + "_notes.txt"
        filepath = os.path.join(self.notes_dir, topic_filename)

        try:
            if os.path.exists(filepath):
                with open(filepath, "r") as file:
                    notes = file.readlines()
                if not notes:
                    self._notify_user(f"No notes found for the topic: {topic}")
            else:
                self._notify_user(f"Notes for {topic} do not exist in the notes directory.")
        except Exception as e:
            logging.error(f"Error in search_notes: {str(e)}")
            self._notify_user("An error occurred while searching for notes. Please try again later.")
        
        return notes

    def generate_quiz(self, notes):
        """Generate quiz questions based on the notes"""
        questions = []
        self.total_questions = len(notes)

        for note in notes:
            note_parts = note.split(" - ")  # Assuming the notes are in 'timestamp - note' format
            if len(note_parts) > 1:
                question = note_parts[1].strip()
                answer = note_parts[1].strip()  # Simplified, this can be extended to complex quizzes
                questions.append((question, answer))

        return questions

    def evaluate_answers(self, user_answers, questions):
        """Evaluate the user's answers and calculate the score"""
        self.quiz_score = 0
        for idx, (question, correct_answer) in enumerate(questions):
            if idx < len(user_answers) and self.check_plagiarism(user_answers[idx], correct_answer):
                self.quiz_score += 1
            else:
                self._notify_user(f"Q{idx + 1}: Incorrect!")
        
        self._notify_user(f"Your final score: {self.quiz_score}/{self.total_questions}")
        
        # Save the results to the report
        self.save_report(user_answers)

    def check_plagiarism(self, user_answer, correct_answer):
        """Check for plagiarism by comparing answers"""
        similarity = difflib.SequenceMatcher(None, user_answer.lower(), correct_answer.lower()).ratio()
        plagiarism_threshold = 0.8  # 80% similarity
        if similarity > plagiarism_threshold:
            self._notify_user("Plagiarism detected! Your answer is too similar to the correct answer.")
            return False
        return True

    def save_report(self, user_answers):
        """Save the marks report to a CSV file"""
        topic = input("Enter the topic for your quiz: ")
        report_data = {
            "Topic": topic,
            "Total Questions": self.total_questions,
            "Score": self.quiz_score,
            "User Answers": ", ".join(user_answers),
        }

        # Check if report file exists, if not create a new one with headers
        file_exists = os.path.exists(self.report_file)
        with open(self.report_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=report_data.keys())

            if not file_exists:
                writer.writeheader()  # Write header only once
            writer.writerow(report_data)

        self._notify_user(f"Your quiz results have been saved to {self.report_file}.")

    def take_quiz(self, topic):
        """Take the quiz for a given topic"""
        self._notify_user(f"\nWelcome to the {topic} quiz!")

        notes = self.search_notes(topic)
        if notes:
            questions = self.generate_quiz(notes)
            user_answers = []

            for idx, (question, _) in enumerate(questions):
                print(f"Q{idx + 1}: {question}")
                user_answer = input("Your answer: ").strip()
                user_answers.append(user_answer)

            self.evaluate_answers(user_answers, questions)

    def _notify_user(self, message):
        """Notify the user with a message"""
        print(message)
        self.speak(message)

    def speak(self, text):
        """Convert text to speech (for voice output)"""
        # Placeholder for text-to-speech functionality, can be integrated with pyttsx3 or other libraries
        print(text)

def main4():
    app = QuizApp()
    topic = input("Enter the topic for your quiz: ")
    app.take_quiz(topic)

# Main function to start the quiz
if __name__ == "__main__":
    main4()