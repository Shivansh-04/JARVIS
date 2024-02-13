# All the commented code below work for the voice command just uncomment the code and it will start working in voice and text mode.
# Except re dcomments
import pyttsx3
import datetime
import openai
import wikipedia
from features.login_function import logininfo
import sys
import pyautogui

openai.api_key = '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'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)
engine.setProperty('volume',1.0)
engine.setProperty('pitch', 150)
engine.setProperty('timbre', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("i am Jarvis , please tell how can i help you ? ")

if __name__ == "__main__":
    speak("Enter username ")
    username = input("Enter username: ")
    speak("Enter password ")
    password = input("Enter password: ")
    logininfo(username, password)
    wishMe()

    while True:
    #if 1:
        #query = takeCommand().lower()
        #! logic for executing tasks based on queary
        query=input("enter your command-->")

        if 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(f"Sir, The time is {strTime}")


        #! To search in wikipedia
        elif 'wikipedia' in query:
            speak('Searching wikipedia........')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        #! To open any program/app
        elif 'open' in query:
            app_name = query.replace('open', '')
            speak("opening" + app_name)
            pyautogui.press('super')
            pyautogui.typewrite(app_name)
            pyautogui.sleep(0.7)
            pyautogui.press('enter')

        #! To close the window 
        elif 'close' in query:
            pyautogui.hotkey('alt','f4')
            speak('done sir!')

        #! to close the jarvis program 
        elif 'no thanks' in query:
            speak('thanks for using me sir, have a good day...')
            sys.exit()

        speak("sir, do you have any other work")