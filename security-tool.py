#Global variable declarations
exit = False
choice = 0

#Main Loop for menu
while(exit==False):
    #Menu options for user
    print("1. Security Event Counter\n2. Brute-Force Simulation\n3. Login Authentication\n4. Exit")

    #Menu choice input from user
    try:
        choice = int(input(">> "))
    except ValueError as e:
        print(f"Error with input: {e}")
    #Input validation
    if (choice < 1 or choice > 4):
        print("Invalid")
        #ask again
        try:
            choice = input(">> ")
        except ValueError as e:
                print(f"Error with input: {e}")

    #Exit choice
    elif choice == 4:
        print("Thank you for using the security tool")
        #ends loop
        exit = True
        break

    #1 - Security Event Counter
    elif choice == 1:
        correct = 0
        false = 0
        password = "password"
        #asks for password 10 times
        for count in range(10):
            #user input
            userpass = input("Enter password >> ")
            #right or wrong?
            if userpass == password:
                correct += 1
                print("Correct")
            else:
                false += 1
                print("False")
        #percentage calculation
        percentage = (false / 10) * 100
        #final results
        if percentage > 50:
            print("Alert! Incorrect password attempts at", percentage,"%")
        else:
            print(percentage,"%")

    #2 - Brute force
    elif choice == 2:
        bruteforcetries = 1
        password = "APre-definedPassword"
        #asks user for input
        userpass = input("Enter password >> ")
        #while its not the set password
        while (userpass != password):
            #tell user
            print(f"Incorrect details. Try No. {bruteforcetries}",)
            #ask again
            userpass = input("Enter password >> ")
            #add 1 to attempt counter
            bruteforcetries += 1
            if userpass == password:
                print(f"Authentication Successful. You brute forced it in {bruteforcetries} attempts.")
                break

    #3 - login auth
    elif choice == 3:
        tries = 1
        #predefined variables, inputs
        user = "user"
        password = "password1"
        if tries != 3:
            username = input("Enter username >> ")
            userpass = input("Enter password >> ")
        #while not correct
        while (userpass != password or username != user):
            #check if too many attempts
            if tries == 3:
                print("Account frozen for 24h")
                break
            #otherwise print fail message.
            else:
                print(f"Incorrect details. Try No. {tries}",)
                #ask again
                username = input("Enter username >> ")
                userpass = input("Enter password >> ")
                #add 1 to attempts
                tries += 1
        #if they get it right, tell
        if username == user and password == userpass:
            print("Authentication Successful")
            