import speech_recognition as sr
import webbrowser
import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")
            elif "open notepad" in command:
                os.system("notepad")
                speak("Opening Notepad")
            elif "open library" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Library")
            elif "exit" in command:
                print("Exiting the program...")
                speak("Exiting the program")
                break
            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to Google's servers.")

if __name__ == "__main__":
    main()
