number = int(input("Enter a number: "))

p1 = 1 
p2 = 1 
print(p1)

while p2 < number:
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    print(p1)

