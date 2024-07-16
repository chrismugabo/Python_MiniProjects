import random

logo = """
                             _   _                                  _               
  __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/                                                                              
"""

print(logo)

correct_number = random.randint(1, 100)
end_of_game = False
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

choice = input("Choose Difficulty, Type 'easy' or 'hard': ").lower()

if choice == "easy":
    counter = 10
else:
    counter = 5

while not end_of_game and counter > 0:
    print(f"You have {counter} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < correct_number:
        print("Too low.")
    elif guess > correct_number:
        print("Too high.")
    else:
        end_of_game = True
        print(f"Congratulations! You guessed the correct number: {correct_number}")

    counter -= 1

if not end_of_game:
    print(f"You've run out of attempts! The correct number was: {correct_number}")
