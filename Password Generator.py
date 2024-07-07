#pypassword generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#asking for input
# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #work out


# random_numbers=random.randint(0,len(numbers)-1)
# random_symbols=random.randint(0,len(symbols)-1)

password=[]
for n in range(nr_letters):
   password.append(random.choice(letters))

for n in range(nr_symbols):
  password.append(random.choice(symbols))

for n in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password_list=''.join(password)
print(password_list)

# #print(numbers[random_numbers]+letters[random_letter]+symbols[random_symbols])
