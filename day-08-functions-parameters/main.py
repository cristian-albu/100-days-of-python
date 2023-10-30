import math

test_data = [[1, False], [4, False], [7, True], [26, False], [97, True]]

def prime_tests(data, function):
    test_results = []
    for test in data:
        result = function(test[0])
        if result != test[1]:
            test_results.append(f"❌ Test: {test[0]} failed. Expected to be {test[1]}")
        else:
            test_results.append(f'✅ Test: {test[0], test[1]}')
    print(test_results)
    




def basic_prime_checker(number):
    if number < 2:
        return False
    if number % 2 == 0 and number != 2:
        return False
    
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def fancier_prime_checker(number): 
    if number < 2:
        return False
    if number % 2 == 0 and number != 2:
        return False
    
    for n in range(3, round(math.sqrt(number)) + 1, 2):
        if number % n == 0 and number != n:
            return False
    return True


prime_tests(test_data, basic_prime_checker)
prime_tests(test_data, fancier_prime_checker)