import pandas
{"A": "Alfa", "B": "Bravo"}

nato_raw = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in nato_raw.iterrows()}
# print(nato_dict)

user_input = input('Enter a word: ').upper()

phonetic_output = [nato_dict[x] for x in user_input]

print(user_input, ':', phonetic_output)