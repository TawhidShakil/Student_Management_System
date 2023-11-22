from tkinter import *
from tkinter import messagebox
import tkinter as tk
import regi
import database
import hashlib
from dashboard import moveToDash

def create_login_window():
    main_window = tk.Tk()
    main_window.geometry("1360x700+0+0")
    main_window.title("Login Frame -")

    def login():
        username = stringUser.get() # nadim
        password = hashlib.sha256(userPass.get().encode()).hexdigest()

        if stringUser.get() == "" or userPass.get() == "":
            messagebox.showwarning("Warning!", "Username or password is empty.")
        else:
            result = database.authentic_user(username, password)
            print(f"Authentication result: {result}")
            if result:
                messagebox.showinfo("Login Successful!!", "Welcome "+username)
                main_window.destroy()
                moveToDash()
            else:
                messagebox.showerror("Login failed!!", "Invalid UserName or Password")

    def signup():
        main_window.destroy()  # Close the login page
        main_window1 = regi.create_registration_window(create_login_window)
        main_window1.mainloop()

    frameDetail = tk.LabelFrame(master=main_window, bg="#001220", fg="lightgrey")
    frameDetail.place(x=700, y=70, width=500, height=575)

    loginTitle = tk.Label(main_window, text="Login ", font=("impact", 40), fg="lightgrey",bg="#001220")
    loginTitle.place(x=880, y=90)

    stringUser = StringVar()

    userName_lbl = tk.Label(main_window, text="User name : ", font=("Arial", 20), bg="#001220", fg="lightgrey")
    userName_lbl.place(x=705, y=225)

    userName_ent = tk.Entry(main_window, bd=5, font=("Arial", 20), textvariable=stringUser)
    userName_ent.place(x=870, y=225)

    userPass_lbl = tk.Label(main_window, text=" Password : ", font=("Arial", 20), bg="#001220", fg="lightgrey")
    userPass_lbl.place(x=705, y=320)

    userPass = tk.Entry(main_window, bd=5, font=("Arial", 20), show='*')
    userPass.place(x=870, y=320)

    enterButton = tk.Button(main_window, text=" Enter ", font=("impact", 16), bd=6, fg="lightgrey", bg="green", command=login)
    enterButton.place(x=940, y=405, width=160)

    signUp = tk.Label(main_window, text="For Create a new account click here: ", font=("Arial", 10), bg="#001220", fg="lightgrey")
    signUp.place(x=800, y=500)

    signUpButton = tk.Button(main_window, text="Sign-up", font=("impact", 8), bg="yellow", command=signup)
    signUpButton.place(x=1020, y=500)

    image1 = tk.PhotoImage(file="C:\\Users\\ACER i3 LAPTOP\\Pictures\\image_for_OOP\\aa.png")
    l1 = Label(main_window, image=image1)
    l1.place(x=60, y=50, width=600, height=600)

    main_window.mainloop()

# Uncomment the following line to create the login window
create_login_window()
