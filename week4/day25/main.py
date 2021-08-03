# import csv

# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

# temp_list = data['temp'].to_list()
# temp_sum = 0

# for temp in temp_list:
#     temp_sum += temp

# temp_sum = temp_sum / len(temp_list)
# #print(temp_sum)
# print(data['temp'].max())

def convert_to_farenheit(c_temp):
    return (c_temp * 9/5) + 32
monday = (data[data.day == 'Monday'])
#print(monday.to)

print(convert_to_farenheit(monday.temp))
