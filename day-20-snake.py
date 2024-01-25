from turtle import Turtle, Screen
import time
import random


def main():
    class Snake:
        def __init__(self):
            self.segments = []
            self.create_snake()
            self.distance = 20  # distance to move
            self.head = self.segments[0]

        def create_snake(self):
            for i in range(3):
                self.add_segment((0, i * -20))

        def move(self):
            for segment_number in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment_number - 1].xcor()
                new_y = self.segments[segment_number - 1].ycor()
                self.segments[segment_number].goto(new_x, new_y)

            self.head.forward(distance=self.distance)

        def up(self):
            if self.head.heading() != 270:
                self.head.setheading(90)

        def down(self):
            if self.head.heading() != 90:
                self.head.setheading(270)

        def left(self):
            if self.head.heading() != 0:
                self.head.setheading(180)

        def right(self):
            if self.head.heading() != 180:
                self.head.setheading(0)

        def extend(self):
            self.add_segment(self.segments[-1].position())

        def add_segment(self, position):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    class Food(Turtle):
        def __init__(self):
            super().__init__()
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color('blue')
            self.speed('fastest')
            self.refresh()

        def refresh(self):
            self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    class ScoreBoard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.hideturtle()
            self.penup()
            self.goto(0, 260)
            self.color('white')
            self.font = ('Arial', 24, 'normal')
            self.align = 'center'
            self.write(f'Score: {self.score}', align=self.align, font=self.font)

        def update_score(self):
            self.score += 1
            self.clear()
            self.write(f'Score: {self.score}', align=self.align, font=self.font)

        def game_over(self):
            self.goto(0, 0)
            self.write('GAME OVER', align='center', font=self.font)

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='w', fun=snake.up)

    screen.onkey(key='Down', fun=snake.down)
    screen.onkey(key='s', fun=snake.down)

    screen.onkey(key='Left' or 'a', fun=snake.left)
    screen.onkey(key='a', fun=snake.left)

    screen.onkey(key='Right', fun=snake.right)
    screen.onkey(key='d', fun=snake.right)

    game_on = True

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            score.update_score()
            snake.extend()
            food.refresh()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            score.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
