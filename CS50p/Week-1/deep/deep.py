
def main():
    user_input = input("What is the Answer to the Great Question of Life, the Univere, and Everything? ")
    user_input = user_input.lower()
    if "42" in user_input or user_input == "forty-two" or user_input == "forty two":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()