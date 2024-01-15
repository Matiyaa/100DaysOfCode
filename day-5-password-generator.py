import random
import string


def main():
    print("Welcome to the Python Password Generator!")
    letters = int(input("How many characters would you like in your password? "))
    symbols = int(input("How many symbols would you like? "))
    numbers = int(input("How many numbers would you like? "))

    password = ""

    for i in range(letters):
        password += random.choice(string.ascii_letters)

    for i in range(symbols):
        symbol = random.choice(string.punctuation)
        pos = random.randint(0, len(password) - 1)
        password = "".join((password[:pos], symbol, password[pos:]))

    for i in range(numbers):
        number = random.choice(string.digits)
        pos = random.randint(0, len(password) - 1)
        password = "".join((password[:pos], number, password[pos:]))

    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()
