score = 0

import time

ENTER = ["""
"""]

print("""
------------
|  Soccer  |
|  Quiz!   |
------------
""")

time.sleep(2)

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt  = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("""Correct Answer
""")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("""Sorry wrong answer, try again.
>>> """)
            attempt = attempt + 1

    if attempt == 3:
        print("""The correct answer is """ + answer + """
!""")

score = 0
        

guess1 = input("""You get kicked out of the game if you get a red card.\n \
True or False?
>>> """)
check_guess(guess1, "True")

guess2 = input("""How much players from one team are you allowed on the field?
>>> """)
check_guess(guess2, "11")

guess3 = input("""Which is true about soccer:\n \
A) You can kick anyone on the field and you will not get a yellow card\n B) The goalie is able to come out onto the field (Without holding the ball)\n \
(Type A or B)
>>> """)
check_guess(guess3, "B")

guess4 = input("""The Premier League is based out of Canada.\n \
True or False?\n \
>>> """)
check_guess(guess4, "False")

guess5 = input("""When was soccer invented?
>>> """)
check_guess(guess5, "1863")

guess6 = input("""Does Soccer have a maker?\n \
Type Yes or No\n \
>>> """)
check_guess(guess6, "No")

guess7 = input("""And finally,
What is the name of the soccer video game?
>>> """)
check_guess(guess7, "Fifa")

print('Your score is ' + str(score) + ", congrats!")

time.sleep(1.5)

print("""
press ENTER to exit""")

waiting = input()

if waiting in ENTER:
    exit()
else:
    exit()
