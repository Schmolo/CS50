
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            user_input = input("Date: ")
            user_input = user_input.strip()

            if user_input[1] == "/" or user_input[2] == "/":
                user_input = user_input.split("/")
                month = int(user_input[0])
                day = int(user_input[1])
                year = int(user_input[2])

            else:
                user_input = user_input.split(" ")

                month = user_input[0]
                if month not in MONTHS:
                    continue
                else:
                    month = MONTHS.index(month) + 1

                day = user_input[1]
                if len(day) != 2:
                    continue

                elif day[1] != ",":
                    continue

                else:
                    day = int(day.replace(",", ""))

                year = int(user_input[2])

            if day > 31:
                continue
            if month > 12:
                continue

            print(f"{year:04}-{month:02}-{day:02}")
            quit()

        except ValueError:
            continue


if __name__ == "__main__":
    main()