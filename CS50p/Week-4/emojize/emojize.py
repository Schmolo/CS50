import emoji

def main():
    user_input = input("Input: ")
    user_input = user_input.strip()

    print(emoji.emojize(user_input, language="alias"))

if __name__ == "__main__":
    main()