import random

numbers = [
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]
symbols = [
'!', '@', '#', '$', '%', '^', '&', '*', '_' , '-',
'+', '!', '@', '#', '$', '%', '^', '&', '*', '+', '_', '-',
'+', '!', '@', '#', '$', '%', '^', '&', '*', '+', '_', '-'
]
letters = [
'a', 'b', 'c', 'd', 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 
 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 
 'v' , 'w' , 'x' , 'y' , 'z', 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 
 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M', 'N' , 'O' , 'P' , 'Q' , 
 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z'
 ]


combined = [numbers, symbols, letters]

password_length = input('Choose your password length: ')

if (password_length.isdigit() and int(password_length) > 0):
    num_len = len(numbers)
    sym_len = len(symbols)
    let_len = len(letters)

    password = ''

    for n in range(0, int(password_length)):
        random_num = random.randint(0, num_len + sym_len + let_len - 1)
        
        if random_num < num_len:
            password += str(combined[0][random.randint(0, num_len-1)])
        elif random_num < sym_len:
            password += combined[1][random.randint(0, sym_len-1)]
        else:
            password += combined[2][random.randint(0, let_len-1)]

    print(password)
else:
    print('You must provide a valid positive integer')