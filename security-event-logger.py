#Library Imports
import socket
from datetime import datetime
from random import randint

#pick random number between 1000 and 9999
id = randint(1000,9999)

#get the date and time of this moment
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#get ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
s.close()

#variable declarations
correct = False
username = "admin"
password = "adminpass"

#user inputs with error catching
try:
    usertry = input("Enter Username >> ")
    passtry = input("Enter Password >> ")
except Exception as e:
        print(f"Error with input, {e}")

#while credentials wrong
while(correct == False):
    #tell and ask again, catch errors
    print("Incorrect credentials.")

    #pick successful/failed event type for log, break loop if correct
    if usertry == username and passtry == password:
        event = "Successful Login"
        correct = True
        print(f"ID: {id}\n Username: {usertry}\n IP Address: {ip_address}\n Event: {event}\n Timestamp: {timestamp}")
        break
    else:
        event = "Failed Login"  
    #Print Log entry
    print(f"ID: {id}\n Username: {usertry}\n IP Address: {ip_address}\n Event: {event}\n Timestamp: {timestamp}")
    try:
        usertry = input("Enter Username >> ")
        passtry = input("Enter Password >> ")
    except Exception as e:
        print(f"Error with input, {e}")
