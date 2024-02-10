import tkinter as tk

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
repetitions = 0
timer = None


def main():
    # Timer reset
    def reset_timer():
        global repetitions
        repetitions = 0
        title_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        checkmark_label.config(text="")
        window.after_cancel(timer)

    # Timer mechanism
    def start_timer():
        global repetitions

        if repetitions % 2 == 0:
            count_down(WORK_MIN * 60)
            title_label.config(text="Work", fg=GREEN)
        elif repetitions % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="Break", fg=RED)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="Break", fg=PINK)
            checkmark_label.config(text=CHECKMARK * (repetitions // 2))
        repetitions += 1

    # Countdown mechanism
    def count_down(count):
        global timer
        count_min = count // 60
        count_sec = count % 60
        canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        else:
            window.bell()
            window.attributes("-topmost", True)
            start_timer()

    # UI setup
    window = tk.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    # Labels
    title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    title_label.grid(row=0, column=1)

    # Canvas
    canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tk.PhotoImage(file="day-28-tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    # Buttons
    start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.grid(row=2, column=0)
    reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
    reset_button.grid(row=2, column=2)

    # Checkmarks
    checkmark_label = tk.Label(fg=GREEN, bg=YELLOW)
    checkmark_label.grid(row=3, column=1)

    # Keep the window open
    window.mainloop()


if __name__ == "__main__":
    main()
