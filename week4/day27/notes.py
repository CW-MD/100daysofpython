import random
import pandas
numbers = [1,2,3,4,5]
#print(numbers)


def even_double(num):
    if num % 2 == 0:
        num = num * 2
    return num


numplus = [even_double(num) for num in numbers]
print(numplus)

name = 'Chadwick McDayton'

def alt_case(str,let):
    if str.index(let) % 1 == 2:
        if let == let.upper():
            let = let.lower()
        else:
            let = let.upper()
        return let
    else:
        return let

new_name = [alt_case(name, letter) for letter in name]



# print(new_name)

double_range = [n*2 for n in range(1,10)]

# print(double_range)

names = ['Alex', 'Beth', 'Carol', "Mike", 'Ashleigh', 'Hartej']

long_upper = [name.upper() for name in names if len(name) > 4]

# print(long_upper)
# print(10)

student_scores = {student:random.randint(1,100) for student in names}
#print(student_scores)

passed_scores = {student:student_scores[student]  for student in student_scores if student_scores[student] > 59}

print(passed_scores)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: