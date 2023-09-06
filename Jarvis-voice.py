import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import sys
import PyPDF2
import math as operator

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
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        #!logic for executing tasks based on queary
        
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

        #!physics file open karne ke lia
        elif 'physics' in query:
            speak('opening physics sir')
            codePath = "D:\PCM\PHYSICS"
            os.startfile(codePath)

        #!chemistry file open karne ke lia
        elif 'open chemistry' in query:
            speak('opening chemistry sir')
            codePath = "D:\PCM\CHEMISTRY"
            os.startfile(codePath)

        #!math file open karne ke lia
        elif 'open math' in query:
            speak('opening maths sir')
            codePath = "D:\PCM\MATHS"
            os.startfile(codePath)

        #!python open karne ke lia
        elif 'open python' in query:
            speak('opening python sir')
            codePath = "C:\Program Files\PyScripter\PyScripter.exe"
            os.startfile(codePath)

        #!ms excel open karne ke lia
        elif 'open excel' in query:
            speak('opening excel sir')
            codePath = "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(codePath)

        #!drama file open karne ke lia
        elif 'open drama' in query:
            speak('opening dramas sir')
            codePath = "D:\DRAMA"
            os.startfile(codePath)

        #!whatsapp me message send karne ke lia
        elif 'send message in whatsapp' in query:
            speak('Sir, what can i send on whatsapp')
            command2 = takeCommand().lower()
            kit.sendwhatmsg("+919140470224",command2,21,54)

        #!youtube se video open karne ke lia
        elif 'play songs on youtube' in query:
            kit.playonyt("see you again")

        speak("sir, do you have any other work")