
# ------------------------
# | *\Made by SpaceN64*/ |
# ------------------------


# Imports
from random import choice
import random
import time

# Funny Messages + Exit Code
greeting = choice(["Alright, give me you password.", "Let's Make this quick.", "Hurry up and type your password.", "I don't have all day..."])
judge = ["You really think this is a good password?", "My Grandma could do better!", "Well this password is complete garbage.", "Who would want to use this password?", "Why would anyone use this password?", "Wow, this is a horrible Password", "You could do better", "I mean... its not bad, but its not good either."] 
leave = ["Exit", "exit", "Exit()", "exit()", "Leave", "leave", "Leave()", "leave()"]

print(greeting)

# Repeating
while True:
    print("")
    password = input(">>> ")
    print("")
    pas = random.choice(judge)
    print(pas)

