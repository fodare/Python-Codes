from game_data import data
import random
from art import logo, vs

# Display Art
print(logo)
score = 0
game_on = True
account_b = random.choice(data)

def format_data(account):
    """Format the account data into printable form."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Compares the user guess and follower count then return the highest """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Todo: Make the game loop until the user losses
while game_on:
    # Todo: Generate a random account from the game data.
        # Make the account at position B be position As
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Todo: Ask the user for a guess.
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # Todo: Check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Todo: Give the user a feedback on their guess.
    # Todo: Score keeping
    if is_correct:
        score += 1
        print(f"You are right. Current score is: {score}")
    else:
        game_on = False
        print(f"You are wrong. Your Score is: {score}")

