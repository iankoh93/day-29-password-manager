from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_input.get()
    website = website_input.get()
    password = password_output.get()
    data_entry = website + "  |  " + email + "  |  " + password + "\n"
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"Theres are the details entered: \nEmail: {email}\nPassword: {password} \nIs it okay to "
                                                 f"save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(data_entry)
                website_input.delete(0, END)
                password_output.delete(0, END)
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# GUI Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# GUI Inputs/Outputs
website_input = Entry(width=51)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "ian_koh93@hotmail.com")

password_output = Entry(width=32)
password_output.grid(row=3, column=1)

# GUI Buttons
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=2)

window.mainloop()
