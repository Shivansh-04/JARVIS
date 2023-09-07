# All the commented code below work for the voice command just uncomment the code and it will start working in voice and text mode.
# Except re dcomments
import pyttsx3
import datetime
import openai
from features import whatsapp

openai.api_key = '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'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


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

        elif 'send message on WhatsApp' in main:
            speak("Enter the recipient's name: ")
            recipient_name = input("Enter the recipient's name: ")
            speak("enter the message you want to send: ")
            message = input("Enter the message you want to send: ")
            speak("enter time: ")
            scheduled_time = input("Enter the time to send the message (HH:MM): ")
            whatsapp.send_message_to_whatsapp(recipient_name, message, scheduled_time)
        
        elif 'add new contact for whatsapp' in main:
            recipient_name = input("Enter the recipient's name: ")
            recipient_number = input("Enter the recipient's phone number (including country code): ")
            recipients = whatsapp.load_recipients("recipients.txt")
            recipients[recipient_name] = recipient_number
            whatsapp.save_recipients("recipients.txt", recipients)
            print(f"Recipient '{recipient_name}' added successfully.")