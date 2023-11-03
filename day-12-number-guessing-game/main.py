import random

def init_game():
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    if difficulty != 'easy' and difficulty != 'hard':
        print('You have to choose a difficulty')
        init_game()
    else:
        return difficulty
    
def guess_number():
    guess = int(input('Guess a number: '))
    if guess == number:
        print('You win')
        return True
    elif guess > number:
        print('Too high')
        return False
    elif guess < number:
        print('Too low')
        return False

print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
lives = 5
difficulty = init_game()

if difficulty == 'easy':
    lives += 10

while lives > 0:
    print(f"Lives left: {lives}")

    guess = guess_number()
    if guess == True:
        break
    else:
        lives -= 1
        
if lives == 0:
    print('You lost')



