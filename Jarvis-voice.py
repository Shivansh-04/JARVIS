import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import sys
from features.login_function import logininfo
import pyautogui

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
    speak("i am nexus sir, please tell how can i help you ? ")

def takeCommand():
    #it take microphone input from the user and return string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.......")
        return "None"
    return query

if __name__ == "__main__":
    speak("Enter username ")
    username = input("Enter username: ")
    speak("Enter password ")
    password = input("Enter password: ")
    logininfo(username, password)
    wishMe()
    while True:
    #if 1:
        #!logic for executing tasks based on queary
        query = takeCommand().lower()
        
        #!to search anything on wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia........')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        #!youtube open karne ke lia
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        #!google open karne ke lia
        elif 'open google' in query:
            speak('Sir, what can i search on google')
            command1 = takeCommand().lower()
            webbrowser.open("google.com")

        #!time batane ke lia
        elif 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        #!vs code open karne ke lia
        elif 'open code' in query:
            speak('opening vs code sir')
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        #!vs code close karne ke lia
        elif "close code" in query:
            speak("okey sir, closing code")
            os.system("taskkill /f /im code.exe")

        #!program close karne ke lia
        elif 'no thanks' in query:
            speak('thanks for using me sir, have a good day...')
            sys.exit()

        #!python open karne ke lia
        elif 'open python' in query:
            speak('opening python sir')
            codePath = "C:\Program Files\PyScripter\PyScripter.exe"
            os.startfile(codePath)

        #! more things to do here


        speak("sir, do you have any other work")