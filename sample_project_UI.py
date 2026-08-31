import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Library Management System")
app.geometry("600x650")
app.resizable(False, False)
title = ctk.CTkLabel(
    app,
    text="📚 Library Management System",
    font=("Arial",28,"bold")
)

title.pack(pady=20)

library = {}
#------------------Function-------------------------
def save_book():

    book_id = id_entry.get()

    title = title_entry.get()

    author = author_entry.get()

    quantity = int(quantity_entry.get())

    library[book_id] = {
        "title": title,
        "author": author,
        "quantity": quantity,
        "max_quantity": quantity
    }
def clear():
    id_entry.delete(0, "end")
    title_entry.delete(0, "end")
    author_entry.delete(0, "end")
    quantity_entry.delete(0, "end")
#--------------FRAME1------------------------------
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

add_btn = ctk.CTkButton(
    button_frame,
    text="Add Book"
)

add_btn.grid(row=0,column=0,padx=10,pady=10)

delete_btn = ctk.CTkButton(
    button_frame,
    text="Delete Book"
)

delete_btn.grid(row=0,column=1,padx=10,pady=10)

issue_btn = ctk.CTkButton(
    button_frame,
    text="Issue Book"
)

issue_btn.grid(row=1,column=0,padx=10,pady=10)

return_btn = ctk.CTkButton(
    button_frame,
    text="Return Book"
)

return_btn.grid(row=1,column=1,padx=10,pady=10)

search_btn = ctk.CTkButton(
    button_frame,
    text="Search Book"
)

search_btn.grid(row=2,column=0,padx=10,pady=10)

display_btn = ctk.CTkButton(
    button_frame,
    text="Display Books"
)

display_btn.grid(row=2,column=1,padx=10,pady=10)

#--------------FRAME2------------------------------

form = ctk.CTkFrame(
    app,
    border_width=3,
    border_color="#427bb8"
    )
    
form.pack(
    pady=20,
    ipadx=50,
    ipady= 150,
    )

id_entry = ctk.CTkEntry(
    form,
    placeholder_text="Enter Book ID",
    corner_radius=50,
    width=200,
    height=40,
    )
id_entry.pack(pady=18)

title_entry = ctk.CTkEntry(
    form,
    placeholder_text="Enter Book Title",
    corner_radius=50,
    width=200,
    height=40,
    )
title_entry.pack(pady=8)

author_entry = ctk.CTkEntry(
    form,
    placeholder_text="Enter Author",
    corner_radius=50,
    width=200,
    height=40,
    )
author_entry.pack(pady=8)

quantity_entry = ctk.CTkEntry(
    form,
    placeholder_text="Enter Quantity",
    corner_radius=50,
    width=200,
    height=40,
    )
quantity_entry.pack(pady=8)

save_btn = ctk.CTkButton(
    form,
    text="Save Book",
    fg_color="green"
)

save_btn.pack(pady=15)

clear_btn = ctk.CTkButton(
    form,
    text="Clear All",
    fg_color="Red",
    command=clear
)
clear_btn.pack(pady=5)

print(library)
save_btn.configure(command=save_book)
app.mainloop()