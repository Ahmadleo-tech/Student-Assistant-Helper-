import os
import logging
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from pydub import AudioSegment

# Configure logging for debugging and errors
logging.basicConfig(filename="note_taking.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NoteTakingApp:
    def __init__(self):
        """Initialize the Text-to-Speech engine and setup logging"""
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def create_notes(self):
        """Main function for managing notes: add, view, delete, edit, search, record voice"""
        try:
            self.speak("Welcome to the Note-taking Program!")
            print("Welcome to the Note-taking Program!")

            topic = input("Enter the topic for your notes: ")
            filename = topic.replace(" ", "_") + "_notes.txt"
            
            # Check if file exists, if not, create it
            if not os.path.exists(filename):
                with open(filename, "w"):
                    pass

            while True:
                self.show_menu()
                choice = input("Enter your choice (1-7): ")

                if choice == '1':
                    self.add_note(filename)
                elif choice == '2':
                    self.view_notes(filename)
                elif choice == '3':
                    self.delete_note(filename)
                elif choice == '4':
                    self.edit_note(filename)
                elif choice == '5':
                    self.search_notes(filename)
                elif choice == '6':
                    self.record_voice_note(filename)
                elif choice == '7':
                    self.speak("Exiting program. Your notes are saved.")
                    print("Exiting program. Your notes are saved.")
                    break
                else:
                    self.speak("Invalid choice, please try again.")
                    print("Invalid choice, please try again.")
        except Exception as e:
            logging.error(f"Error in create_notes: {str(e)}")
            self.speak("An unexpected error occurred. Please try again later.")
            print("An unexpected error occurred. Please try again later.")

    def show_menu(self):
        """Display the options menu for the user"""
        print("\nChoose an option:")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Delete a note")
        print("4. Edit a note")
        print("5. Search notes")
        print("6. Record a voice note")
        print("7. Exit")
        self.speak("Please choose an option.")

    def add_note(self, filename):
        """Add a new note with a timestamp"""
        try:
            note = input("\nEnter your note: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(filename, "a") as file:
                file.write(f"{timestamp} - {note}\n")

            self.speak("Note added successfully!")
            print("Note added successfully!")
        except Exception as e:
            logging.error(f"Error in add_note: {str(e)}")
            self.speak("Could not add the note. Please try again.")
            print("Could not add the note. Please try again.")

    def view_notes(self, filename):
        """Display all notes saved in the file"""
        try:
            with open(filename, "r") as file:
                notes = file.readlines()

            if not notes:
                self.speak("No notes found.")
                print("No notes found.")
            else:
                print("\nViewing your notes:")
                for index, note in enumerate(notes, start=1):
                    print(f"{index}. {note.strip()}")
        except FileNotFoundError:
            self.speak("No notes found for this topic yet.")
            print("No notes found for this topic yet.")
        except Exception as e:
            logging.error(f"Error in view_notes: {str(e)}")
            self.speak("An error occurred while viewing notes. Please try again.")
            print("An error occurred while viewing notes. Please try again.")

    def delete_note(self, filename):
        """Delete a specific note based on user input"""
        try:
            with open(filename, "r") as file:
                notes = file.readlines()

            if not notes:
                self.speak("No notes available to delete.")
                print("No notes available to delete.")
                return

            print("\nSelect the note to delete:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")

            note_to_delete = int(input("\nEnter the note number to delete: "))

            if 1 <= note_to_delete <= len(notes):
                notes.pop(note_to_delete - 1)
                with open(filename, "w") as file:
                    file.writelines(notes)
                self.speak("Note deleted successfully!")
                print("Note deleted successfully!")
            else:
                self.speak("Invalid note number.")
                print("Invalid note number.")
        except FileNotFoundError:
            self.speak("No notes found for this topic yet.")
            print("No notes found for this topic yet.")
        except Exception as e:
            logging.error(f"Error in delete_note: {str(e)}")
            self.speak("An error occurred while deleting the note. Please try again.")
            print("An error occurred while deleting the note. Please try again.")

    def edit_note(self, filename):
        """Edit an existing note"""
        try:
            with open(filename, "r") as file:
                notes = file.readlines()

            if not notes:
                self.speak("No notes available to edit.")
                print("No notes available to edit.")
                return

            print("\nSelect the note to edit:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")

            note_to_edit = int(input("\nEnter the note number to edit: "))

            if 1 <= note_to_edit <= len(notes):
                new_note = input("Enter the updated note: ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                notes[note_to_edit - 1] = f"{timestamp} - {new_note}\n"
                with open(filename, "w") as file:
                    file.writelines(notes)
                self.speak("Note updated successfully!")
                print("Note updated successfully!")
            else:
                self.speak("Invalid note number.")
                print("Invalid note number.")
        except FileNotFoundError:
            self.speak("No notes found for this topic yet.")
            print("No notes found for this topic yet.")
        except Exception as e:
            logging.error(f"Error in edit_note: {str(e)}")
            self.speak("An error occurred while editing the note. Please try again.")
            print("An error occurred while editing the note. Please try again.")

    def search_notes(self, filename):
        """Search for a keyword in the notes"""
        keyword = input("Enter a keyword to search in your notes: ")

        try:
            with open(filename, "r") as file:
                notes = file.readlines()

            found_notes = [note for note in notes if keyword.lower() in note.lower()]

            if found_notes:
                self.speak("Found notes containing the keyword.")
                print("\nFound notes containing the keyword:")
                for note in found_notes:
                    print(note.strip())
            else:
                self.speak("No notes found with that keyword.")
                print("No notes found with that keyword.")
        except FileNotFoundError:
            self.speak("No notes found for this topic yet.")
            print("No notes found for this topic yet.")
        except Exception as e:
            logging.error(f"Error in search_notes: {str(e)}")
            self.speak("An error occurred while searching the notes. Please try again.")
            print("An error occurred while searching the notes. Please try again.")

    def record_voice_note(self, filename):
        """Record a voice note using the microphone and save it as an MP3"""
        with sr.Microphone() as source:
            self.speak("Please say your note.")
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                note = self.recognizer.recognize_google(audio)
                print(f"You said: {note}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Save the audio as a WAV file
                audio_filename = f"{timestamp}_voice_note.wav"
                with open(audio_filename, "wb") as audio_file:
                    audio_file.write(audio.get_wav_data())

                # Convert WAV to MP3 using pydub
                sound = AudioSegment.from_wav(audio_filename)
                audio_mp3_filename = audio_filename.replace(".wav", ".mp3")
                sound.export(audio_mp3_filename, format="mp3")

                # Add the transcribed note to the file
                with open(filename, "a") as file:
                    file.write(f"{timestamp} - {note} (Audio saved as {audio_mp3_filename})\n")

                self.speak(f"Note added: {note}. Audio saved as {audio_mp3_filename}")
                print(f"Note added: {note}. Audio saved as {audio_mp3_filename}")

            except sr.UnknownValueError:
                self.speak("Sorry, I could not understand your speech.")
                print("Sorry, I could not understand your speech.")
            except sr.RequestError:
                self.speak("Could not request results from the speech recognition service.")
                print("Could not request results from the speech recognition service.")

# Instantiate and run the app
if __name__ == "__main__":
    app = NoteTakingApp()
    app.create_notes()
