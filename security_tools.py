#Import Libraries
import random
import string


#declare validate password module with userpassword parameter
def validatepassword(userpassword):

    #declare variables
    uppercase = 0
    lowercase = 0
    number = 0
    symbol = 0
    space = 0

    #loops through each character and checks if is uppercase, lowercase, a number, symbol, space and counts them
    for char in userpassword:
        #check if any uppercase
        if char.isupper():
            uppercase = uppercase + 1

        #check if any lowercase
        elif char.islower():
            lowercase = lowercase + 1

        #check if any numbers
        elif char.isdigit():
            number = number + 1

        #check if any spaces
        elif char.isspace():
            space = space + 1

        #check if any accepted symbols
        elif char == "!" or char == "@" or char == "#" or char == "$" or char == "%":
            symbol = symbol + 1

        #if longer than 10 characters, has at least 1 uppercase and lowercase character with 2 numbers no spaces and an accepted symbol, send back the good words
    if len(userpassword) >= 10 and uppercase >= 1 and lowercase >= 1 and number >= 2 and space == 0 and symbol >= 1:
        ispolicy = True
        return  ispolicy
    else:
        #otherwise its not compliant
        ispolicy = False
        return ispolicy

#Declare functions with 'address' as a parameter
def validate_ip(address):

    #remove white space
    address.strip()

    #if no dots in XYZ.XYZ.XYZ.XYZ not an ip or if theres dots, but less than 3, its not an ip either
    if ("." not in address or address.count(".") != 3):
        return False
    
    #split each set of numbers by the dots
    parts = address.split(".")

    #if not 4 parts, invalid ip
    if len(parts) != 4:
        return False
    
    #if theres letters and numbers in your ipv4, its not an ipv4
    for part in parts:
        if not part.isdigit():
            return False
        try:
            number = int(part)
        except ValueError as e:
            return False
        #if each part is 0 or greater than the 8 bit limit (255), invalid ip
        return not (number < 0 or number > 255)

#Declare random_password module
def random_password():

    #declare variables
    password = ""

    #select random length between 10 and 16 characters
    length = random.randint(10,16)

    #make a list of all ascii letters
    lett = list(string.ascii_letters)

    #make a list of all ascii numbers
    num = list(string.digits)

    #make a list of all ascii symbols
    sym = list(string.punctuation)

    #shuffles list of letters,numbers and symbols
    random.shuffle(lett)
    random.shuffle(num)
    random.shuffle(sym)

    #index set to 0
    i = 0

    #loop through length - 1 to account for the starting pos of 0
    for i in range(length-1):
        #pick if its a letter number of symbol
        char = random.randint(1,3)

        #if a letter, add a letter on
        if char == 1:
            password += lett[i]

        #if a number, add a number on
        elif char== 2:
            r = random.randint(0,9)
            password += num[r]

        #if a symbol, add a symbol on
        elif char == 3:
            password += sym[i]
            
    #send back the random password
    return password