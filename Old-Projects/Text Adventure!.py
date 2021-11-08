import time
import os
import sys

print("Loading Game...")
time.sleep(2) # Waits 2 Seconds

print("")

# Variables Python Looks for
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

print(" Text Adventure!")
time.sleep(1) # Waits 1 Second
print("")

print("You walk into a dark cave, then a monster with one eye jumps you!")

time.sleep(0.8) # Waits 0.7 of a Second
print("")

print("You have 2 objects in your bag, a sword and a potion")
time.sleep(0.3) # Waits 0.3 of a Second
print("Which item do you choose?")
print("""A. Use Sword
B. Use Potion""")

print("")

choice = input(">>> ")
if choice in answer_A:
    print("You slayed the Monster with your mighty edge!")
elif choice in answer_B:
    print("You slayed the dragon with the potion!")
    print("You gained 60xp!")
else:
    print("I Don't know how, but you died!")
    time.sleep(1) # Waits 1 Second
    exit()

print("")

print("""You walk more into the cave, looking around to see if anything
else is going to jumpscare you. You walk farther and see light and the end.
You run to that light, but see a figure. The figure is a Man!""")

print("")

print(" He says...")
print('"My name is Aiden! Are you traveller having fun?"')
print("y or n")
print("")
fun = input(">>> ")
if fun in yes:
    print("Well thats nice! Please take some Xp I have!")
    print("")
    print("You gain 20xp!")
else:
    print('"Well to bad. Would you like to continue?"')
    fun = input(">>> ")
    if fun in yes:
        print('"Ok! Resuming the Game..."')
    else:
        print("Quitting...")
        time.sleep(1) # Waits 1 Second
        exit()

print("")

print("As you walk out the cave, the blinding light reaches your eyes. You wipe your eyes and see a big valley with villages spreaded out everywhere!")

print("")

print("You go up to a village, and a person greets you:")

print("")

print('"Hello traveller! What is your name?"')

print("")

name = input(">>> ")

print("")

print("Welcome to chain valley, " + name + "!")

print("")

print("Would you like to know who I am, mister " + name + "?")
guy = input(">>> ")
if guy in yes:
    print("My name is Fedor! I am a village resident here in chop village!")
else:
        print('"I understand! This village is called chop"')

print("")

print('"Would you like some food to eat?"')

print("")

print("""We have
A.Beef
B.Pork
C.suspicious Stew...""")
food = input(">>> ")
if food in answer_A:
    print("The beef tasted well done!")
elif choice in answer_B:
    print("The pork tasted so good! You gained 6xp!")
elif choice in answer_C:
    print("The suspicious stew was not good! You died!")
    print("Exitting...")
    time.sleep(1.5) # Waits 1.5 Seconds
    exit()
else:
    print("Stopping...")
    time.sleep(1.5) # Waits 1.5 Seconds
    exit()

print("")

print('"Now to stay here ' + name + ', you must play a game of rock paper scissors in order to be kept alive or to die!"')

print("")

print('"Give me a moment..."')
time.sleep(1) # Waits 1 Second
print("")

from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("""Rock, Paper, Scissors?
>>> """)
    if player == computer:
        print("Tie!")
        player = False
        computer = t[randint(0,2)]
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print("You died!")
            time.sleep(1) # Waits 1 Second
            exit()
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print("You died!")
            time.sleep(1) # Waits 1 Second
            exit()
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print("You died!")
            time.sleep(1) # Waits 1 Second
            exit()
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        player = False
        computer = t[randint(0,2)]

print('"You beat me! Would you like to stay here, or would you like to continue your journey?"')
print("""A.Stay
B.Continue""")
time.sleep(2) # Waits 2 Seconds

print("")
end = input(">>> ")
if end in answer_A:
    print('"Marvaless! Welcome to the Village!"')
    time.sleep(0.7) # Waits 0.7 of a Second
    print("You live happily ever after in the village, and live a long life!")
    time.sleep(1) # Waits a Second
    exit()
elif choice in answer_B:
        print('"Wonderful! You may continue on with your journey."')

print("")
print("You walk down the valley, looking around at every object. You see something shiny on the ground, you walk up to it. It is a potion!")
print("")

print("You got 1+ Potion!")
print("")

time.sleep(0.8) # Waits 0.8 of a Second
print("As you continue walking down the valley, a monster jumps you!")
print("""You have two items,
A.Sword
B,Weird Potion

What do you choose?""")
Monster = input(">>> ")
if monster in answer_A:
    print("")
    print("You did 10+ Damage!")
elif monster in answer_B:
    print("")
    print("You throw the potion!")
    time.sleep(0.4) # Waits 0.4 of a Second
    print("The potion was a healing potion!")
    time.sleep(0.2) # Waits 0.2 of a Second
    print("You died!")
    print("Exitting...")
    time.sleep(0.5) # Waits Half a Second
    exit()

print("Would you like to use your sword again?")
repeat = input(">>> ")

if yes in repeat:
    print("""Good Choice!

          You slayed the monster!
          """)
elif no in repeat:
    print("""You run away back to the village!
    """)
    print("""You go sleep and get a full rest. When you return, you notice the monsters was gone!
    """)


