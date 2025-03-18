import math

def perimeter(radius):
    return 2*math.pi*radius

def area(radius):
    return math.pi*pow(radius,2)

def volume(radius):
    return (4/3)*math.pi*pow(radius,3)

def show():
    print(f'Perimeter = {perimeter(radius):.3f}')
    print(f'Area = {area(radius):.3f}')
    print(f'Volume = {volume(radius):.3f}')

radius = float(input("Radius = "))
show()

