import os.path
import random
import tkinter as tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
if os.path.exists("day-31-data/words_to_learn.csv"):
    word_data_df = pd.read_csv("day-31-data/words_to_learn.csv")
else:
    word_data_df = pd.read_csv("day-31-data/japanese_words - words.csv")
to_learn = word_data_df.to_dict(orient="records")
word = {}


def main():
    window = tk.Tk()
    window.title("Flashcard App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.minsize(width=900, height=600)

    def next_card():
        global word
        word = random.choice(to_learn)
        canvas.itemconfig(card_title, text="Japanese", fill="black")
        canvas.itemconfig(card_word, text=word['Japanese'], fill="black")
        canvas.itemconfig(card_background, image=card_front_image)
        window.after(5000, flip_card)

    def flip_card():
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=word['English'], fill="white")
        canvas.itemconfig(card_background, image=card_back_image)

    def yay_card():
        to_learn.remove(word)
        word_data = pd.DataFrame(to_learn)
        word_data.to_csv("day-31-data/words_to_learn.csv", index=False)
        next_card()

    canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)
    card_front_image = tk.PhotoImage(file="day-31-data/card_front.png")
    card_back_image = tk.PhotoImage(file="day-31-data/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_image)
    card_title = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
    card_word = canvas.create_text(400, 263, text='word', font=("Arial", 60, "bold"))

    next_card()

    nay_button = tk.PhotoImage(file="day-31-data/wrong.png")
    nay_button_label = tk.Button(image=nay_button, highlightthickness=0, command=next_card)
    nay_button_label.grid(row=3, column=0)
    nay_button_label.config(padx=50, pady=50)

    yay_button = tk.PhotoImage(file="day-31-data/right.png")
    yay_button_label = tk.Button(image=yay_button, highlightthickness=0, command=yay_card)
    yay_button_label.grid(row=3, column=1)
    yay_button_label.config(padx=50, pady=50)

    window.mainloop()


if __name__ == "__main__":
    main()
