# [message, shift, result]
test_data = [['Hello', 5, 'mjqqt'], ['axyz', 5, 'fcde'], ['abc', 1, "bcd"]]

def test_encryption(data, func):
    output = []
    for test in data:
        result = func(test[0], test[1])
        if result != test[2]:
            output.append(f'❌ {test} failed') 
        else:
            output.append(f'✅ {test} succeeded')
    print(output)




def encrypt_caesar(message, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    output = ""

    for letter in list(message):
        if letter == ' ':
            output += ' '
        else:
            index_of_curr = letters.index(letter.lower())
            if index_of_curr + shift < len(letters):
                output += letters[index_of_curr + shift]
            else:
                output += letters[index_of_curr + shift - len(letters)]
    
    return output


test_encryption(test_data, encrypt_caesar)

def run_live():
    message = input('Write your message. This will be encrypted: ').lower()
    shift = int(input('Write the shift of the message: '))

    result = encrypt_caesar(message, shift)

    print(result)

run_live()