import sys
from pyfiglet import Figlet
import random

FONTS = Figlet().getFonts()

def main():
    if len(sys.argv) == 1:

        font = FONTS[random.randint(0, len(FONTS) - 1)]

        user_input = input("Input: ")

        f = Figlet(font=font)
        print(f.renderText(user_input))

    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in FONTS:
            print("Invalid usage")
            sys.exit(1)

        user_input = input("Input: ")

        f = Figlet(font=sys.argv[2])
        print(f.renderText(user_input))

    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == "__main__":
    main()