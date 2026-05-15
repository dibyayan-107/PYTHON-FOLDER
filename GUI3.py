import customtkinter as ctk
#Setting
ctk.set_appearance_mode("dark")

#Window
app = ctk.CTk()
app.geometry("400x500")
app.title("My Webpage")

#Non-resizable window
app.resizable(False, False)

#Text
title = ctk.CTkLabel(
    app, 
    text="SIGN IN",
    font=("Arial", 30)
)
title.pack(pady=30)
#Input boxes
username = ctk.CTkEntry(
    app,
    placeholder_text="Username",
    text_color="White",
    border_color="light blue",
    corner_radius=20,
    width=300,
    height=45
)
username.pack(pady=10)

password = ctk.CTkEntry(
    app,
    placeholder_text="Password",
    text_color="White",
    border_color="light blue",
    corner_radius=20,
    width=300,
    height=45
)
password.pack(pady=10)
#Button
btn = ctk.CTkButton(
    app,
    text="Log in",
    fg_color="black",
    border_width=2,
    border_color="green",
    hover_color="green",
    corner_radius=20,
    width=150,
    height=45
)
btn.pack(pady=50)

#Run the program
app.mainloop()
