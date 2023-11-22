import tkinter as tk
from tkinter import ttk, END
from tkinter import messagebox
from reportlab.pdfgen import canvas
import database
import re
from datetime import datetime
from validation import is_valid_roll, is_valid_name, is_valid_email, is_valid_phone, is_valid_date

# def is_valid_roll(roll_number):
#     return roll_number.replace("-", "").isdigit()

# def is_valid_name(name):
#     return all(c.isalpha() or c.isspace() or c in ["'", ".", "-"] for c in name) and name.strip() != ""


# def is_valid_email(email):
#     email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     return re.match(email_pattern, email) is not None

# def is_valid_phone(phone):
#     phone_pattern = r'^\d{11}$'
#     return re.match(phone_pattern, phone) is not None

# def is_valid_date(dob):
#     try:
#         datetime.strptime(dob, '%d-%m-%y')
#         return True
#     except ValueError:
#         return False

valid_departments = ("Software Engineering", "SWE", "CSE", "Computer Science")

def moveToDash():
    
    def addData():
        print("Add button succ")
        try:
            if not is_valid_roll(ent_rollNo.get()):
                messagebox.showinfo("Invalid Roll Number", "Enter the correct roll number")
            elif not is_valid_name(ent_fullName.get()):
                messagebox.showerror("Invalid Name!!", "Please Enter Correct Name")
            elif not is_valid_email(ent_email.get()):
                messagebox.showerror("Invalid E-mail!!", "Please enter a valid E-mail....")
            elif not is_valid_date(ent_dateOfBirth.get()):
                messagebox.showerror("Invalid Date format!!", "dd-mm-yy follow this format...")
            elif not is_valid_phone(ent_phone.get()):
                messagebox.showerror("Invalid Phone number!!", "Please enter the correct number...")
            elif ent_department.get() not in valid_departments:
                messagebox.showinfo("Invalid Department", "Enter a valid department")
            elif ent_rollNo.get() == "" or ent_fullName.get() == "" or ent_email.get() == "":
                messagebox.showinfo("Invalid data!!", "Please enter correct data")
            else:
                existing_records = [(student_table.item(item)['values'][0]) for item in student_table.get_children()]
                if ent_rollNo.get() in existing_records:
                    messagebox.showinfo("Duplicate Record", "Student with this ID already exists. Use the Update button to modify the record.")
                    #updateData()
                else:
                    database.addStudentInfo(
                        ent_rollNo.get(),
                        ent_fullName.get(),
                        ent_email.get(),
                        ent_phone.get(),
                        ent_gender.get(),
                        ent_dateOfBirth.get(),
                        ent_department.get()
                    )

                    new_record = (
                        ent_rollNo.get(),
                        ent_fullName.get(),
                        ent_email.get(),
                        ent_phone.get(),
                        ent_gender.get(),
                        ent_dateOfBirth.get(),
                        ent_department.get()
                    )

                    student_table.insert("", END, values=new_record)
                    messagebox.showinfo("Information Added Successfully...")
        except Exception as e:
            print(f"Error in addData: {e}")
            displayData()


    # UPDATE Button implement
    def updateData():
        try:
            selectedItem = student_table.selection()[0]
            studentId = student_table.item(selectedItem, 'values')[0]
            print("Selected Item:", selectedItem)
            print("Student ID: ", studentId)
            print("New Data:", ent_rollNo.get(), ent_fullName.get(), ent_email.get(), ent_phone.get(), ent_gender.get(), ent_dateOfBirth.get(), ent_department.get())

            database.updateStudentInfo(
                studentId,
                ent_rollNo.get(),
                ent_fullName.get(),
                ent_email.get(),
                ent_phone.get(),
                ent_gender.get(),
                ent_dateOfBirth.get(),
                ent_department.get()
            )

            # Update the data in the Treeview
            updated_data = (
                ent_rollNo.get(),
                ent_fullName.get(),
                ent_email.get(),
                ent_phone.get(),
                ent_gender.get(),
                ent_dateOfBirth.get(),
                ent_department.get()
            )
            student_table.item(selectedItem, values=updated_data)
            messagebox.showinfo("Information Updated Successfully...")
        except IndexError:
            messagebox.showerror("Error!!", "Please select a record to update...")


    # display Student information
    def displayData():
        try:
            result = database.displayInfo()
            student_table.delete(*student_table.get_children()) 
            if len(result) != 0:
                for row in result:
                    # Ensure the order of values matches the order of columns in Treeview
                    student_table.insert('', END, values=row[1:])
        except Exception as e:
            print(f"Error in displayData: {e}")





    # display Student information
    def studentRec(event):
        global sd
        clearData()
        veiwInfo = student_table.focus()
        lenearData = student_table.item(veiwInfo)
        sd = lenearData['values']

        ent_rollNo.insert(END, sd[0])
        ent_fullName.insert(END, sd[1])
        ent_email.insert(END, sd[2])
        ent_phone.insert(END, sd[3])
        ent_gender.set(sd[4])
        ent_dateOfBirth.insert(END, sd[5])
        ent_department.insert(END, sd[6])
        
    # ADD  Method End
    # DISPLAY methd start
    def displayData():
        try:
            result = database.displayInfo()
            student_table.delete(*student_table.get_children()) 
            if len(result) != 0:
                for row in result:
                    # Exclude the first element (ID) from the row before inserting into Treeview
                    student_table.insert('', END, values=row[1:])
        except Exception as e:
            print(f"Error in displayData: {e}")

    #End Display method

    # DELETE BUTTON start
    def deleteData():
        try:
            selectedItem = student_table.selection()[0]
            studentId = student_table.item(selectedItem, 'values')[0]

            # Ask for confirmation before deleting
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
            
            if confirm:
                database.deleteStudentInfo(studentId)
                student_table.delete(selectedItem)
                
                messagebox.showinfo("Record Deleted", "Student record deleted successfully.")
        except IndexError:
            messagebox.showerror("Error!!", "Please select a record to delete...")


    # DELETE BUTTON end

    # CLEAR BUTTON Start
    def clearData():
        ent_rollNo.delete(0, END)
        ent_fullName.delete(0, END)
        ent_email.delete(0, END)
        ent_phone.delete(0, END)
        ent_gender.set('')
        ent_dateOfBirth.delete(0, END)
        ent_department.delete(0, END)
    # End CLEAR BUTTON
    # Start PRINT BUTTON
    def pdfGenerate():
        try:
            result = database.displayInfo()
            if len(result) == 0:
                messagebox.showinfo("No Data", "No Records to print")
                return
            
            pdf_fileName = "student_records.pdf"
            pdf = canvas.Canvas(pdf_fileName)
            pdf.setTitle("Student Records")

            # set the column widths
            column_widths = [100,100,100,100,100,100,100]

            # set the header row
            header = ["Id No.", "Name", "E-mail", "Phone", "Gender", "D.O.B", "Department"]
            for i, text in enumerate(header):
                pdf.drawString(sum(column_widths[:i]) + 10, 800, text)

            # draw the student records
            y_position = 780
            for row in result:
                for i, value in enumerate(row):
                    pdf.drawString(sum(column_widths[:i]) + 10, y_position, str(value))
                y_position -= 20
            pdf.save()
            messagebox.showinfo("PDF Generated", f"Student records saved as {pdf_fileName}")
        except Exception as e:
            messagebox.showerror("ERROR!!", f"Error generating PDF: {e}")


    #END PRINT BUTTON

    window = tk.Tk()
    window.geometry("1350x700+0+0")
    window.title("Student Management System")
    #create a label for heading
    lbl_heading = tk.Label(
        master= window, 
        text="Student Mangement System",
        font=("Helvetica", 30, "bold"),
        border=10, relief=tk.GROOVE,
        bg= "lightgrey"
    )
    lbl_heading.pack(side=tk.TOP, fill=tk.X)

    # create a details frame
    frm_detail = tk.LabelFrame(
        master= window,
        text = "Enter Details",
        font = ("Helvetica", 20), 
        border=10, relief=tk.GROOVE, 
        bg="lightgrey"

    )

    frm_detail.place(x = 20, y =90, width=420, height=575)
    frm_data = tk.Frame(
        master=window,
        bd = 12, bg = "lightgrey", relief=tk.GROOVE
    )

    frm_data.place(x = 475, y = 90, width=810, height=575)

    # ========= Entry =======

    #label for roll num
    lbl_rollNo = tk.Label(
        master= frm_detail,
        text="ID No",
        font=("Helvetica", 18), 
        bg="lightgrey"
    )
    lbl_rollNo.grid(row=0, column=0, padx=2, pady=2)

    # create a entry box for roll no
    ent_rollNo = tk.Entry(
        master=frm_detail,
        bd= 5,
        width=20,
        font=("Helvetica", 12)
    )

    ent_rollNo.grid(row= 0, column=1, padx=2, pady=2)


    #label for Full name
    lbl_fullName = tk.Label(master=frm_detail, text="Name", font=("Helvetica", 18), bg="lightgrey")
    lbl_fullName.grid(row=1, column=0, padx=2 , pady=2)

    ent_fullName = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
    ent_fullName.grid(row=1, column=1, padx=2, pady=2)

    # label for e-mail
    lbl_email = tk.Label(master=frm_detail, text="E-mail", font=("Helvetica", 18), bg="lightgrey")
    lbl_email.grid(row=2, column=0, padx=2 , pady=2)

    ent_email = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
    ent_email.grid(row=2, column=1, padx=2, pady=2)

    # label for gender
    lbl_gender = tk.Label(master=frm_detail, text="Gender", font=("Helvetica", 18), bg="lightgrey")
    lbl_gender.grid(row=3, column=0, padx=2 , pady=2)

    ent_gender = ttk.Combobox(master=frm_detail, font=("Helvetica", 12), state="readonly")
    ent_gender['values'] = ("Male", "Female", "Others")
    ent_gender.grid(row=3, column=1, padx=2, pady=2)

    #label for date of birth
    lbl_dateOfBirth = tk.Label(master=frm_detail, text="D.O.B", font=("Helvetica", 18), bg="lightgrey")
    lbl_dateOfBirth.grid(row=4, column=0, padx=2 , pady=2)

    ent_dateOfBirth = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12) )
    ent_dateOfBirth.grid(row=4, column=1, padx=2, pady=2)

    # label for phone number
    lbl_phone = tk.Label(master=frm_detail, text="Phone", font=("Helvetica", 18), bg="lightgrey")
    lbl_phone.grid(row=5, column=0, padx=2 , pady=2)

    ent_phone = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12) )
    ent_phone.grid(row=5, column=1, padx=2, pady=2)

    #label for department 
    lbl_department = tk.Label(master=frm_detail, text="Department", font=("Helvetica", 18), bg="lightgrey")
    lbl_department.grid(row=6, column=0, padx=2 , pady=2)

    ent_department = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
    ent_department.grid(row=6, column=1, padx=2, pady=2)



    #============ ============#

    # ============= start the button frame ================#

    btn_frame = tk.Frame(master=frm_detail, bd= 5, bg="lightgrey", relief=tk.GROOVE)
    btn_frame.place(x = 30, y= 350, width=350, height=100)

    # button for add student
    btn_add = tk.Button(master=btn_frame, text="ADD", font=("Helvetica", 10), bg="green", fg="white", bd=7,width=5, command=addData)
    btn_add.place(x=10, y=30)

    # button for UPDATE
    btn_update = tk.Button(master=btn_frame, text="UPDATE", font=("Helvetica", 10), bg="orange", fg="black", bd=7, command=updateData)
    btn_update.place(x=80, y=30)

    #button for DELETE 
    btn_delete = tk.Button(master=btn_frame, text="DELETE", font=("Helvetica", 10), bg="red", fg="white", bd=7, command=deleteData)
    btn_delete.place(x=170, y=30)

    # button for CLEAR
    btn_clear = tk.Button(master=btn_frame, text="CLEAR", font=("Helvetica", 10), bg="blue", fg="white", bd=7, command=clearData)
    btn_clear.place(x=260, y=30)

    # ============= End the button frame ==================#

    # ============== Create a SEARCH Frame ========#

    search_frm = tk.Frame(master= frm_data, bg="lightgrey", bd=10, relief= tk.GROOVE)
    search_frm.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(master=search_frm, text="Search By ID", font=("Helvetica", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_comboBox = ttk.Combobox(master=search_frm, font=("Helvetica", 14), state="readonly")
    search_comboBox ['values'] = ("ID NO", "E-MAIL")
    search_comboBox.grid(row=0, column=1, padx=12, pady=2)

    search_btn = tk.Button(master=search_frm, text="Search", font=("Helvetica", 12), bg="blue", fg="White", width=8, bd=5)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(master=search_frm, text="Show All", font=("Helvetica", 12), bg="green", fg="White",  width=8, bd=5)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    print_btn = tk.Button(master=search_frm, text="PRINT", font=("Helvetica", 12), bg="green", fg="White",  width=8, bd=5, command=pdfGenerate)
    print_btn.grid(row=0, column=4, padx=12, pady=2)

    # ============== END Search Frame =============#

    # =============== DATABASE frame ===============#
    main_frm = tk. Frame(master=frm_data, bg ="lightgrey", bd=11, relief=tk.GROOVE)
    main_frm.pack(fill= tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frm, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frm, orient=tk.HORIZONTAL)

    student_table = ttk.Treeview(master=main_frm, columns=("ID No.", "Name", "E-mail", "Phone", "Gender", "D.O.B", "Department"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)
    y_scroll.pack(side=tk.RIGHT, fill= tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill= tk.X)

    student_table.heading("ID No.", text="ID No.")
    student_table.heading("Name", text="Name")
    student_table.heading("E-mail", text="E-mail")
    student_table.heading("Phone", text="Phone")
    student_table.heading("Gender", text="Gender")
    student_table.heading("D.O.B", text="D.O.B")
    student_table.heading("Department", text="Department")

    student_table['show'] = 'headings'

    student_table.column("ID No.", width=100)
    student_table.column("Name", width=100)
    student_table.column("E-mail", width=100)
    student_table.column("Phone", width=100)
    student_table.column("Gender", width=100)
    student_table.column("D.O.B", width=100)
    student_table.column("Department", width=100)

    student_table.pack(fill=tk.BOTH, expand=True)
    student_table.bind("<ButtonRelease-1>", studentRec)
    displayData()

    # =============== END DATABASE frame ===========#





    window.mainloop()