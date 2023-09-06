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

# Function to encode a phone number
def encode_number(number):
    encoded_number = ""
    for char in number:
        encoded_number += chr(ord(char) + 1)
    return encoded_number

# Function to decode an encoded phone number
def decode_number(encoded_number):
    decoded_number = ""
    for char in encoded_number:
        decoded_number += chr(ord(char) - 1)
    return decoded_number

# Function to load recipients from an encrypted file
def load_recipients(filename):
    recipients = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, encoded_number = line.strip().split(': ')
                number = decode_number(encoded_number)
                recipients[name] = number
        return recipients
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

# Function to save recipients to an encrypted file
def save_recipients(filename, recipients):
    with open(filename, 'w') as file:
        for name, number in recipients.items():
            encoded_number = encode_number(number)
            file.write(f"{name}: {encoded_number}\n")

# Function to send a WhatsApp message
def send_message_to_whatsapp():
    recipients = load_recipients("recipients.txt")

    recipient_name = input("Enter the recipient's name: ")
    message = input("Enter the message you want to send: ")
    scheduled_time = input("Enter the time to send the message (HH:MM): ")

    if recipient_name in recipients:
        recipient_number = recipients[recipient_name]

        try:
            # Parse the scheduled time
            scheduled_hour, scheduled_minute = map(int, scheduled_time.split(':'))

            kit.sendwhatmsg(recipient_number, message, scheduled_hour, scheduled_minute)
            print(f"WhatsApp message scheduled to be sent to {recipient_name} at {scheduled_time}: {message}")
        except Exception as e:
            print(f"An error occurred while scheduling the WhatsApp message: {str(e)}")
    else:
        print(f"Recipient '{recipient_name}' not found in the recipient list.")

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
        
        elif 'add new contact for whatsapp' in main:
            recipient_name = input("Enter the recipient's name: ")
            recipient_number = input("Enter the recipient's phone number (including country code): ")
            recipients = load_recipients("recipients.txt")
            recipients[recipient_name] = recipient_number
            save_recipients("recipients.txt", recipients)
            print(f"Recipient '{recipient_name}' added successfully.")