# HIGER OR LOWER GAME

import art
from game_data import data as questions
import random
import os

# assign art vars
game_logo = art.logo
vs_logo = art.vs

#game vars
user_score = 0
compare_a = 0
compare_b = 0

# print logo


# function to clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


#get random index in quesstion
def get_index():
    index = random.randint(0, len(questions) - 1)
    return index

#set initial indices
def init_index():
    global compare_a
    global compare_a

    compare_a = get_index()
    compare_b = get_index()

    
    while compare_a == compare_b:
        compare_b = get_index()



#call init index
init_index()


def get_question(index):
    question = questions[index]
    return(f'{question["name"]}, a {question["description"]}, from {question["country"]}')


def compute_input_and_score(ans):
    follows_a = questions[compare_a]["follower_count"]
    follows_b = questions[compare_b]["follower_count"]
    global user_score

    if ans == "a":
        if follows_a > follows_b:
            user_score += 1
    elif ans == "b":
        if follows_b > follows_a:
            user_score += 1


#next comparison
def print_next_quesstion():
    print(game_logo)
    print(f"\n\n******* Score: {user_score} *******\n\n")
    
    print(f"A => {compare_a} | B => {compare_b}")
    #print Comapre_A
    print(f"Compare A: {get_question(compare_a)}")
    print(vs_logo)
    print(f"Compare B: {get_question(compare_b)}")
    print("\n")
    answer = input("Who has more followers? A or B ").lower()
    compute_input_and_score(answer)
    cls()
    print_next_quesstion()

print_next_quesstion()

