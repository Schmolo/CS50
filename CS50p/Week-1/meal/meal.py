
def main():
    user_input = input("What time is it? ")
    user_input = user_input.strip()
    hours = convert(user_input)

    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")
    else:
        exit()


def convert(time):
    hours, minutes = time.split(":")
    time = int(hours) + int(minutes) / 60
    return time


if __name__ == "__main__":
    main()