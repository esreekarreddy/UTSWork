import random

n = int(input("Enter a number: "))

numbers = [random.randint(0,99) for _ in range(n)]

print(numbers)

numbers[0], numbers[-1], numbers[n//2] = 10, -5, 3

print(numbers)



