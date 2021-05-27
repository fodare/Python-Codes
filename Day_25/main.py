"""
Day 25
Working with CSV files and analysing Data with Pandas
"""
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_colors_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_colors_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_colors_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "fur_color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_colors_count, red_colors_count, black_colors_count]
}

new_file = pandas.DataFrame(data_dict)
new_file.to_csv("New_squirrel_data")