import random

# print("Welcome to the Virtual coin tossing game")
# random_number = random.randint(0,1)
# user_in = input("Heads OR Tail? Chose 1: \n")
# if random_number == 1:
#     print("Heads win!")
# else:
#     print("Tails win!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




# Who pays the Bill
names_list = ["Aurthur", "Benjamin", "Rolland", "Benson", "Dirk"]
random_number = random.randint(0,len(names_list)-1)
# ToDo 1:
print("Who pays the bill!")
payer = names_list[random_number]
print(f"{payer} Pays the bill today!")
