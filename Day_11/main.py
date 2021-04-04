"""Day_11
BlackJack Capstone Project"""
from Art import logo
import random


def deal_card():
    """Returns a random number from cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# ToDo: 3 - Create a function called calculate_score() that takes a list of
# cards as input and returns the score using the Sum() function
def calculate_score(cards):
    """Returns the sum of cards in a list"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer Lost. Player has a black jack!"
    elif user_score == 0:
        return "Player won with a BlackJack!"
    elif user_score > 21:
        return "Player lost. score above 21"
    elif user_score > computer_score:
        return "Player wins"
    else:
        return "Computer wins"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards are: {user_cards}. Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final deck is {user_score} and computer deck is {computer_score}")
    print(compare(user_score, computer_score))


while input(f"Do you want to play a game of BlackJack? Type 'y' to continue or 'n' to quit: \n") == "y":
    play_game()
