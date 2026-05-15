import customtkinter as ctk

# ---------------- SETTINGS ---------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ---------------- WINDOW ---------------- #
app = ctk.CTk()
app.geometry("900x500")
app.title("Modern Login UI")

# make window non-resizable
app.resizable(False, False)

# ---------------- LEFT FRAME ---------------- #
left_frame = ctk.CTkFrame(
    app,
    width=400,
    corner_radius=0
)
left_frame.pack(side="left", fill="y")

welcome = ctk.CTkLabel(
    left_frame,
    text="Welcome Back 👋",
    font=("Arial", 32, "bold"),
    text_color="#ff3c00"
)
welcome.place(x=70, y=120)

desc = ctk.CTkLabel(
    left_frame,
    text="Login to continue your journey\nwith Python GUI Development 🚀",
    font=("Arial", 16),
    justify="right"
)
desc.place(x=70, y=190)

# ---------------- RIGHT FRAME ---------------- #
right_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
right_frame.pack(side="right", expand=True)

title = ctk.CTkLabel(
    right_frame,
    text="Login",
    font=("Arial", 35, "bold")
)
title.pack(pady=(70, 30))

# ---------------- USERNAME ---------------- #
username = ctk.CTkEntry(
    right_frame,
    width=300,
    height=45,
    placeholder_text="Username",
    corner_radius=12,
    border_color="#007fff"
)
username.pack(pady=15)

# ---------------- PASSWORD ---------------- #
password = ctk.CTkEntry(
    right_frame,
    width=300,
    height=45,
    placeholder_text="Password",
    show="*",
    corner_radius=12,
    border_color="#007fff"
)
password.pack(pady=15)

# ---------------- LOGIN FUNCTION ---------------- #
def login():
    user = username.get()

    if user == "":
        status.configure(text="Please enter username!!")
    else:
        status.configure(text=f"Welcome {user} 😄!")

# ---------------- BUTTON ---------------- #
login_btn = ctk.CTkButton(
    right_frame,
    text="Login",
    width=300,
    height=45,
    corner_radius=25,
    font=("Arial", 16, "bold"),
    command=login,
    fg_color="#007fff",
    hover_color="#ff3c00"
)
login_btn.pack(pady=25)

# ---------------- STATUS LABEL ---------------- #
status = ctk.CTkLabel(
    right_frame,
    text="",
    font=("Arial", 14)
)
status.pack()

# ---------------- SIGNUP TEXT ---------------- #
signup = ctk.CTkLabel(
    right_frame,
    text="Don't have an account? Sign Up",
    font=("Arial", 13)
)
signup.pack(pady=25)

# ---------------- RUN ---------------- #
app.mainloop()

