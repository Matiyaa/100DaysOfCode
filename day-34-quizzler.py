import html
import tkinter as tk

import requests


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = self.get_question()
        self.score = 0

    def get_question(self):
        API = "https://opentdb.com/api.php?amount=10&type=boolean"
        response = requests.get(API)
        response.raise_for_status()
        questions = response.json()["results"]

        question_bank = [Question(question["question"], question["correct_answer"]) for question in questions]
        return question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False): ")
        return html.unescape(current_question.text), current_question.answer
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


class QuizUI:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.theme = "#375362"
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=self.theme)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=self.theme)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=self.theme,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.current_question = ""
        self.current_answer = ""
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.current_question, self.current_answer = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"Q.{self.quiz.question_number}:{self.current_question}")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True", self.current_answer))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False", self.current_answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


def main():
    quiz = QuizBrain()
    quiz_ui = QuizUI(quiz)

    # Commented out to avoid text version running
    # while quiz.still_has_questions():
    #     quiz.next_question()
    #
    # print("You've completed the quiz")
    # print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == '__main__':
    main()
