from turtle import Turtle, Screen


def move_forward():
    franklin.forward(10)


def move_backward():
    franklin.backward(10)


def turn_left():
    franklin.setheading(franklin.heading() + 10)


def turn_right():
    franklin.setheading(franklin.heading() - 10)


def clear_screen():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()


def main():
    global franklin

    franklin = Turtle()
    franklin.shape("turtle")
    franklin.color("green")
    franklin.speed("fastest")

    screen = Screen()
    screen.listen()

    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")

    screen.exitonclick()


if __name__ == '__main__':
    main()
