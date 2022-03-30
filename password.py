##program that makes "random" passwords and saves them onto a text file in the computer for quick access
import os
import sys
import secrets
import string

alphabet = string.ascii_letters + string.digits
words = ["Dill", "bEnt", "abet", "freT", "boWl", "fOwl", "mice", "lice", "wood", "read", "lead",
        "back", "sack", "lack", "down", "home", "lock", "caps", "rats", "dogs", "cats", "rack",
        "four", "five", "plus"]

counter = 0
yesno = "2"
print("Welcome to the not really random but random enough password generator!")
print("What is your name? (case sensitive)")
name = input("")


while os.path.isfile((name+".txt")) == False:
    print("It seems like you dont have a password file, would you like to create one or try again?")
    print("1 to create and 2 to try again.")
    input1 = input("")
    if input1 == "1":
        file= open(name+".txt","w+")
    elif input1 == "2":
        print("Please input the right name this time. (CASE SENSITIVE)")
        name = input("")
    else:
        print("ur dumb and dont deserve to use this L")
        ##put in a stupid image here later
        sys.exit()


print("Hi "+ name + "!")
print("Would you like to view your passwords or make a new one?")
print("1 to view passwords and 2 to make new password.")
input2 = input("")
while (input2 != "1" and input2 != "2" ):
    counter = counter + 1
    if (counter == 5):
        print("ur actually trolling")
        sys.exit()
    print("Please input 1 or 2")
    print("1 to view passwords and 2 to make a new password")

if (input2 == "1"):
    with open(name+".txt") as f:
        for line in f:
            print(line)
    sys.exit()
else:
    while (yesno != "1"):
        print("What password is this for? (Password name)")
        pname = input("")
        print(pname + " is the correct name?")
        print("Input 1 to proceed, enter anything else to go back")
        yesno = input("")

while True:
    password = words[secrets.randbelow(len(words))]
    password = password + ''.join(secrets.choice(alphabet) for i in range(8))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 4):
        password = password + words[secrets.randbelow(len(words))]
        break
    
pname = pname + " Password:"
passfile = open(name+".txt", 'a')
passfile.write(pname)
passfile.write(password)
passfile.write("\n")
passfile.close()

