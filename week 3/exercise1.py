import math

x = 4.6666789
y = 2.2346576
print(f"x + y = {x + y:.3f}")
print(f"x - y = {x - y:.3f}")
print(f"x * y = {x * y:.3f}")
print(f"x / y = {x / y:.3f}")
print(f"x%y+x/y = {(x%y)+(x/y):.3f}")

new_operation = (pow(y, 7) / (math.sqrt(5) + x)) * ((pow(x, 4) % 5) + 2)
print(f"new_operation = {new_operation:.3f}")