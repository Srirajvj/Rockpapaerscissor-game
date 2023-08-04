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
import random
x=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor\n "))
y= random.randint(0, 2)
if x==0:
    if y==0:
        print(rock)
        print("Computer also choose:")
        print(rock)
        print("Try again")
    elif y==1:
        print(rock)
        print("Computer choose:")
        print(paper)
        print("You loose")
    else:
        print(rock)
        print("Computer choose:")
        print(scissors)
        print("You win")
elif y==1:
    if y==0:
        print(paper)
        print("Computer choose:")
        print(rock)
        print("You win")
    elif y==1:
        print(paper)
        print("Computer also choose:")
        print(paper)
        print("Try again")
    else:
        print(paper)
        print("Computer choose:")
        print(scissors)
        print("You loose")
else:
    if y==0:
        print(scissors)
        print("Computer choose:")
        print(rock)
        print("You loose")
    elif y==1:
        print(scissors)
        print("Computer choose:")
        print(paper)
        print("You win")
    else:
        print(scissors)
        print("Computer also choose:")
        print(scissors)
        print("Try again")