import os
import fnmatch
import webbrowser
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import logging
import time

# Initialize text-to-speech engine and translator
engine = pyttsx3.init()
translator = Translator()

# Configure logging for debugging and errors
logging.basicConfig(filename="search_engine.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def speak_data(data):
    """Convert text to speech"""
    engine.say(data)
    engine.runAndWait()

def search_files_on_pc(query, root_dir=None):
    """Search for files on the PC matching the query"""
    if not root_dir:
        root_dir = os.path.expanduser("~")  # Default to user’s home directory
    matched_files = []
    speak_data(f"Searching for files matching {query} on your computer.")
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if fnmatch.fnmatch(file, f"*{query}*"):
                matched_files.append(os.path.join(root, file))
    return matched_files

def display_found_files(matched_files):
    """Display and open found files"""
    if matched_files:
        print(f"Found {len(matched_files)} file(s):")
        for idx, file in enumerate(matched_files, 1):
            print(f"{idx}: {file}")
        speak_data(f"Found {len(matched_files)} files. Please check the list.")
        
        open_choice = input("Do you want to open a file? (yes/no): ").strip().lower()
        if open_choice == "yes":
            try:
                file_idx = int(input("Enter the file number to open: ")) - 1
                os.startfile(matched_files[file_idx])
                speak_data("Opening the file.")
            except (IndexError, ValueError):
                print("Invalid choice. Exiting.")
                speak_data("Invalid choice. Exiting.")
    else:
        print("No matching files found.")
        speak_data("No matching files found.")

def voice_search():
    """Perform a voice search"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as micro:
        print("Listening... Please say something!")
        speak_data("Listening... Please say something!")
        try:
            audio = recognizer.listen(micro, timeout=10)
            print("Recognizing...") 
            speak_data("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You searched for: {query}")
            speak_data(f"You searched for: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
            speak_data("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak_data(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            print("You didn't say anything.")
            speak_data("You didn't say anything.")
    return None

def manage_todo_list():
    """Manage the student's to-do list"""
    todo_file = "todo_list.txt"
    if not os.path.exists(todo_file):
        open(todo_file, 'w').close()  # Create a new file if it doesn't exist

    while True:
        print("\nTo-Do List Options:")
        print("1: View To-Do List")
        print("2: Add a Task")
        print("3: Remove a Task")
        print("4: Exit To-Do List Management")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\nYour To-Do List:")
            with open(todo_file, 'r') as file:
                tasks = file.readlines()
                if tasks:
                    for idx, task in enumerate(tasks, 1):
                        print(f"{idx}: {task.strip()}")
                else:
                    print("Your to-do list is empty.")
        elif choice == "2":
            task = input("Enter the task you want to add: ").strip()
            with open(todo_file, 'a') as file:
                file.write(f"{task}\n")
            speak_data(f"Task '{task}' added to your to-do list.")
        elif choice == "3":
            with open(todo_file, 'r') as file:
                tasks = file.readlines()
            print("\nSelect a task to remove:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}: {task.strip()}")
            try:
                task_idx = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_idx < len(tasks):
                    del tasks[task_idx]
                    with open(todo_file, 'w') as file:
                        file.writelines(tasks)
                    speak_data(f"Task {task_idx + 1} removed from your to-do list.")
                else:
                    speak_data("Invalid task number. No task removed.")
            except (IndexError, ValueError):
                speak_data("Invalid task number. No task removed.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
            speak_data("Invalid choice. Try again.")

def start_study_timer():
    """Start a study timer with the Pomodoro technique"""
    study_time = 25 * 60  # Default to 25 minutes (Pomodoro technique)
    break_time = 5 * 60  # Default break time (5 minutes)

    print("Study Timer: Starting your study session for 25 minutes.")
    speak_data("Starting your study session for 25 minutes.")
    time.sleep(study_time)  # Study session time

    print("Study session complete! Take a 5-minute break.")
    speak_data("Study session complete! Take a 5-minute break.")
    time.sleep(break_time)  # Break time

    print("Break time over! Start a new study session.")
    speak_data("Break time over! Start a new study session.")

def search_engine(query, language=None):
    """Perform an internet search using the specified search engine"""
    if language:
        query = translate_query(query, language)

    print("Select Search Engine:")
    print("1: Google")
    print("2: Bing")
    engine_choice = input("Enter the search engine number: ").strip()

    search_engine = "google" if engine_choice == "1" else "bing" if engine_choice == "2" else None
    if not search_engine:
        print("Invalid choice. Exiting.")
        speak_data("Invalid choice. Exiting.")
        return

    print(f"Choose a feature for {search_engine.capitalize()}:")
    print("1: Search")
    print("2: Maps")
    print("3: Videos")
    print("4: Images")
    feature_choice = input("Enter the feature number: ").strip()

    if query:
        open_search_feature(query, feature_choice, search_engine)
    else:
        print("No query provided. Exiting search.")
        speak_data("No query provided. Exiting search.")

def open_search_feature(query, feature_choice, search_engine):
    """Open the selected search feature"""
    if feature_choice == "1":  # Search
        if search_engine == "google":
            webbrowser.open(f"https://www.google.com/search?q={query}&safesearch=active")
        elif search_engine == "bing":
            webbrowser.open(f"https://www.bing.com/search?q={query}&safesearch=active")
    elif feature_choice == "2":  # Maps
        if search_engine == "google":
            webbrowser.open(f"https://www.google.com/maps/search/{query}&safesearch=active")
        elif search_engine == "bing":
            webbrowser.open(f"https://www.bing.com/maps?q={query}&safesearch=active")
    elif feature_choice == "3":  # Videos
        if search_engine == "google":
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}&safesearch=active")
        elif search_engine == "bing":
            webbrowser.open(f"https://www.bing.com/videos/search?q={query}&safesearch=active")
    elif feature_choice == "4":  # Images
        if search_engine == "google":
            webbrowser.open(f"https://www.google.com/search?hl=en&tbm=isch&q={query}&safesearch=active")
        elif search_engine == "bing":
            webbrowser.open(f"https://www.bing.com/images/search?q={query}&safesearch=active")
    else:
        print("Invalid choice. Exiting.")
        speak_data("Invalid choice. Exiting.")

def main_search(query):
    """Main search function to select the search type"""
    print("Select Search Type:")
    print("1: Internet Search")
    print("2: PC File Search")
    print("3: Manage To-Do List")
    print("4: Start Study Timer")
    search_type = input("Enter the search type number: ").strip()

    if search_type == "1":
        search_engine(query)
    elif search_type == "2":
        matched_files = search_files_on_pc(query)
        display_found_files(matched_files)
    elif search_type == "3":
        manage_todo_list()
    elif search_type == "4":
        start_study_timer()
    else:
        print("Invalid search type. Exiting.")
        speak_data("Invalid search type. Exiting.")

def translate_query(query, target_lang):
    """Translate the query to the target language"""
    try:
        translated = translator.translate(query, dest=target_lang)
        print(f"Translated Query: {translated.text} (Language: {target_lang})")
        speak_data(f"Translated your query to {target_lang}.")
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        speak_data("Sorry, translation failed.")
        return query  # Use the original query if translation fails

def main2():
    """Main function to handle search input and processing"""
    choice = input("Choose input method (1: Voice Search, 2: Manual Input): ").strip()
    if choice == "1":
        query = voice_search()
    elif choice == "2":
        query = input("Enter data to search: ").strip()
    else:
        print("Invalid choice. Exiting.")
        speak_data("Invalid choice. Exiting.")
        query = None

    if query:
        lang_choice = input("Do you want to translate your query? (yes/no): ").strip().lower()
        if lang_choice == "yes":
            target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()
            query = translate_query(query, target_lang)

        main_search(query)

if __name__ == "__main__":
    main2()