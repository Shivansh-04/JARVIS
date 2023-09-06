# All the commented code below work for the voice command just uncomment the code and it will start working in voice and text mode.
# Except re dcomments
import pyttsx3
import pyaudio
import speech_recognition as sr
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

        elif 'russian girl' in main:
            speak("abhi bulaata hu russian ko 6000 me")
            # codePath = "#"
            # os.startfile(codePath)
        

