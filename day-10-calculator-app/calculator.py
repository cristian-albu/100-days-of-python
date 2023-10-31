def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def determine_operation(text):
    if text == "+":
        return add
    elif text == "-":
        return subtract
    elif text == '*':
        return multiply
    elif text == '/':
        return divide
    else:
        redo = input('Please enter a valid operator: ')
        return determine_operation(redo)
    
def prompt_continue(result):
    should_continue = input(f"Result is: {result}. Want to continue? y/n: ")
    if should_continue == 'n':
        return False
    elif should_continue == 'y':
        return True
    else:
        print('Provide the proper inputs')
        prompt_continue(result)

def start_calculator():
    count = 0
    first_num = int(input('Enter a number: '))
    stop_calculator = True
    while stop_calculator == True:
        if count != 0:
            first_num = result 
        operation_input = input('Choose operation (+, -, *, /): ')
        operation = determine_operation(operation_input)
        second_num = int(input('Enter a number: '))
        result = operation(first_num, second_num)
        stop_calculator = prompt_continue(result)

        count += 1

start_calculator()