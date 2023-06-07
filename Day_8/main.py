# DAY 8 PROJECT => CEASER CIPHER
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
isExit = False


def ceaser(msg, shift_by, scramble_direction):
    output_str = ""
    if shift_by > len(alphabet):
        shift_by = shift_by % len(alphabet)
    if scramble_direction == "decode":
        shift_by *= -1
    for letter in msg:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_by
            if new_position > len(alphabet) - 1:
                new_position = new_position % len(alphabet)
            output_str += alphabet[new_position]
        else:
            output_str += letter

    print(f"Here's the {scramble_direction}d result: {output_str}")


ceaser(text, shift, direction)

while not isExit:
    repeat = input("Continue? type 'yes' to continue and 'no' to Quit: ").lower()
    if repeat == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(text, shift, direction)
    elif repeat == 'no':
        isExit = True
    else:
        print("Invalid input")
