import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x400")

title = ctk.CTkLabel(master=app, text="Login System", font=("Arial", 24))
title.pack(pady=30)

username = ctk.CTkEntry(master=app, placeholder_text="Username")
username.pack(pady=20)

password = ctk.CTkEntry(master=app, placeholder_text="Password", show="*")
password.pack(pady=10)

def login():
       
       user = username.get()
       print(f"Welcome {user}")

btn = ctk.CTkButton(master=app, text="Login", command=login, fg_color="red", hover_color="green",corner_radius=20)
btn.pack(pady=20)

app.mainloop()