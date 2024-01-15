def turn_right():
    turn_left()
    turn_left()
    turn_left()


def main():
    while front_is_clear():
        move()

    turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


if __name__ == "__main__":
    main()
