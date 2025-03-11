import sys 
"""
This program prompts the user to enter a series of numbers and determines the minimum and maximum values from the entered numbers.
The program continues to accept numbers until the user enters -1, which signals the end of input.

"""

number = int(input('Enter a number: '))
minimum = sys.maxsize
maximum = -sys.maxsize

while number != -1:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
    number = int(input('Enter a number: '))

print('Minimum:', minimum)
print('Maximum:', maximum)  