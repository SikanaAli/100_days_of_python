# day 12 number guessing game
import random
from art import logo

# Print logo
print(logo)

# player prefs
lives = 0

# Game Prefs
guess_is_correct = False

# init
# prints welcome message and asks the user
# to select a difficulty
def init():
    init_msg = f"""
        Welcome to the number guesser
        I'm thinking of a number between 1 and 100
        Pssst, the correct answer is {random.randint(1,100)}
    """
    print(init_msg)

    return input("Choose a difficulty. type 'easy' or 'hard': ").lower()


def validate_guess(player_guess, correct_guess):
    global guess_is_correct
    global lives
    if player_guess > correct_guess:
        print("Too High.\nGuess Again.")
        lives -= 1
    elif player_guess < correct_guess:
        print("Too Low.\nGuess Again.")
        lives -= 1
    elif player_guess == correct_guess:
        print(f"You win, the correct guess was {correct_guess}")
        guess_is_correct = True

    if lives < 1:
        print(f"Attempts {lives}, you are out of attempts, You Loose")
        guess_is_correct = True


difficulty = init()


def set_lives():
    global lives
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5


set_lives()


def number_guesser():

    # randomly generated number
    correct_number = random.randint(1, 100)

    while not guess_is_correct:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        validate_guess(guess, correct_number)


number_guesser()
