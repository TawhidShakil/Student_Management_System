from tkinter import *
from tkinter import messagebox
import tkinter as tk

def switch_to_login_frame():
    frameRegister.place_forget()
    frameLogin.place(x=700, y=70, width=500, height=575)

def switch_to_register_frame():
    frameLogin.place_forget()
    frameRegister.place(x=700, y=70, width=500, height=575)

def login():
    if stringUser.get() == "" or stringPassword.get() == "":
        messagebox.showwarning("Warning!", "Username or password is empty.")
    else:
        messagebox.showinfo("Successful", "Welcome, " + stringUser.get())
        # Add logic to move to the main application window or perform other actions.

def signup():
    switch_to_register_frame()

def register():
    if (
        stringUsername.get() == ""
        or stringPassword.get() == ""
        or stringConfirmPassword.get() == ""
    ):
        messagebox.showwarning("Warning!", "Potential fields are required.")
    elif stringPassword.get() != stringConfirmPassword.get():
        messagebox.showwarning("Warning!", "Passwords do not match.")
    else:
        username = stringUsername.get()
        password = stringPassword.get()
        print(f"Registration Successful:\nUsername: {username}\nPassword: {password}")
        messagebox.showinfo("Successful", "Registration successful.")
        switch_to_login_frame()

def sign_in():
    messagebox.showinfo("Sign-In", "Sign-In functionality goes here.")
    # Add logic to move to the main application window or perform other actions.

main_window = tk.Tk()
main_window.geometry("1360x700+0+0")
main_window.title("Login Frame -")

# Login Frame
frameLogin = tk.LabelFrame(master=main_window, bg="#001220", fg="lightgrey")
frameLogin.place(x=700, y=70, width=500, height=575)

loginTitle = tk.Label(main_window, text="Login ", font=("impact", 40), fg="lightgrey", bg="#001220")
loginTitle.place(x=880, y=90)

stringUser = StringVar()


# ... (rest of the login frame code)

enterButton = tk.Button(main_window, text=" Enter ", font=("impact", 16), bd=6, fg="lightgrey", bg="green", command=login)
enterButton.place(x=940, y=405, width=160)

signUpButton = tk.Button(main_window, text="Sign-up", font=("impact", 8), bg="yellow", command=signup)
signUpButton.place(x=1020, y=500)

# Register Frame
frameRegister = tk.LabelFrame(master=main_window, bg="#FFB6C1", fg="lightgrey")
frameRegister.place_forget()

registrationTitle = tk.Label(main_window, text="Registration", font=("Comic Sans MS", 25), fg="black", bg="#FFB6C1")
registrationTitle.place(x=130, y=120)

stringUsername = StringVar()
stringPassword = StringVar()
stringConfirmPassword = StringVar()

# ... (rest of the register frame code)

registerButton = tk.Button(main_window, text="Register", font=("impact", 16), bd=3, fg="white", bg="red", command=register)
registerButton.place(x=130, y=520, width=250)

sign_inButton = tk.Button(main_window, text="Sign-In", font=("impact", 16), fg="white", bg="black", command=sign_in)
sign_inButton.place(x=400, y=520, width=230)

# ... (rest of the main window code)

main_window.mainloop()
