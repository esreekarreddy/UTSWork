def upper_diamond(n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()  

def middle_diamond(n):
    for i in range(n):
        print("* ", end="")
    print()

def lower_diamond(n):
    for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()  

while True:
    size = int(input("Enter diamond size (-1 to exit): "))
    if size == -1:
        break
    print(f"Size: {size}")
    upper_diamond(size)
    middle_diamond(size)
    lower_diamond(size)
