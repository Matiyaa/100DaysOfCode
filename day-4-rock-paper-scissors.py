def main():
    import random
    import os
    import time

    def clear():
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def rock(player):
        print(f"{player} chose rock.")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

    def paper(player):
        print(f"{player} chose paper.")
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

    def scissors(player):
        print(f"{player} chose scissors.")
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    def win(p1, p2):
        if p1 == "rock" and p2 == "scissors":
            return True
        elif p1 == "paper" and p2 == "rock":
            return True
        elif p1 == "scissors" and p2 == "paper":
            return True
        else:
            return False

    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors.")
    clear()
    print("You will be playing against the computer.")
    clear()
    print("The first to 3 points wins.")
    clear()
    print("Ready?")
    clear()
    print("Rock...")
    clear()
    print("Paper...")
    clear()
    print("Scissors...")
    clear()
    print("Shoot!")
    clear()
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        player_choice = input("What do you choose? Type 'rock', 'paper', or 'scissors'.\n").lower()
        if player_choice in choices:
            computer_choice = random.choice(choices)
            if player_choice == "rock":
                rock("You")
            elif player_choice == "paper":
                paper("You")
            else:
                scissors("You")
            if computer_choice == "rock":
                rock("Computer")
            elif computer_choice == "paper":
                paper("Computer")
            else:
                scissors("Computer")
            if win(player_choice, computer_choice):
                player_score += 1
                print("You win this round!")
            elif win(computer_choice, player_choice):
                computer_score += 1
                print("The computer wins this round!")
            else:
                print("It's a tie!")
            print(f"Your score: {player_score}")
            print(f"Computer score: {computer_score}")
            clear()
        else:
            print("You didn't type 'rock', 'paper', or 'scissors'.")


if __name__ == "__main__":
    main()
