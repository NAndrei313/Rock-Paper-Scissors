import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
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

game_image = [rock, paper, scissors]
person_chose = int(input())
print('You chose:')
print(game_image[person_chose])

# if person_chose == 0:
#     print(f'You chose: {rock}')
# elif person_chose == 1:
#     print(f'You chose: {paper}')
# else:
#     print(f'You chose: {scissors}')


computer_choice = random.randint(0, 2)
print('Computer chose:')
print(game_image[computer_choice])

# if computer_choice == 0:
#     print(f"Computer chose: {rock}")
# elif computer_choice == 1:
#     print(f"Computer chose: {paper}")
# else:
#     print(f'Computer chose: {scissors}')

if person_chose == 0 and computer_choice == 2:
    print('You Win!')
elif person_chose == 1 and computer_choice == 0:
    print('You Win!')
elif person_chose == 2 and computer_choice == 1:
    print('You Win!')
elif person_chose == computer_choice:
    print('It is a Draw!')
elif person_chose >= 3 or person_chose < 0:
    print('Chose another number between 0,1 or 2')
else:
    print('You Lose!')
