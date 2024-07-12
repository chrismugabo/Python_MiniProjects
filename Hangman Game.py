# Import necessary modules
# Import necessary modules
# Import necessary modules
# Import necessary modules
# Import necessary modules
import random
from hangman_words import word_list  # Import the list of words
from hangaman_art import stages  # Import the ASCII art for the game stages

# Game initialization
lives = len(stages)  # Set initial lives based on the number of stages
end_of_game = False  # Flag to control the game loop
chosen_word = random.choice(word_list)  # Randomly select a word from the list
word_length = len(chosen_word)  # Get the length of the chosen word

# Debugging line to help during development (should be removed in production)
print(f'Pssst, the solution is {chosen_word}.')

# Initialize the display list with underscores for each letter in the chosen word
display = []
for i in range(word_length):
  display.append("_")
print(display)

# Main game loop
while not end_of_game:
  guess = input("Guess a letter: ").lower()  # Prompt the user for a guess

  # Check each letter in the chosen word against the user's guess
  for letter in range(len(display)):
    if chosen_word[letter] == guess:
      display[letter] = guess  # Reveal the guessed letter in the display
  print(display)
  
  # If the guess is incorrect, reduce lives
  if guess not in chosen_word:
    lives -= 1
  print(stages[lives])  # Display the current stage of the hangman

  # Check for loss condition
  if lives == 0:
    end_of_game = True
    print("You lose")

  # Check for win condition
  if "_" not in display:
    end_of_game = True
    print("You win")