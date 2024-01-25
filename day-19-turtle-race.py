from turtle import Turtle, Screen
from random import randint


def main():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = None

    while user_bet not in colors:
        user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

    turtles = []

    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=-100 + colors.index(color) * 40)
        turtles.append(turtle)

    race = True

    while race:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() >= 230:
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")
                race = False


if __name__ == '__main__':
    main()
