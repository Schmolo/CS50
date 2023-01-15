
VOWELS = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def main():
    user_input = input("Input: ")

    for vowel in VOWELS:
        user_input = user_input.replace(vowel, "")

    print(user_input)


if __name__ == "__main__":
    main()