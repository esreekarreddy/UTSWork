import random, math

def generate_random_numbers(n):
    return [random.randint(0, 100) for i in range(n)]

def calculate_mean(elements):
    return sum(elements) / len(elements)

def calculate_standard_deviation(elements):
    mean = calculate_mean(elements)
    variance = sum((x - mean) ** 2 for x in elements) / len(elements)
    return math.sqrt(variance)

def show_calculated_values(elements):
    mean = calculate_mean(elements)
    std_dev = calculate_standard_deviation(elements)
    print(f'Mean: {mean:.2f}')
    print(f'Standard Deviation: {std_dev:.2f}')

# Generate 20 random numbers
random_numbers = generate_random_numbers(20)    
show_calculated_values(random_numbers)