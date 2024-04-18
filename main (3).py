import random

# Define lists of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print welcome message
print("Welcome to the PyPassword Generator")

# Prompt user for number of letters, numbers, and symbols
nr_letter = int(input("how many Letters would you like?\n"))
nr_number = int(input("how many Numbers would you like?\n"))
nr_symbol = int(input("how many Symbols would you like?\n"))

# Initialize an empty list for the password
password = []

# Generate random letters and add them to the password list
for char in range(1, nr_letter+1):
    random_char = random.choice(letters)
    password += random_char

# Generate random numbers and add them to the password list
for num in range(1, nr_number+1):
    random_num = random.choice(numbers)
    password += random_num

# Generate random symbols and add them to the password list
for sym in range(1, nr_symbol+1):
    random_sym = random.choice(symbols)
    password += random_sym

# Shuffle the password list to randomize the characters
random.shuffle(password)

# Convert the password list to a string
all_character = ""
for char in password:
    all_character += char

# Print the generated password
print(f"Here is your Password: {all_character}")