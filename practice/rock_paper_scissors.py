import random
# Több soros stringet '''  ''' jelek közé rakjuk
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

list = [rock, paper, scissors]

choice = input("What do you choose? 0 - Rock, 1 - PAper, 2 - Scissors")
choice_to_num = int(choice)
random_num = random.randint(0,2)
print("Your choice:")
print(choice_to_num)
print(list[choice_to_num])
print("Computer's choice:")
print(random_num)
print(list[random_num])

if (choice_to_num == 0 and random_num == 2) or (choice_to_num == 1 and random_num == 0) or (choice_to_num == 2 and random_num == 1):
    print("You win!")
elif (choice_to_num == 0 and random_num == 1) or (choice_to_num == 1 and random_num == 2) or (choice_to_num == 2 and random_num == 0):
    print("You loose")
elif (choice_to_num == random_num):
    print("Draw")
else:
    print("Wrong number")