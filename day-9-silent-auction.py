def main():
    print('''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    ''')

    auction = {}
    print("Welcome to the secret auction program.")

    bidding = True
    while bidding:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))

        auction[name] = bid

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if more_bidders == "no":
            bidding = False
            highest_bidder = max(auction, key=auction.get)
            print(f"The winner is {highest_bidder} with a bid of ${auction[highest_bidder]}")
        elif more_bidders == "yes":
            print("Next bidder.")
        else:
            print("Invalid input. Next bidder.")


if __name__ == "__main__":
    main()
