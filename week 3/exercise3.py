import math

def circle_area(radius):
    return math.pi * radius ** 2

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

radius = int(input("Enter the radius of the circle: "))
area = circle_area(radius)
volume = sphere_volume(radius)

print(f"Circle area of radius {radius} is {area:.2f}")
print(f"Sphere volume of radius {radius} is {volume:.2f}")

