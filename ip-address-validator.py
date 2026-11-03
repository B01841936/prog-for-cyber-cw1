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
        #try converting each to ints, if it doesnt work tell user
        try:
            number = int(part)
        except ValueError as e:
            print(f"Error with IP, {e}")

        #if each part is 0 or greater than the 8 bit limit (255), invalid ip
        return not (number < 0 or number > 255)

#variable declaration
valid = False

#while invalid ip;
while valid == False:

    #user input
    try:
        address = str(input("Enter IP address >> "))
    except Exception as e:
            print(f"Error with input, {e}")

    #call function to check if valid
    #if no, tell user and continue, otherwise end loop
    if validate_ip(address) == False:
        print("Invalid IP address")
    else:
        break

#tell user result
print("Valid IP address")