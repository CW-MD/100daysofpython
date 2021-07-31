#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#read names
names_list = []
with open("./Input/Names/invited_names.txt") as file:
    raw_list = file.readlines()
    
for item in raw_list:
    names_list.append(item.strip())

#print(names_list)

#read template letter
with open("./Input/Letters/starting_letter.txt") as file:
    #header = file.readlines()[0].replace('[name]')
    letter = file.read()
    for name in names_list:
        new_letter = letter.replace('[name]', name)
        with open(f'./Output/ReadyToSend/letter_to_{name}.txt', 'w') as file:
            file.write(new_letter)

