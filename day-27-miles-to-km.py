import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Miles to Km Converter")
    window.minsize(width=220, height=100)
    window.config(padx=20, pady=20)

    miles = tk.Entry(width=10,
                     justify="center",
                     font=("Arial", 12, "normal"),
                     borderwidth=2,
                     relief="groove")
    miles.insert(0, "0")
    miles.grid(row=0, column=1)

    miles_label = tk.Label(text="Miles")
    miles_label.grid(row=0, column=2)

    equal_label = tk.Label(text="is equal to")
    equal_label.grid(row=1, column=0)

    km_label = tk.Label(text="Km")
    km_label.grid(row=1, column=2)

    km = tk.Label(text="0")
    km.grid(row=1, column=1)

    def calculate_km():
        miles_value = float(miles.get())
        km_value = miles_value * 1.609
        km.config(text=km_value)

    calculate_button = tk.Button(text="Calculate", command=calculate_km)
    calculate_button.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    main()
