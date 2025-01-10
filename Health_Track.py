import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import logging

# Initialize text-to-speech engine and translator
engine = pyttsx3.init()
translator = Translator()

# Configure logging for debugging and errors
logging.basicConfig(filename="health_track.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def speak_data(data):
    """Convert text to speech"""
    engine.say(data)
    engine.runAndWait()

def search_medical_problem(query):
    """Search for a medical problem on WebMD"""
    search_url = f"https://www.webmd.com/search/search_results/default.aspx?query={query}"
    logging.info(f"Searching for medical solutions for: {query}")
    speak_data(f"Searching for medical solutions for {query}")
    webbrowser.open(search_url)

def voice_search():
    """Perform a voice search for a medical problem"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as micro:
        logging.info("Listening for a medical problem...")
        speak_data("Listening... Please say a medical problem!")
        try:
            audio = recognizer.listen(micro, timeout=10)
            logging.info("Recognizing speech...")
            speak_data("Recognizing...")
            query = recognizer.recognize_google(audio)
            logging.info(f"Voice search query: {query}")
            speak_data(f"You searched for: {query}")
            return query
        except sr.UnknownValueError:
            logging.error("Could not understand the speech.")
            speak_data("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            logging.error(f"Request error: {e}")
            speak_data(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            logging.error("No speech detected.")
            speak_data("You didn't say anything.")
    return None

def main3():
    """Main function to handle medical problem search"""
    choice = input("Choose input method (1: Voice Search, 2: Manual Input): ").strip()
    
    if choice == "1":
        query = voice_search()
    elif choice == "2":
        query = input("Enter the medical problem to search: ").strip()
    else:
        logging.error("Invalid choice. Exiting.")
        speak_data("Invalid choice. Exiting.")
        return

    if query:
        lang_choice = input("Do you want to translate your query? (yes/no): ").strip().lower()
        if lang_choice == "yes":
            target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()
            translated_query = translate_query(query, target_lang)
            search_medical_problem(translated_query)
        else:
            search_medical_problem(query)

def translate_query(query, target_lang):
    """Translate the query to the target language"""
    try:
        translated = translator.translate(query, dest=target_lang)
        logging.info(f"Translated Query: {translated.text} (Language: {target_lang})")
        speak_data(f"Translated your query to {target_lang}.")
        return translated.text
    except Exception as e:
        logging.error(f"Translation failed: {e}")
        speak_data("Sorry, translation failed.")
        return query  # Use the original query if translation fails

if __name__ == "__main__":
    main3()