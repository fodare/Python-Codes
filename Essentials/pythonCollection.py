# There are generally 4 types of collections in python and they are namely
# List: Collection which is ordered and changable. Allows dupicate value
# Tuple: collection which is ordered and unchangable. Allows dupicate values
# Set: collection which is nor ordered and unindexed. No duplicate members
# Dictionary: collection of un-ordereded, changable and indexed. no duplicate members

# Python List
# Python list is a collection of ordered and changeable dataset. They are written with square brackets.
fruits = ["Apple", "Carrot", "Orange"]
print(fruits)
print(fruits[2])
# To access a data a list, simply use the index value of the list. Example above


# You can also change the item in a list and example below
countries = ["Nigeria", "Etopia", "India",
             "United Arab Emirate", "Finland", "Estonia"]
countries[3] = "UAE"
countries.append("Germany")
print(countries)

# Python Tuples are collection of ordered unchangable and allows duplicate values, they are enclosed in a round brackets
myNames = ("Damilare", "Olatunbosun", "Folorunso")
print(myNames)

# Accessing tuples items can be done by using the index value of the data we are trying to access. Example below
print(myNames[1])


# Python Set is a collection of unordered and un-indexed. Does not allow duplicate members. example below
fooditems = {"Oil", "Pans", "Meats", "Vegetables"}
print(fooditems)
# Adding a single item to a set, use the add() method. Example below
fooditems.add("Cereals")
print(fooditems)

# Adding multiple items to a set use the update()method. Example below
fooditems.update(["Wheat", "Pasta", "Tea"])
print(fooditems)
print(len(fooditems))

# To remove an item from the set, simply use the remove() or discard() method. Example below
fooditems.remove("Pans")
print(fooditems)


# Another Collection od the dictionary. It's a collection of unordered , changale, indexed and has a key value

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year":  "1964"}

print(thisDict)

# To access an element of the dictonary use the . method with the keyname inside a square brackets
print(thisDict["Year"])

# You can also change the value of a keyname in a dictonary. Example is
thisDict["Year"] = 2018
print(thisDict)
