"""
Day 11 BlackJack capstone project
AKA 21. Text based version of the game
If the sum of the played card(s) equals 21 then player losses

"""
# Rules:
# 1: Addition of cards can not go over 21. If so then it's considered a Bust
# 2: Jack, king and Queen is considered 10 and every other cards retains it's number
# 3: The Ace can either count as 1 or 11
# 4: Whenever players score = the program score then the game is a draw
# 5: If the adittion of the computer score is below 17 then the program needs to add another card
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

# Step 1: Create a deal_card() function that uses the List below to * return* a random card.
# 11 is the Ace.


def deal_card():
    # Fuction that return a random number from the cards below
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
