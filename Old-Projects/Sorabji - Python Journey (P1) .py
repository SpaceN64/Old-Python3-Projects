print("Loading Program")
import time
time.sleep(1) # Waits 1 Second

Munson = ["Munson", "munson", "Mr. Munson", "mr. munson", "mr munson", "Mr Munson"]
yes = ["Y", "y", "Yes", "yes"]
no = ["N", "n", "No", "no"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

print("""
Now Starting...
""")

time.sleep(1)

print("""
------------------
|      Text      |
|   Adventure!   |
------------------
""")

time.sleep(0.9) # Waits 0.9 of a Second

print("What is your name traveller?")
name = input(">>> ")

if name in Munson:
    print("""
Hello Mr. Munson!
""")
    print("\t\nStarting game...\n\t")
else:
    print("""
Welcome, """ + name + """! Starting the game...
""")

time.sleep(1) # Waits 1 Second

print("""
-------------------------------------------------------------------------------
    You, """ + name + """ Start you journey off in a tiny village. You walk out of
the house excited because today is the day you start you journey to fight monsters!
""")
time.sleep(0.8)

print("""
    You finally are at the exit to get out of town. You take a big breath and go
into the cave. The cave was dark, but luckly you had a torch with you.
    """)
time.sleep(0.8)

print("""

As you walk, you hear footsteps ahead, It's a monster!
        """)

time.sleep(0.7)

print("""

You have two items in your bag, a stick, and a potion.

What do you choose?
A.Stick
B.Potion
    """)
CaveM = input(">>> ")

if CaveM in answer_A:
    print("""
You hit the monster with you stick!

It does 50+ Damage!
""")
    time.sleep(0.9)
    print("""Would you like to hit again or throw a potion?
A.Stick
B.Potion
""")
    again = input(">>> ")
    if again in answer_A:
        print("""You hit the monster!

The stick does 50+ Damage!

You slayed the monster!
""")
    elif again in answer_B:
        print("""You throwed the potion to the monster!

Critical Hit!

You killed the monster!
""")
    else:
        print("That's not a valid command!")
        exit()
elif CaveM in answer_B:
    print("""
You throwed the potion to the monster!

Critical Hit!
Your potionn did 100+ Damage and killed the monster!
""")
else:
    print("That's not a valid command!")
    exit()

time.sleep(4)
print("""   After you slayed the monster, you continue walking through the cave
until you see a bright light! You run towards the light, wating for it to gleem
onto your eyes.

And then, you see...
""")

time.sleep(6)
print("""Thank you for playing the demo of this game, """ + name + """!
""")

time.sleep(3)

print("Exitting...")
time.sleep(3)
exit()

