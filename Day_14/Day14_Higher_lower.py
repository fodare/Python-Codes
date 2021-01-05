"""
Day 14. Test game Higher or Lower
"""
import random
from game_data import data
import os
Logo = """
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ /_/_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/

"""

VS_Logo = """
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""

# Step 1: Display Logo
print(Logo)
score = 0
# Score tracking
game_should_continue = True
##### Functions #####
account_b = random.choice(data)


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr} from {account_country} ")

# use if statement to check if user is correct


def check_answer(guess, a_followers, b_followers):
    """ Takes the user and follower counts and returns if they got
    it right  """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def clear():
    os.system('clear')


# Make the game repeatable
while game_should_continue:

    # Step 2: Generate a randpm account from the game data.

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Step 3: Format the account data into a printable format.
    # By pulling the value of the key from data

    print(f"Compare A: {format_data(account_a)}. ")
    print(VS_Logo)
    print(f"Against B: {format_data(account_b)}. ")

    # step 4: Ask the user for a guess. The .lower() is to catch the scenario
    # where the user could type either a,b,A,B so the code works in any condition
    guess = input(f"Who has more followers, type 'A' or 'B': ").lower()

    # check if the user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the console
    clear()
    print(Logo)

    # Give the user a feedback on their guess
    if is_correct:
        score = score + 1
        print(f"You are right! Your score is {score}")
    else:
        print(f"Oops you are wrong!. Final score is: {score}")
        game_should_continue = False
