score = 0

import time

print("""
------------
|  Animal  |
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
            score = score + 3 - attempt
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("""Sorry wrong answer, try again.
"""))
            attempt = attempt + 1

    if attempt == 3:
        print("""The correct answer is """ + answer + """
!""")

score = 0
        

guess1 = input("""Which bear lives in the North Pole?
>>> """)
check_guess(guess1, "polar bear")

guess2 = input("""What is the fastest land animal?
>>> """)
check_guess(guess2, "cheetah")

guess3 = input("""What is the largest animal?
>>> """)
check_guess(guess3, "blue whale")

guess4 = input("""Which one of these are fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
(Type A, B, C, or D)
""")
check_guess(guess, "C")

guess5 = input("""Mice are mammals.\n \
True or False?
""")
check_guess(guess, "True")

print('Your score is ' + str(score))
