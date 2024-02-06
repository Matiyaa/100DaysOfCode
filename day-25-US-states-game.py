import turtle
import pandas


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    image = "day-25-blank_states_img.gif"
    states = open("day-25-50_states.csv")
    states_data = pandas.read_csv(states)

    screen.addshape(image)
    turtle.shape(image)

    screen.listen()
    # screen.onscreenclick(get_mouse_click_cord)
    correct_guesses = []

    while len(correct_guesses) < 50:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            state_to_learn = [state for state in states_data.state if state not in correct_guesses]
            new_data = pandas.DataFrame(state_to_learn)
            new_data.to_csv("day-25-states_to_learn.csv")
        if answer_state in states_data.values:
            correct_guesses.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states_data[states_data.state == answer_state]
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(answer_state)

# def get_mouse_click_cord(x, y):
#     print(x, y)


if __name__ == "__main__":
    main()
