# DAY 4 PROJECT 
# CREATING A ROCK, PAPER, SCISSORS GAME
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]  # Place options in a list

user_choice = int(input("Whats your choice 1 for ROCK, 2 for PAPER, 3 for SCISSORS")) - 1  # PRompt user for input
computer_choice = random.randint(0,2)  # random index for computer selection


# first if state user win conditions
# second elif stats draw condition
# all other condition are user loose conditions handled by else

if ((user_choice == 0) and (computer_choice == 2)) or ((user_choice == 1) and (computer_choice == 0)) or ((user_choice == 2) and (computer_choice == 1)):
    print("You Choose :\n\n")
    print(options[user_choice])
    print("\n\nComputer Choose :\n\n")
    print(options[computer_choice])
    print("\n\n YOU WIN")

elif (user_choice == computer_choice):
    print("You Choose :\n\n")
    print(options[user_choice])
    print("\n\nComputer Choose :\n\n")
    print(options[computer_choice])
    print("\n\n IT'S A DRAW")
    
else:
    print("You Choose :\n\n")
    print(options[user_choice])
    print("\n\nComputer Choose :\n\n")
    print(options[computer_choice])
    print("\n\n YOU LOSE")
