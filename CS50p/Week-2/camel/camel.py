
def main():
    user_input = input("camelCase: ")
    print("snake_case: ", end="")
    for char in user_input:
        if char.isupper():
            char = char.lower()
            print(f"_{char}", end="")
        else:
            print(char, end="")
    print()


if __name__ == "__main__":
    main()