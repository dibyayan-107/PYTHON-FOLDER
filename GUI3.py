import customtkinter as ctk
import webbrowser
#--------Setting
ctk.set_appearance_mode("dark")

#--------Window
app = ctk.CTk()
app.geometry("400x500")
app.title("My Webpage")

#--------Function
def link(event = None):
    try:
        webbrowser.open_new_tab("https://www.bing.com")
    except Exception as e:
        print(f"Error opening link: {e}")

def login():
    user = username.get()
    if user == "":
        status.configure(text="Please enter username!!")
    else:
        status.configure(text=f"Welcome {user} 😄!")


#---------Non-resizable window
app.resizable(False, False)

#--------Text
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
    height=45,
)
username.pack(pady=10)

password = ctk.CTkEntry(
    app,
    placeholder_text="Password",
    text_color="White",
    border_color="light blue",
    corner_radius=20,
    show="*",
    width=300,
    height=45
)
password.pack(pady=20)
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
    height=45,
    command=login
)
btn.pack(pady=50)
#--------text
text = ctk.CTkLabel(
    app,
    text="Don't have an account? Sign Up.",
    font=("Arial",14),
    text_color="light blue",
    cursor="hand2"
)
text.pack(pady=30)

status = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14)
)
status.pack()
text.bind("<Button-1>", link)
#Run the program
app.mainloop()
