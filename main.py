#Import the functions from other file
import security_tools

#User Input with error catching
try:
    password = input("Enter Password >> ")
    ipaddress = input("Enter IP >>")
except Exception as e:
        print(f"Error with input, {e}")

#calls validatepassword and send user's chosen password to module
if security_tools.validatepassword(password) == False:
    #If password not secure enough, tell user and suggest a password by calling the random_password module
    print("Suggested Password: ",security_tools.random_password())

#calls validate_ip and send user's ip to module
if security_tools.validate_ip(ipaddress) == False:
    #if ip not valid, tell user
    print("Invalid IP")