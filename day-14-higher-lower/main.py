from game_data import data
import random

print ("Higher lower")

def calc_answer(choice_a, choice_b):
    if choice_a['follower_count'] > choice_b['follower_count']:
        return "A"
    elif choice_a['follower_count'] < choice_b['follower_count']:
        return "B"
    else:
        return 'Same'
    
def check_answer(choice, answer):
    if choice == answer:
        print('Good guess!')
        return True
    else:
        print('Not good!')
        return False

def play_game(points, prev_b):    
    print(f'Current points: {points}')
    choice_a = prev_b
    choice_b = random.choice(data)
    print(f"{choice_a['name']} vs. {choice_b['name']}")
    choice = input('Who has more followers? A or B: ')
    correct_answer = calc_answer(choice_a, choice_b)
    player_answer = check_answer(choice, correct_answer)

    if player_answer == True:
        points = points + 1
        play_game(points, choice_b)
        
    else:
        print('Game over')
        return points


play_game(0, random.choice(data))

