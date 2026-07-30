import customtkinter as ctk

ctk.set_appearance_mode("Dark")

# Create window
root = ctk.CTk()
root.title("My First GUI")
root.geometry("400x400")
root.resizable(False, False)

#Function
def func1():
    if ent1.get() == "":
        status.configure(text="Please enter username!!")
    else:
        status.configure(text=f"Welcome {ent1.get()}😄!")
def func2():
    ent1.delete(0, "end")

labl1 = ctk.CTkLabel(
    master=root,
    text="Welcome to customtkinter!",
    font=("Helvetica",15),
    text_color="yellow",
    height=30
)
labl1.pack(pady = 10)

ent1 = ctk.CTkEntry(
   master=root,
   placeholder_text="Enter your name..",
   border_color="cyan",
   placeholder_text_color="cyan",
   corner_radius=50,
   width=200,
   height=40,
   text_color="cyan"
    )
ent1.pack(
    pady=20
    )

bu1 = ctk.CTkButton(
    master = root,
    text="Submit",
    fg_color="green",
    text_color="black",
    width=100,
    height=30,
    corner_radius=30,
    command=func1
)
bu1.pack(
    pady=10
    )

bu2 = ctk.CTkButton(
    master = root,
    text="Clear",
    fg_color="red",
    text_color="white",
    width=100,
    height=30,
    corner_radius=30,
    command=func2
)
bu2.pack(
    pady=10
    )
status = ctk.CTkLabel(
    master=root,
    text="",
    font=("Helvetica",15)
)
status.pack(
    pady=50
)
root.mainloop()