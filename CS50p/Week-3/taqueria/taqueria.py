
PRICE_LIST = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            user_input = input("Item: ")
            user_input = user_input.title()
            if user_input in PRICE_LIST:
                total += PRICE_LIST[user_input]
                print (f"Total: ${total:.2f}")
                continue

        except EOFError:
            quit()

if __name__ == "__main__":
    main()