import random as ran 

number = ran.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != number:
    guess = int(input("Sorry! try again: "))

print(f"Success, secret number is {number}")