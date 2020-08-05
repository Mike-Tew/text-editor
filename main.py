from tkinter import Tk, Label, Button, Text, Frame, LEFT, END
from tkinter import filedialog


def save():
    # Save the text to a local directory
    editor_text = editor.get("1.0", "end-1c")
    text_file = filedialog.askopenfilename(
        initialdir="C:/", title="Save Text File", filetypes=(("Text Files", "*.txt"),)
    )
    with open(text_file, "w") as open_file:
        open_file.write(editor_text)


def open_func():
    # Open selected file and display it in the text area
    text_file = filedialog.askopenfilename(
        initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"),)
    )
    with open(text_file, "r") as open_file:
        file_text = open_file.read()

    editor.insert(END, file_text)


def close():
    root.destroy()


root = Tk()
root.title("Text Editor")
root.geometry("1000x700")

# Text Editor Label
Label(root, text="Text Editor", font="Helvetica 20 bold").pack(pady=20)

# Main Text Box
editor = Text(root, height=30, width=100, bd=3)
editor.pack()

# Button Frame
button_frame = Frame(root)
button_frame.pack()

# Open Button
Button(
    button_frame,
    text="OPEN",
    height=2,
    width=15,
    font="Helvetica 15 bold",
    bd=3,
    command=open_func,
).pack(pady=20, padx=20, side=LEFT)

# Save Button
Button(
    button_frame,
    text="SAVE",
    height=2,
    width=15,
    font="Helvetica 15 bold",
    bd=3,
    command=save,
).pack(pady=20, padx=20, side=LEFT)

# Close Button
Button(
    button_frame,
    text="CLOSE",
    height=2,
    width=15,
    font="Helvetica 15 bold",
    bd=3,
    command=close,
).pack(pady=20, padx=20, side=LEFT)

root.mainloop()
