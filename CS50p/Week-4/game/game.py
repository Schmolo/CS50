from random import randint

def main():
    rng = 0
    while True:
        try:
            level = int(input("Level: "))
            if not level:
                continue
            rng = randint(1, level)
            break
        except ValueError:
            continue

    while True:
        try:
            guess = int(input("Guess: "))
            if guess == rng:
                print("Just right!")
                quit()
            elif guess > rng:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            continue


if __name__ == "__main__":
    main()