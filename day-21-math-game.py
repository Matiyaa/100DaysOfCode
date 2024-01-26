from random import randint


def main():
    print("Welcome to the Math Game!")
    print("You will be asked 10 questions.")
    print("Good luck!")

    score = 0
    for i in range(0, 10):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        answer = num1 * num2
        user_answer = int(input(f"{num1} x {num2} = "))
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is {answer}.")

    print(f"You got {score} out of 10 questions correct.")


if __name__ == '__main__':
    main()
