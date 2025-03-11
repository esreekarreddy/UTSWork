import random
"""
This program demonstrates the use of Python's random module to:
1. Generate an array of 20 random integers between 1 and 100
2. Print the generated array to the console

The random.randint() function is used to generate random integers within 
the specified range (1 to 100) and a list comprehension creates the array 
in a concise way.
"""

arrayOfNumbers = [random.randint(1, 100) for i in range(20)]

print(arrayOfNumbers)

