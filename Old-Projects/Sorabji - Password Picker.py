import time
import random
import string

adjectives = ["sleepy", "slow", "smelly", "wet", "fat", "red", "orange", "yellow", "green",
       "blue", "purple", "fluffy", "white", "proud", "brave"]

nouns = ["apple", "dinosaur", "ball", "ball", "hammer", "duck", "panda"]

consoles = ["gamecube", "wii", "switch", "n64", "xbox", "ps", "dreamcast"]

games = ["minecraft", "cod", "smb", "ssbu", "ssf2"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("""Welcome to Password Picker!
""")


while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    console = random.choice(consoles)
    game = random.choice(games)
    letter = random.choice(letters)

    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char + letter
    password2 = adjective + game + str(number) + special_char + console
    
    rep = input("""Would you like one with an adjective, game, number, character, and a console?\n \
(Y or N)\n \

>>> """)
    if rep == 'n':
        print("Your new password is: %s" % password)
    elif rep == 'y':
        print("Your new password is: %s" % password2)

    response = input("""
Would you like another password?\n \
(Y or N)\n \

>>> """)
    if response == 'n':
        break
