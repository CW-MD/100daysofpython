from os import close


with open("test.txt") as file:
    contents = file.read()
    print(contents)

with open("test.txt", 'w') as file:
    file.write('Using w mode will overwrite all prior text')

with open('test.txt', 'a') as file:
    file.write('\n"a" will Append new text instead')

with open("new_test.txt", 'w') as file:
    file.write('write mode can also be used to create and write to new files')