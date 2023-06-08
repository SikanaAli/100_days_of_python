import os
from art import logo

print(logo)
print("Welcome to the Secret Auction program")


# function to clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Bidders Dictionary
bidders = {}
more_bidders = True

def get_bid():
    who = input("What is your name? ")
    amount = int(input("Whats your bid? "))

    # Add bid info to bidders dictionary
    bidders[who] = amount


def compute_highest_bid(bids):
    highest_bid = 0
    bidder_name = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            bidder_name = bidder

    print(f"The winner is {bidder_name} with a bid of ZMW {highest_bid}")


get_bid()


while more_bidders:

    one_more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if one_more == "yes":
        cls()
        get_bid()
    elif one_more == 'no':
        compute_highest_bid(bidders)
        more_bidders = False
    else:
        print("Invalid input")
