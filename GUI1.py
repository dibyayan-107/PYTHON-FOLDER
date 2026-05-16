import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First GUI")
root.geometry("600x300")

# Function
def say_hello():
    label.config(text="Hello...this is my first GUI😄")

# Button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=20)

# Label
label = tk.Label(root, text="")
label.pack()

# Run app
root.mainloop()