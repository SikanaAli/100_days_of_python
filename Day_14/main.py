# HIGHER OR LOWER GAME

import art
from game_data import data as questions
import random
import os

# assign art vars
game_logo = art.logo
vs_logo = art.vs

# game vars
user_score = 0
compare_a = 0
compare_b = 0

# print logo


# function to clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# get random index in question
def get_index():
    index = random.randint(0, len(questions) - 1)
    return index


# set initial indices
def init_index():
    global compare_a
    global compare_b

    compare_a = get_index()
    compare_b = get_index()

    while compare_a == compare_b:
        compare_b = get_index()


# call init index
init_index()


def get_question(index):
    question = questions[index]
    return f'{question["name"]}, a {question["description"]}, from {question["country"]}'


# set next compare
def set_next_compare_index():
    global compare_a
    global compare_b

    compare_a = compare_b
    compare_b = get_index()
    while compare_a == compare_b:
        compare_b = get_index()


def compute_input_and_score(ans):
    follows_a = questions[compare_a]["follower_count"]
    follows_b = questions[compare_b]["follower_count"]
    global user_score

    if ans == "a"  and follows_a > follows_b:
        user_score += 1
        set_next_compare_index()
        print_next_question()
    elif ans == "b" and follows_b > follows_a:
        user_score += 1
        set_next_compare_index()
        print_next_question()
    else:
        cls()
        print(game_logo)
        print(f"Game Over. Your Score is {user_score}")


# print next comparison
def print_next_question():
    print(game_logo)
    print(f"\n\n******* Score: {user_score} *******\n\n")

    # print Compare_A
    print(f"Compare A: {get_question(compare_a)}. followers {questions[compare_a]['follower_count']}")
    print(vs_logo)
    print(f"Compare B: {get_question(compare_b)}")
    print("\n")
    answer = input("Who has more followers? A or B ").lower()
    cls()
    compute_input_and_score(answer)


print_next_question()

