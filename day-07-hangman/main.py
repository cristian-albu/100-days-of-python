import random


word_list = ['Eagle', 'Bear', 'Elephant']
game_word = random.choice(word_list).lower()
lifes = len(game_word) - 1
game_over = False
display_word = []

for n in range(len(game_word)):
    display_word.append("_")

def check_answer(answer):
    at_least_one = False
    for n in range(len(game_word)):
        if answer == game_word[n]:
            display_word[n] = answer
            at_least_one = True
    return at_least_one

def check_winner():
    if "_" not in display_word:
        return True
    else:
        return False

print("Let's play hangman. ")

while game_over == False and lifes > 0:
    is_winner = check_winner()

    if is_winner:
        print("Congrats! You've won!")
        game_over = True
    else:
        print(display_word)
        answer = input('Write a letter: ').lower()

        if len(answer) == 1:
            result = check_answer(answer)
            if result == True:
                print('Correct')
            else:
                lifes -= 1
                print(f"Wrong. You have {lifes} lifes left")
        else:
            print("You must write 1 single letter")