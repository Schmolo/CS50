
def main():
    while True:
        try:
            user_input = input("Fraction: ")
            user_input = user_input.split("/")

            if int(user_input[0]) > int(user_input[1]):
                continue

            percentage = int(user_input[0]) / int(user_input[1]) * 100

            if percentage >= 99:
                print("F")
                quit()

            elif percentage <= 1:
                print("E")
                quit()

            else:
                print(f"{percentage:.0f}%")
                quit()

        except ValueError:
            continue
        except ZeroDivisionError:
            continue


if __name__ == "__main__":
    main()