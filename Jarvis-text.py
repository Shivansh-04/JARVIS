# All the commented code below work for the voice command just uncomment the code and it will start working in voice and text mode.
# Except re dcomments
import pyttsx3
import datetime
import openai
from features.login_function import logininfo
import sys

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
        main=input("enter your command-->")

        if 'tell time' in main:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(f"Sir, The time is {strTime}")

        speak("sir, do you have any other work")