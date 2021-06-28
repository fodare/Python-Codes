# Todo 1: Exception handling test 1
fruits = ["Apple", "Pear", "Orange"]

"""Catch the exception and make sure the code runs without crashing"""


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"Fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(4)

# Todo 2: Exception handling test 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 2},
    {'Likes': 19, 'Comments': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
print(f"Total number of likes = {total_likes}")