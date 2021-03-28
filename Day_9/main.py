# Day 9
"""Dictionaries and Nesting"""

# Goal: Blind auction biding game

from Logo import logo as gabbel

'''Variables'''
bidders = {}

more_bidders = True

print(gabbel)
print("Welcome to the secret auction program!")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Get the bidder amount
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Set the highest amount from the bidders list
            winner = bidder  # The winner becomes the bidder with the  highest amount
    print(f"The winner is {winner} with the bid amount $ {highest_bid}")


while more_bidders:
    bidder_name = input("What is your name: ")
    bidder_amount = int(input("Enter you bid amount: $ "))
    bidders[bidder_name] = bidder_amount
    more_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bid == "yes":
        more_bidders = True
    else:
        more_bidders = False
        find_highest_bidder(bidders)
