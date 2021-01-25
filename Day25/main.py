"""
Day 25. Reading data from a CSV folder
Using the Panda module
"""
import pandas

# Use pandas to read the csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print (data.head(8))

# gray_squirrels_count = len(data["Primary Fur Color"] == "Gray")
# red_squirrels_count = len(data["Primary Fur Color"] == "Cinnamon")
# black_squirrels_count = len(data["Primary Fur Color"] == "Black")
#
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# # To construct our data frame and save in new file
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("Squirrel_count.csv")

