
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not len(s) <= 6 or not len(s) >= 2:
        return False

    elif not s.isalnum():
        return False

    elif not s[0:2].isalpha():
        return False

    check = True
    for char in s:

        if char.isnumeric():
            if check == True and char == "0":
                return False
            else:
                check = False

        if check == False and char.isalpha():
            return False

    else:
        return True


main()