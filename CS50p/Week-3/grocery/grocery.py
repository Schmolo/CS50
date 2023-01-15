from collections import OrderedDict

DICT = {}

def main():
    while True:
        try:
            user_input = input("")
            user_input = user_input.upper()
            if user_input in DICT:
                DICT[user_input] += 1
            else:
                DICT[user_input] = 1

        except EOFError:
            sorted_dict = {}
            sorted_dict = OrderedDict(sorted(DICT.items()))

            for item in sorted_dict:
                print (f"{DICT[item]} {item}")

            quit()

        except ValueError:
            continue


if __name__ == "__main__":
    main()