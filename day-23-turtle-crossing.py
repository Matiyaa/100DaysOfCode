from turtle import Screen, Turtle
from time import sleep
from random import randint, choice


def main():
    class CarManager(Turtle):
        def __init__(self):
            super().__init__()
            self.x_move = -10
            self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
            self.all_cars = []

        def create_car(self, amount=1):
            for _ in range(0, amount):
                new_car = Turtle("square")
                new_car.color(choice(self.colors))
                new_car.penup()
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.goto(randint(-290, 290), randint(-250, 250))
                self.all_cars.append(new_car)

        def move(self):
            for car in self.all_cars:
                car.goto(car.xcor() + self.x_move, car.ycor())
                if car.xcor() <= -300:
                    car.goto(300, car.ycor())

        def speed_up(self):
            self.x_move *= 1.1

    class Player(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("turtle")
            self.color("white")
            self.penup()
            self.goto(0, -280)
            self.setheading(90)

        def move_up(self):
            self.forward(10)

        def move_left(self):
            self.setheading(180)
            self.forward(10)
            self.setheading(90)

        def move_right(self):
            self.setheading(0)
            self.forward(10)
            self.setheading(90)

        def reset(self):
            self.goto(0, -280)

    class ScoreBoard(Turtle):
        def __init__(self):
            super().__init__()
            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(0, 260)
            self.score = 1
            self.font = ("Courier", 24, "normal")
            self.align = "center"
            self.update()

        def update(self):
            self.clear()
            self.write(f"Level: {self.score}", align=self.align, font=self.font)

        def increase(self):
            self.score += 1
            self.update()

        def game_over(self):
            self.goto(0, 0)
            self.write("GAME OVER", align=self.align, font=self.font)

    def check_collision(cars, player):
        for car in cars:
            if car.distance(player) <= 20:
                return True
        return False

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Turtle Crossing")
    screen.bgcolor("black")
    screen.listen()

    player = Player()
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkey(screen.bye, "Escape")

    scoreboard = ScoreBoard()

    car_manager = CarManager()

    car_manager.create_car(20)

    cars = car_manager.all_cars

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()

        if player.ycor() > 280:
            player.reset()
            scoreboard.increase()
            car_manager.speed_up()
            car_manager.create_car(scoreboard.score)

        if check_collision(cars, player):
            game_is_on = False
            scoreboard.game_over()

        car_manager.move()

    screen.exitonclick()


if __name__ == '__main__':
    main()
