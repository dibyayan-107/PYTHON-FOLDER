# Modern Calculator App using CustomTkinter

import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("My Calculator")
app.geometry("350x500")
app.resizable(False, False)

# Variable
expression = ""

# Entry Box
entry = ctk.CTkEntry(
    app,
    width=320,
    height=60,
    border_width=2,
    border_color="cyan",
    font=("Arial", 28),
    justify="right"
)
entry.pack(pady=20)


# Functions
def press(value):
    global expression
    expression += str(value)
    entry.delete(0, "end")
    entry.insert("end", expression)


def clear():
    global expression
    expression = ""
    entry.delete(0, "end")


def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, "end")
        entry.insert("end", result)
        expression = result
    except:
        entry.delete(0, "end")
        entry.insert("end", "Error")
        expression = ""


# Button Frame
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

# Buttons Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create Buttons
for row in buttons:
    row_frame = ctk.CTkFrame(frame, fg_color="transparent")
    row_frame.pack(pady=5)

    for button in row:
        if button == "=":
            cmd = calculate
        else:
            cmd = lambda x=button: press(x)

        btn = ctk.CTkButton(
            row_frame,
            text=button,
            fg_color="blue",
            width=70, 
            height=60,
            font=("Arial", 22),
            border_width=2,
            border_color="yellow",
            command=cmd
        )
        btn.pack(side="left", padx=5)

# Clear Button
clear_btn = ctk.CTkButton(
    app,
    text="Clear",
    width=320,
    height=50,
    font=("Arial", 22),
    fg_color="red",
    hover_color="darkred",
    command=clear
)
clear_btn.pack(pady=15)

# Run App
app.mainloop()