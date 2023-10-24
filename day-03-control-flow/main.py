print('Welcome to the rollercoaster!')
height = int(input("What is your height? "))
weight = int(input("What is your weight? "))

if height > 120 and weight < 100:
    print('You okay to go')
elif height >= 100 or weight <= 120:
    print('Barely making it')
else:
    print('Too short and fat!')



