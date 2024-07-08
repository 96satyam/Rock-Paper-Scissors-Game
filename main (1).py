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

#Write your code below this line 👇
my_list  = ["rock","paper","scissors"]
my_list[0] = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

my_list[1] = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

my_list[2] = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


my_choice =input("Enter your choice:\n 0 for rock\n 1 for paper\n 2 for scissors\n")
choice1 = int(my_choice)
result=my_list[choice1]
print(result)
print("Computer Choose:")
import random
choice2 = random.randint(0,2)
result2 = my_list[choice2]
print(result2)
if (choice1==choice2):
    print("DRAW! Try again")
elif (choice1==0 and choice2==2):
    print("You Win!")
elif(choice1==1 and choice2==0):
    print("You Win!")
elif(choice1==2 and choice2 ==1):
    print("You WIn!")
else:
    print("You Loose!")