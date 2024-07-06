import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#human choice
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if(choice==0):
    print(rock)
elif (choice==1):
     print(paper)
elif (choice==2):
 print(scissors)

#computer choice
print("The computer chose:")
computer_choices=[rock,paper,scissors]
random_choice=random.randint(0,len(computer_choices)-1)
print(computer_choices[random_choice])

if(choice==random_choice):
   print("It's a draw")
elif((choice==0 and random_choice==2)):
   print("You win")
elif(choice==1 and random_choice==0):
   print("You win")
elif(choice==2 and random_choice==1):
   print("You Win")
elif(choice==2 and random_choice==0):
   print("You Lose")
elif(choice==0 and random_choice==1):
   print("You Lose")
elif(choice==1 and random_choice==2):
   print("You Lose")
else:
   print("you typed an invalid number, You Lose")