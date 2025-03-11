def count_vowels_upper_and_lower_case():
    value = input("Enter a character: ")

    lower_case_vowels = "aeiou"
    upper_case_vowels = "AEIOU"

    lower_case_vowels_count = 0
    upper_case_vowels_count = 0

    while value != ".":
        if value in lower_case_vowels:
            lower_case_vowels_count += 1
        elif value in upper_case_vowels:
            upper_case_vowels_count += 1
        value = input("Enter a character: ")

    print("Lower case vowels:", lower_case_vowels_count)
    print("Upper case vowels:", upper_case_vowels_count)

def count_vowels():
    value = input("Enter a character: ")

    vowels = "aeiouAEIOU"

    vowels_count = 0

    while value != ".":
        if value in vowels:
            vowels_count += 1
        value = input("Enter a character: ")

    print("Vowels:", vowels_count)

def main():
    #count_vowels_upper_and_lower_case()
    count_vowels()

if __name__ == "__main__":
    main()
