number = int(input('Enter a number: '))
while number != -1:
    sum = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            sum += i
    print(f'Even summation of {number} is {sum}')
    number = int(input('Enter a number: '))