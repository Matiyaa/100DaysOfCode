from turtle import Turtle, Screen, colormode
from random import choice
import colorgram


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle, length):
    for _ in range(length):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shapes(turtle, sides):
    angle = 360 / sides
    turtle.color(random_rgb_color())
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


def random_walk(turtle, steps):
    for _ in range(steps):
        turtle.forward(10)
        turtle.setheading(choice([0, 90, 180, 270]))
        turtle.color(random_rgb_color())


def random_rgb_color():
    r = choice(range(0, 256))
    g = choice(range(0, 256))
    b = choice(range(0, 256))
    return r, g, b


def draw_spirograph(turtle, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_rgb_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


def draw_hirst_painting(turtle, rows, columns, colors):
    turtle.penup()
    turtle.hideturtle()
    turtle.setheading(225)
    turtle.forward(700)
    turtle.setheading(0)
    turtle.speed("fastest")
    for row in range(rows):
        for column in range(columns):
            turtle.dot(20, choice(colors))
            turtle.forward(50)
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(50 * columns)
        turtle.setheading(0)


def main():
    franklin = Turtle()
    franklin.shape("turtle")
    franklin.color("green")
    franklin.speed("fastest")
    colormode(255)

    colors = colorgram.extract('day-18.jpg', 35)
    colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

    draw_hirst_painting(franklin, 20, 20, colors)

    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    main()
