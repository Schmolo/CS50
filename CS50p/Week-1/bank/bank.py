
def main():
    user_input = input("Greeting: ")
    user_input = user_input.strip()
    user_input = user_input.lower()

    if not user_input.startswith("h"):
        print("$100")
    elif user_input.startswith("hello"):
        print("$0")
    else:
        print("$20")


if __name__ == "__main__":
    main()