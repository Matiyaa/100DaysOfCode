def main():
    print("Welcome to the tip calculator.")

    bill = input("What was the total bill? $")
    tip = input("What percentage tip would you like to give? 10, 15, or 20? ")
    people = input("How many people to split the bill? ")

    total = float(bill) * (1 + float(tip) / 100)

    print(f"Each person should pay: ${round(total / int(people), 2)}")


if __name__ == "__main__":
    main()
