from random import randint


def main():
    print(r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)

    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            attempts = 10
            break
        elif difficulty == 'hard':
            attempts = 5
            break
        else:
            print("Invalid input.")
            continue

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}.")
            break

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The answer was {number}.")
    else:
        print("You win!")

    print("Thanks for playing!")
    print("Goodbye!")


if __name__ == '__main__':
    main()
