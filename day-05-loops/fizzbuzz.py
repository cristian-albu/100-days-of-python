fruits = ['Apple', 'Peach', 'Pair']

# for fruit in fruits:
#     print(fruit)

# for number in range(1, 10):
#     print(number)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)