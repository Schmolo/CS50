import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    # Check if the argument is a number
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Invalid command-line argument")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Error: API request failed")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]

    print(f"${(price * amount):,.4f}")


if __name__ == "__main__":
    main()