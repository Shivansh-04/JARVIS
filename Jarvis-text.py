# All the commented code below work for the voice command just uncomment the code and it will start working in voice and text mode.
# Except re dcomments
import pyttsx3
import datetime
import openai
import pywhatkit as kit

openai.api_key = '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'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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

def send_message_to_whatsapp():
    recipient_number = input("Enter the recipient's phone number (including country code): ")
    message = input("Enter the message you want to send: ")
    scheduled_time = input("Enter the time to send the message (HH:MM): ")

    try:
        # Parse the scheduled time
        scheduled_hour, scheduled_minute = map(int, scheduled_time.split(':'))

        # Calculate the time difference in minutes
        current_time = datetime.datetime.now()
        scheduled_time = datetime.datetime(current_time.year, current_time.month, current_time.day, scheduled_hour, scheduled_minute)

        time_difference = scheduled_time - current_time
        minutes_until_scheduled_time = time_difference.total_seconds() / 60

        # Check if the scheduled time is in the future
        if minutes_until_scheduled_time < 0:
            print("Scheduled time should be in the future.")
        else:
            kit.sendwhatmsg(f"+{recipient_number}", message, scheduled_hour, scheduled_minute)
            print(f"WhatsApp message scheduled to be sent to {recipient_number} at {scheduled_time}: {message}")
    except Exception as e:
        print(f"An error occurred while scheduling the WhatsApp message: {str(e)}")

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
            send_message_to_whatsapp()
        