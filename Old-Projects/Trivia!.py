print("Before we start the game, what is your name?")
name = input(">>> ")

# Importing wait Command
import time
time.sleep(1)

yes = ["Y", "y", "Yes", "yes"]
no = ["N", "n", "No", "no"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
t = ["True", "true", "T", "t"]
f = ["False", "false", "F", "f"]

print("Ok, starting the game...")
time.sleep(0.9)

print("""
-------------------
|     Trivia      |
|    Questions    |
-------------------
""")

time.sleep(1.28)

print("""Here's how to play:

A question will pop on the shell and you have to answer it with A or B (Simple!).

Ex. What came first, the chicken or the egg?

    If you wanted to choose chicken, you would type A. iF you wanted to choose the
egg, type B.
""")

time.sleep(3)

print("Do you understand?")
rules = input(">>> ")

if rules in yes:
    print("""Ok! Starting the game (Again)...
""")
elif rules in no:
    print("Well to bad.")
else:
    print("That's not a valid command!")
    exit()

time.sleep(1)
print("""
-----------------------------------------------------------------------------
1. Who teaches coding in SMS?
A.Munson
B.Scherick
""")
coding = input(">>> ")

if coding in answer_A:
    print("""
Good job!
You got it right!
""")
elif coding in answer_B:
    print("""
Im sorry, that is not correct!
""")
else:
    print("""
That's not a valid command!
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
2. What coding language is this game running?
A.Java (Short-term)
B.Python
""")
language = input(">>> ")

if language in answer_A:
    print("""
Oops! You go this question wrong!
""")
elif language in answer_B:
    print("""
Good job!
You got this question right!
""")
else:
    print("""
That's not a valid command!
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
3. Who made the "iPhone"?
A.Android
B.Apple
""")
apple = input(">>> ")

if apple in answer_A:
    print("""
Oooo, So close!
""")
elif apple in answer_B:
    print("""
You got it! Wow you are smart...
""")
else:
    print("""
That is not a valid command!
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
4. Is Python a open souce program?
Y or N
""")
Open = input(">>> ")

if Open in yes:
    print("""
You are correct!

    Python is an open source program for coding so people are able to add and
make their own versions of the code!
""")
elif Open in no:
    print("""
Sadly, you are wrong!

    Python is an open source program for coding so people are able to add and
make their own versions of the code!
""")
else:
    print("""
That is not a Valid Command!
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
5. What OS's are PC's able to run?
A.Windows (Microsoft)
B.MacOs (Apple)
C.Linux (Open Source)
D.All of the Above
""")
OS = input(">>> ")

if OS in answer_A:
    print("""
You are correct and uncorrect at the same time!
""")
elif OS in answer_B:
    print("""
You are correct and uncorrect at the same time!
""")
elif OS in answer_C:
    print("""
You are correct and uncorrect at the same time!
""")
elif OS in answer_D:
    print("""
You are correct!

    You probably know that PC's can run linux and windows, but did you know
that PC's can also run MacOS?

    The process of getting MacOs on your PC is tedius, but once you finished it,
its rewarding! Getting MacOs on your PC is called "Hackintosh".
""")
else:
    print("""
That's not a valid command!
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
6. You can run windows on your Mac
T or F
""")
Mac = input(">>> ")

if Mac in t:
    print("""
You are correct!
""")
elif Mac in f:
    print("""
Oooo, I'm afraid that is not the right answer...
""")
else:
    print("""
That's not a valid command! (you should have learned now lol)
""")

time.sleep(1)
print("""
-----------------------------------------------------------------------------
7. Who plays as Pikichu in "Detective Pikachu"?
A.Ryan Renolds
B.Dany Divito
C.Jack Massey Welsh
""")
DP = input(">>> ")

if DP in answer_A:
    print("""
You are correct!
""")
elif DP in answer_B:
    print("""
I mean, Ill give it to you..
""")
elif DP in answer_C:
    print("""
SUPSCRIBE TO DONT SUBSCRIBE

https://www.youtube.com/channel/UC68DIXWCmetC8N5J_Kc5gjQ
""")
else:
    print("""
That is not a valid command! (really, the commands are t & f, a, b, c, d, y & n)
""")
