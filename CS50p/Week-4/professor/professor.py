import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        fail_count = 0
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        while True:
            try:
                if fail_count == 3:
                    print(f"{n1} + {n2} = {n1 + n2}")
                    break

                user_input = input(f"{n1} + {n2} = ")
                if int(user_input) == n1 + n2:
                    score += 1
                    break
                else:
                    print("EEE")
                    fail_count += 1

            except ValueError:
                fail_count += 1
                continue
    print(f"Score: {score}")
    quit()

def get_level():
    while True:
        try:
            user_input = input("Level: ")
            user_input = int(user_input)

            if user_input not in range(1, 4):
                raise ValueError()

            return user_input

        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        minumum = 0
        maximum = 9
    else:
        minumum = pow(10, level - 1)
        maximum = pow(10, level) - 1
    return random.randint(minumum, maximum)


if __name__ == "__main__":
    main()