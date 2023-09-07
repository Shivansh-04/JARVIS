import sys

def logininfo(username, password):
    if username == 'root' and password == 'itsdev04':
        print(f"Welcome, {username}!")
    else:
        print("Incorrect username or password.")
        sys.exit("Program terminated due to failed login.")
