# # from tkinter import *
# # from tkinter import messagebox
# # import tkinter as tk

# # def create_registration_window():
# #     main_window1 = tk.Tk()
# #     main_window1.geometry("1260x700+0+0")
# #     main_window1.title("Registration Form")
# #     main_window1.configure(bg="#FFB6C1")

# #     def register():
# #         if (
# #             stringUsername.get() == ""
# #             or stringPassword.get() == ""
# #             or stringConfirmPassword.get() == ""
# #         ):
# #             messagebox.showwarning("Warning!", "All fields are required.")
# #         elif stringPassword.get() != stringConfirmPassword.get():
# #             messagebox.showwarning("Warning!", "Passwords do not match.")
# #         else:
# #             username = stringUsername.get()
# #             password = stringPassword.get()
# #             print(f"Registration Successful:\nUsername: {username}\nPassword: {password}")
# #             messagebox.showinfo("Successful", "Registration successful.")
# #             main_window1.destroy()

# #     frameDetail = tk.LabelFrame(master=main_window1, bg="#FFFFFF", fg="lightgrey")
# #     frameDetail.place(x=60, y=60, width=1140, height=575)

# #     registrationTitle = tk.Label(main_window1, text="Registration", font=("Comic Sans MS", 25), fg="black", bg="white")
# #     registrationTitle.place(x=130, y=120)

# #     stringUsername = StringVar()
# #     stringPassword = StringVar()
# #     stringConfirmPassword = StringVar()

# #     username_lbl = tk.Label(main_window1, text="Username:", font=("Arial", 20), bg="white", fg="black")
# #     username_lbl.place(x=130, y=220)

# #     username_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), textvariable=stringUsername)
# #     username_ent.place(x=130, y=260, width=500)

# #     password_lbl = tk.Label(main_window1, text="Password:", font=("Arial", 20), bg="white", fg="black")
# #     password_lbl.place(x=130, y=320)

# #     password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringPassword)
# #     password_ent.place(x=130, y=355, width=500)

# #     confirm_password_lbl = tk.Label(main_window1, text="Confirm Password:", font=("Arial", 20), bg="white", fg="black")
# #     confirm_password_lbl.place(x=130, y=415)

# #     confirm_password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringConfirmPassword)
# #     confirm_password_ent.place(x=130, y=450, width=500)

# #     registerButton = tk.Button(main_window1, text="Register", font=("impact", 16), bd=3, fg="white", bg="red", command=register)
# #     registerButton.place(x=130, y=520, width=250)

# #     main_window1.mainloop()



# from tkinter import *
# from tkinter import messagebox
# import hashlib
# import database
# import tkinter as tk
# from loginF import create_login_window

# def create_registration_window(on_registration_success):
#     main_window1 = tk.Tk()
#     main_window1.geometry("1260x700+0+0")
#     main_window1.title("Registration Form")
#     main_window1.configure(bg="#FFB6C1")

#     def register():
#         if (
#             stringUsername.get() == ""
#             or stringPassword.get() == ""
#             or stringConfirmPassword.get() == ""
#         ):
#             messagebox.showwarning("Warning!", "All fields are required.")
#         elif stringPassword.get() != stringConfirmPassword.get():
#             messagebox.showwarning("Warning!", "Passwords do not match.")
#         else:
#             username = stringUsername.get()
#             password = hashlib.sha256(stringPassword.get().encode()).hexdigest()
#             print(f"Username: {username}, Password (hashed): {password}")
#             database.insert_user(username, password)
#             messagebox.showinfo("Successful", "Registration successful.")
#             main_window1.destroy()
#             on_registration_success()


#     frameDetail = tk.LabelFrame(master=main_window1, bg="#FFFFFF", fg="lightgrey")
#     frameDetail.place(x=60, y=60, width=1140, height=575)

#     registrationTitle = tk.Label(main_window1, text="Registration", font=("Comic Sans MS", 25), fg="black", bg="white")
#     registrationTitle.place(x=130, y=120)

#     stringUsername = StringVar()
#     stringPassword = StringVar()
#     stringConfirmPassword = StringVar()

#     username_lbl = tk.Label(main_window1, text="Username:", font=("Arial", 20), bg="white", fg="black")
#     username_lbl.place(x=130, y=220)

#     username_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), textvariable=stringUsername)
#     username_ent.place(x=130, y=260, width=500)

#     password_lbl = tk.Label(main_window1, text="Password:", font=("Arial", 20), bg="white", fg="black")
#     password_lbl.place(x=130, y=320)

#     password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringPassword)
#     password_ent.place(x=130, y=355, width=500)

#     confirm_password_lbl = tk.Label(main_window1, text="Confirm Password:", font=("Arial", 20), bg="white", fg="black")
#     confirm_password_lbl.place(x=130, y=415)

#     confirm_password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringConfirmPassword)
#     confirm_password_ent.place(x=130, y=450, width=500)

#     registerButton = tk.Button(main_window1, text="Register", font=("impact", 16), bd=3, fg="white", bg="red", command=register)
#     registerButton.place(x=130, y=520, width=250)

#     main_window1.mainloop()

#     return main_window1


from tkinter import *
from tkinter import messagebox
import tkinter as tk
import database
import hashlib

def create_registration_window(on_registration_success):
    main_window1 = tk.Tk()
    main_window1.geometry("1260x700+0+0")
    main_window1.title("Registration Form")
    main_window1.configure(bg="#FFB6C1")

    def register():
        if (
            stringUsername.get() == ""
            or stringPassword.get() == ""
            or stringConfirmPassword.get() == ""
        ):
            messagebox.showwarning("Warning!", "All fields are required.")
        elif stringPassword.get() != stringConfirmPassword.get():
            messagebox.showwarning("Warning!", "Passwords do not match.")
        else:
            username = stringUsername.get()
            password = hashlib.sha256(stringPassword.get().encode()).hexdigest()
            print(f"Username: {username}, Password (hashed): {password}")
            database.insert_user(username, password)
            messagebox.showinfo("Successful", "Registration successful.")
            main_window1.destroy()
            on_registration_success()

    frameDetail = tk.LabelFrame(master=main_window1, bg="#FFFFFF", fg="lightgrey")
    frameDetail.place(x=60, y=60, width=1140, height=575)

    registrationTitle = tk.Label(main_window1, text="Registration", font=("Comic Sans MS", 25), fg="black", bg="white")
    registrationTitle.place(x=130, y=120)

    stringUsername = StringVar()
    stringPassword = StringVar()
    stringConfirmPassword = StringVar()

    username_lbl = tk.Label(main_window1, text="Username:", font=("Arial", 20), bg="white", fg="black")
    username_lbl.place(x=130, y=220)

    username_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), textvariable=stringUsername)
    username_ent.place(x=130, y=260, width=500)

    password_lbl = tk.Label(main_window1, text="Password:", font=("Arial", 20), bg="white", fg="black")
    password_lbl.place(x=130, y=320)

    password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringPassword)
    password_ent.place(x=130, y=355, width=500)

    confirm_password_lbl = tk.Label(main_window1, text="Confirm Password:", font=("Arial", 20), bg="white", fg="black")
    confirm_password_lbl.place(x=130, y=415)

    confirm_password_ent = tk.Entry(main_window1, bd=2, font=("Arial", 20), show='*', textvariable=stringConfirmPassword)
    confirm_password_ent.place(x=130, y=450, width=500)

    registerButton = tk.Button(main_window1, text="Register", font=("impact", 16), bd=3, fg="white", bg="red", command=register)
    registerButton.place(x=130, y=520, width=250)
    
    # add image
    image = PhotoImage(file="C:\\Users\\ACER i3 LAPTOP\\Pictures\\image_for_OOP\\aa.png")
    image_label = tk.Label(main_window1, image=image, bg="white")
    image_label.image = image
    image_label.place(x=650,y=120,width=500,height=450)

    main_window1.mainloop()
