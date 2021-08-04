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

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#print(squirrel_data[squirrel_data['Primary Fur Color']] == 'Gray')
gray_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
black_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
cinnamon_squirrels = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
print(gray_squirrels)
print(black_squirrels)
print(cinnamon_squirrels)

sq_dict = {

   "Fur Color":['Gray', 'Cinnamon', 'Black'] ,"Count":[gray_squirrels, cinnamon_squirrels, black_squirrels]
}

dFrame = pandas.DataFrame(sq_dict)
dFrame.to_csv("squirrel_count.csv")

