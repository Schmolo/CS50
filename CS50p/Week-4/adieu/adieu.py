
DEFAULT = "Adieu, adieu, to "

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            if not name:
                continue
            else:
                names.append(name)

        except EOFError:
            if len(names) == 1:
                print(f"\n{DEFAULT}{names[0]}")
                quit()

            elif len(names) == 2:
                print(f"\n{DEFAULT}{names[0]} and {names[1]}")
                quit()

            else:
                print(f"\n{DEFAULT}", end="")

                for i in range(len(names) - 2):
                    print(f"{names[i]}, ", end="")

                print(f"{names[-2]}, and {names[-1]}")
                quit()


if __name__ == "__main__":
    main()