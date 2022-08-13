import random
# Variables
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Letters
numbers = "0123456789" # Numbers
everything = letters + numbers ## That Variable Creates The Code
characters = 16  # Fortnite Gift Card Codes Should Be 16 Characters

# Display Code
gen = ''.join(random.sample(everything, characters)) # That Will Create The Code With Its Letters And Numbers And Its Characters
print("Code Is", gen) # It Prints The Code
