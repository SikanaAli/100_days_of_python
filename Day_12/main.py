# day 12 number guessing game
import random
from art import logo

# Print logo
print(logo)

# player prefs
lives = 0
difficaulty = ""


# init
# prints welcome message and asks the user
# to select a dificulty
def init():
    init_msg = f"""
        Welcome to the number guesser
        I'm thinking of a number between 1 and 100
        Pssst, the correct answer is {random.randint(1,100)}
    """
    print(init_msg)

    return input("Choose a dificulty. type 'easy' or 'hard': ").lower()


#def validate_guess(guess):


#def number_guesser():

init()
