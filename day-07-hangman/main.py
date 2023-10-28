import random
word_list = ['professor', 'worker', 'wizard']



game_word = random.choice(word_list)


print(game_word)

def build_hidden_word(word, tip_number):
    word_arr = list(word)
    count = len(word) - tip_number
    
    while count > 0:
        random_choice = random.choice(word_arr)
        if random_choice != '_':
            index = word_arr.index(random_choice)
            word_arr[index] = '_'
            count -= 1
    return "".join(word_arr)

    

print(build_hidden_word('Anaconda', 2))
