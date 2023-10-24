import random

# between 0.000 and 0.99999
random_num = random.random()

# between 0 and 5
random_int = random.randint(0, 5)



choices = ['rock', 'paper', 'scissors']

player_choice = int(input('Choose 0 for rock, 1 for paper, and 2 for scissors: '))

computer_choice = random.randint(0, 2)

print(f'Computer choose {choices[computer_choice]}')
      
if (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
    print('You lose')
elif player_choice == computer_choice:
    print('Tie')
else:
    print('You win')