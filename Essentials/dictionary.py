"""
Sample dictionary and it's method 
"""
user = {
    'name': 'Damilare',
    'location': 'Tallinn',
    'Work-Experience': '10 Years',
    'interest': 'Volley ball'
}

print(user)

user.update({'Hobbies': 'Soccer'})
print(user)

print(user.popitem())
