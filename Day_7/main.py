# MAKING A HANGMAN GAME

import random
import hangman_art as art
import hangman_words as words
word_list = words.word_list
stages = art.stages
logo = art.logo
user_lives = 6
has_ended = False

# Print Logo at start
print(logo)

# Use random_index to pick a word from word_list
chosen_word = random.choice(word_list)

print(f"The word is => {chosen_word}")

# Create a list with blanks
display = []
for char in chosen_word:
    display.append("_")


while not has_ended:
    guess = input("Guess a letter:").lower()
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    if guess not in chosen_word:
        print(stages[user_lives - 1])
        user_lives -= 1
        print(f"You guessed {guess}, its not in the word")
        print(display)
        if user_lives == 0:
            has_ended = True
            print("You Loose")
    elif "_" not in display:
        print("You Win")
        has_ended = True
    else:
        print(f"You guessed {guess}, correct")
        print(display)


