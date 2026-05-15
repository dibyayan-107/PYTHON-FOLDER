import customtkinter as ctk
import webbrowser

# Function to open the URL
def open_link(event=None):
    try:
        webbrowser.open_new_tab("https://www.python.org")
    except Exception as e:
        print(f"Error opening link: {e}")

# Create the main window
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Clickable Link Example")
app.geometry("300x150")

# Create a clickable label
link_label = ctk.CTkLabel(
    app,
    text="Visit Python.org",
    text_color="blue",  # Make it look like a hyperlink
    cursor="hand2"      # Change cursor on hover
)
link_label.pack(pady=40)

# Bind left mouse click to open the link
link_label.bind("<Button-1>", open_link)

app.mainloop()
