# PROJECT DAY 5 of 100
# PASSWORD GENERATOR

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

temp_letters = ""
temp_numbers = ""
temp_symbols = ""

for letter in range(1, nr_letters + 1):
    temp_letters += letters[random.randint(0, int(len(letters) - 1))]

for num in range(1, nr_numbers + 1):
    temp_numbers += numbers[random.randint(0, int(len(numbers) - 1))]

for symbol in range(1, nr_symbols + 1):
    temp_numbers += numbers[random.randint(0, int(len(symbols) - 1))]

temp_pass = temp_letters + temp_numbers + temp_symbols

final_pass = "".join(random.sample(temp_pass, len(temp_pass)))

print(f"Your Password is : {final_pass}")

