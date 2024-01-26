from turtle import Screen, Turtle
from time import sleep


def main():
    class ScoreBoard(Turtle):
        def __init__(self):
            super().__init__()
            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(0, 260)
            self.score_r = 0
            self.score_l = 0
            self.font = ("Courier", 24, "normal")
            self.align = "center"
            self.write(f"Score: {self.score_l}:{self.score_r}", align=self.align, font=self.font)

        def update(self):
            if ball.xcor() > 350:
                self.score_l += 1
                ball.reset()
            elif ball.xcor() < -350:
                self.score_r += 1
                ball.reset()
            self.clear()
            self.write(f"Score: {self.score_l}:{self.score_r}", align=self.align, font=self.font)

    class Paddle(Turtle):
        def __init__(self, position):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(position, 0)

        def go_up(self):
            self.goto(self.xcor(), self.ycor() + 20)

        def go_down(self):
            self.goto(self.xcor(), self.ycor() - 20)

    class Ball(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.color("white")
            self.penup()
            self.x_move = 10
            self.y_move = 10

        def move(self):
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

        def bounce_y(self):
            self.y_move *= -1

        def reset(self):
            self.goto(0, 0)
            self.bounce_y()
            self.x_move = 10
            self.y_move = 10

        def bounce_x(self):
            self.x_move *= -1

        def speed_up(self):
            self.x_move *= 1.1
            self.y_move *= 1.1

    class ScreenSetup:
        def __init__(self):
            self.screen = Screen()
            self.screen.setup(width=800, height=600)
            self.screen.bgcolor("black")
            self.screen.title("Pong")
            self.screen.tracer(0)
            self.screen.listen()

        def onkey(self, function, key):
            self.screen.onkeypress(function, key)

        def update(self):
            self.screen.update()

        def bye(self):
            self.screen.bye()

        def exitonclick(self):
            self.screen.exitonclick()

    screen_setup = ScreenSetup()
    score_board = ScoreBoard()
    paddle = Paddle(350)
    paddle2 = Paddle(-350)
    ball = Ball()

    screen_setup.onkey(paddle.go_up, "Up")
    screen_setup.onkey(paddle.go_down, "Down")

    screen_setup.onkey(paddle2.go_up, "w")
    screen_setup.onkey(paddle2.go_down, "s")

    screen_setup.onkey(screen_setup.bye, "Escape")

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen_setup.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if (ball.distance(paddle) < 50 and 360 > ball.xcor() > 320 or ball.distance(paddle2) < 50
                and -360 < ball.xcor() < -320):
            ball.bounce_x()
            ball.speed_up()
        if ball.xcor() > 380 or ball.xcor() < -380:
            score_board.update()
            ball.reset()

    screen_setup.exitonclick()


if __name__ == '__main__':
    main()
