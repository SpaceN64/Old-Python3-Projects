# Variables
yes = ["Y", "y", "Yes", "yes"]
no = ["N", "n", "No", "no"]


# Starting Greeting
print("Hello! How are you?")
greeting = input(">>> ")
print("Thats Good!")

# Space
print("")

# Name
print("What is your name?")
name = input(">>> ")
print("So your name is " + name + "?")
choice = input(">>>")
if choice in yes:
    print("")
    print("Ok, I got it right")
else:
    print("")
    print("What is your name?")
    name = input(">>> ")
    print("ok")
