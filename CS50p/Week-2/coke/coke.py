
def main():
    cost = 50
    while True:
        if cost <= 0:
            cost = abs(cost)
            print(f"Change Owed: {cost}")
            break
        else:
            print(f"Amount Due: {cost}")
            user_input = input(f"Insert Coin: ")
            user_input = int(user_input)
            if user_input == 25 or user_input == 10 or user_input == 5:
                cost -= user_input


if __name__ == "__main__":
    main()