
FRUITS_CALORIES = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, "plums": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80}

def main():
    user_input = input("Item: ")
    user_input = user_input.lower()
    for item in FRUITS_CALORIES:
        if user_input == item:
            print("Calories: " + str(FRUITS_CALORIES[item]))
            break

if __name__ == "__main__":
    main()