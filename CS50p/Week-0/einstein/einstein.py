
def main():
    user_input = input("m: ")
    user_input = int(user_input)

    speed_of_light = 300000000 #299792458

    e = user_input * speed_of_light ** 2

    print(f"E: {e}")

if __name__ == "__main__":
    main()