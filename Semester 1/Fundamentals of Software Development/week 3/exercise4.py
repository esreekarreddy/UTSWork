import math

x1 = float(input("Please enter the x1 coordinate of point A: "))
y1 = float(input("Please enter the y1 coordinate of point A: "))
x2 = float(input("Please enter the x2 coordinate of point B: "))
y2 = float(input("Please enter the y2 coordinate of point B: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between A({x1:.1f}, {y1:.1f}) and B({x2:.1f}, {y2:.1f}) is {distance:.2f}")
