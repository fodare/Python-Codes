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
