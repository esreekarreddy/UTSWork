import random

number = int(input("Enter a number: "))
random.seed(10)

total = 0 
for _ in range(number):
    value = random.randint(0, 1000)
    print(value, end= " ")
    if value % 2 == 0:
        total += value
print()    
print(total)