# DAY 8 PROJECT => CEASER CIPHER
from collections import deque
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shiftBy):
    encryptedStr = ""
    temp_alphabet = deque(alphabet)
    temp_alphabet.rotate(-int(shiftBy))
    for i in range(0,len(text)):
        if text[i] == " ":
            encryptedStr += " "
        else:
            index = temp_alphabet.index(text[i])
            encryptedStr += temp_alphabet[index]
    print(temp_alphabet)
    print(f"Encrypted => {encryptedStr}")


encrypt(text,shift)