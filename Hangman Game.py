
import random 
#ASCII
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]

for i in range(0,len(chosen_word)):
    display.append("_")
print(display)
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.

end_of_game=False
while(not end_of_game):
     guess = input("Guess a letter: ").lower()
     for letter in range(len(display)):
          if chosen_word[letter] == guess:
            display[letter]=guess
     print(display)

     if("_" not in display):
      end_of_game=True
      print("You win")
# # #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
