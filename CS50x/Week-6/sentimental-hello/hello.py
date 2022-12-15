from cs50 import get_string

# Ask user for name
name = get_string("Whats your name? ")

# if no name given print hello, world else print hello, {given name}
if name == "":
    print("hello, world")
else:
    print(f"hello, {name}")