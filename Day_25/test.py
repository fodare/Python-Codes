# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row [1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")

# Get data in Columns
# print(f"Getting data from a column: {data.day} ")

# Get data from rows
max_temperatures = data.temp.max()
print(max_temperatures)
day = data[data.temp == max_temperatures]
print(f"The day with the maximum tempreature is:{day.day}")


#Create dataframe
sample_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(sample_dictionary)
print(new_data)
# Create a CSV file
new_data.to_csv("New_data_set.csv")