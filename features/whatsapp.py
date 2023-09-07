import pywhatkit as kit


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
def send_message_to_whatsapp(recipient_name, message, scheduled_time):
    recipients = load_recipients("recipients.txt")

    # speak("Enter the recipient's name: ")
    # recipient_name = input("Enter the recipient's name: ")
    # # speak("enter the message you want to send: ")
    # message = input("Enter the message you want to send: ")
    # # speak("enter time: ")
    # scheduled_time = input("Enter the time to send the message (HH:MM): ")

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