import random

def genereate_random_numbers(n):
    return [random.randint(0, 10) for i in range(n)]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_array(array_of_numbers):  
    factorial_array = []
    for num in array_of_numbers:
        factorial_array.append(factorial(num))
    return factorial_array

def show_arrays(random_numbers, factorial_numbers):
    print(f'Array of random numbers: {random_numbers}')
    print(f'Array of factorials: {factorial_numbers}')

random_numbers = genereate_random_numbers(5)
factorial_numbers = factorial_array(random_numbers)
show_arrays(random_numbers, factorial_numbers)