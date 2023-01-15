
def main():
    user_input = input("Expression: ")
    user_input = user_input.strip()
    user_input = user_input.split(" ")

    if user_input[1] == "+":
        out = int(user_input[0]) + int(user_input[2])
        print("{:.1f}".format(out))

    elif user_input[1] == "-":
        out = int(user_input[0]) - int(user_input[2])
        print("{:.1f}".format(out))

    elif user_input[1] == "*":
        out = int(user_input[0]) * int(user_input[2])
        print("{:.1f}".format(out))

    elif user_input[1] == "/":
        out = int(user_input[0]) / int(user_input[2])
        print("{:.1f}".format(out))

    else:
        print("Invalid operator")


if __name__ == "__main__":
    main()