import math 
"""
This program creates a formatted table displaying:
- Numbers from 1 to 10 ('i' column)
- Their square roots ('sqrt' column) using math.sqrt()
- Their exponential values ('exp' column) using math.exp()

The table uses:
- Center alignment (^) for all columns
- Fixed width formatting for consistent column sizes
- 2 decimal places for floating point numbers
- Pipe characters (|) and dashes (-) for table borders
"""

# Print the top border of the table
print('-' * 28)

print(f"| {'i':^3s} | {'sqrt':^7s} | {'exp':^9s} |")
print('-' * 28)

for i in range(1, 11):
    print(f"| {i:^3d} | {math.sqrt(i):^7.2f} | {math.exp(i):^9.2f} |")

print('-' * 28)
