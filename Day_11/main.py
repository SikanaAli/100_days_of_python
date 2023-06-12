# BLACK JACK CONSOLE GAME
import random
from art import logo

# PRINT GAME BANNER
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []


def deal_card():
    choice = random.choice(cards)
    return choice


def print_user_sum():
    print(f"\tYour Cards: {user_cards}, score: {sum(user_cards)}")


def compute_winner():
    user_sum = sum(user_cards)
    dealer_sum = sum(dealer_cards)

    if dealer_sum > 21:
        print_user_sum()
        print(f"\tDealer Cars: {dealer_cards}, Score: {dealer_sum}")
        print("You Win")
    if user_sum > 21:
        print_user_sum()
        print(f"\tDealer Cars: {dealer_cards}, Score: {dealer_sum}")
        print("Dealer Wins")
    if dealer_sum == user_sum:
        print_user_sum()
        print(f"\tDealer Cars: {dealer_cards}, Score: {dealer_sum}")
        print("IT'S A DRAW")
    elif (dealer_sum < user_sum) and (user_sum < 22):
        print_user_sum()
        print(f"\tDealer Cars: {dealer_cards}, Score: {dealer_sum}")
        print("You Win")
    elif(dealer_sum > user_sum) and (dealer_sum < 22):
        print_user_sum()
        print(f"Dealer Cars: {dealer_cards}, Score: {dealer_sum}")
        print("Dealer Wins")


def black_jack():
    should_start = input("Would you like to play a game of BLACK JACK? Type 'y/Y' or 'n/N': ").lower()

    if should_start == 'y':
        for i in range(2):
            user_cards.append(deal_card())
            dealer_cards.append(deal_card())

        print_user_sum()
        print(f"\tDealer Cards {dealer_cards[1]}")

        wait_for_user = True

        while wait_for_user:
            user_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if user_choice == "y":
                user_cards.append(deal_card())
                print_user_sum()
                if sum(user_cards) > 21:
                    wait_for_user = False
            else:
                wait_for_user = False
        while sum(dealer_cards) < sum(user_cards) < 22:
            dealer_cards.append(deal_card())

        compute_winner()
        black_jack()
    elif should_start == 'n':
        print("Bye ")
    else:
        print("Invalid input")
        black_jack()


black_jack()
