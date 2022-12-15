from cs50 import get_int

answer = 0
sharp = 1

while True:
    answer = get_int("Height: ")
    if answer in range(1, 9):
        break

space = answer - 1

for i in range(answer):

    for j in range(space):
        print(" ", end="")

    space -= 1

    for l in range(sharp):
        print("#", end="")

    print("  ", end="")

    for o in range(sharp):
        print("#", end="")

    sharp += 1

    print("")