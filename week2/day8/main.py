alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encoded_text = ''
  for letter in text:
    index = alphabet.index(letter)
    index += shift
    if index < 26:
      encoded_text += alphabet[index]
    else:
      encoded_text +=alphabet[abs(26-index)]
  print(encoded_text)


def decrypt(text, shift):
  decoded_text = ''
  for letter in text:
    index = alphabet.index(letter)
    index -= shift
    if index >= 0:
      decoded_text += alphabet[index]
    else:
      decoded_text += alphabet[26 + index]
  print(decoded_text)
    
if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)
else:
  input('Please enter a valid command: ')