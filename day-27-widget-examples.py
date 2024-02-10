import tkinter as tk


def main():
    # Create a function that will be called when the button is clicked
    def button_clicked():
        label['text'] = input_entry.get()

    # Create a window and configure it
    window = tk.Tk()
    window.title('Widget Examples')
    window.minsize(width=500, height=300)
    window.config(padx=20, pady=20)

    # Create a label widget and configure it
    label = tk.Label(text='I am a label', font=('Arial', 24, 'bold'))
    label.pack()

    # Change the text of the label
    label['text'] = 'New Text'
    label.config(text='New Text')

    # Create a button widget and configure it
    button = tk.Button(text='Click Me', command=button_clicked)
    button.pack()

    # Create an entry widget and configure it
    input_entry = tk.Entry(width=10)
    input_entry.pack()

    # Create a text widget and configure it
    text = tk.Text(height=5, width=30)
    # Put cursor in the text widget
    text.focus()
    # Add some text to the text widget
    text.insert(tk.END, 'Example of text widget\n')
    # Get the current value in text widget at line 1, character 0
    print(text.get('1.0', tk.END))
    text.pack()

    # Create a spinbox widget and configure it
    def spinbox_used():
        print(spinbox.get())

    spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.pack()

    # Create a scale widget and configure it
    def scale_used(value):
        print(value)

    scale = tk.Scale(from_=0, to=100, command=scale_used)
    scale.pack()

    # Create a checkbutton widget and configure it
    def checkbutton_used():
        print(checked_state.get())  # 1 if checked, 0 if unchecked

    checked_state = tk.IntVar()
    checkbutton = tk.Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
    checked_state.set(0)  # Unchecked
    checkbutton.pack()

    # Create a radiobutton widget and configure it
    def radio_used():
        print(radio_state.get())  # 1 if checked, 0 if unchecked

    radio_state = tk.IntVar()
    radiobutton1 = tk.Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
    radiobutton2 = tk.Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)
    radiobutton1.pack()
    radiobutton2.pack()

    # Create a listbox widget and configure it
    def listbox_used(event):
        print(listbox.get(listbox.curselection()))  # Get the value of the selected item

    listbox = tk.Listbox(height=4)
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    for fruit in fruits:
        listbox.insert(fruits.index(fruit), fruit)
    listbox.bind('<<ListboxSelect>>', listbox_used)
    listbox.pack()

    # Start the application
    window.mainloop()


if __name__ == '__main__':
    main()
