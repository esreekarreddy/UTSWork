def read_a_sentence():
    return input("Enter a sentence: ")

def count_vowels(sentence):
    count = 0
    for _ in 'aeiou':
        count += sentence.count(_)
    return count

def show_number_of_vowels():
    sentence = read_a_sentence()
    while sentence != '*':
        print(f'Number of vowels = {count_vowels(sentence.lower())}')
        sentence = read_a_sentence()

show_number_of_vowels()