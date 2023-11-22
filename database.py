# # database.py

# import sqlite3

# # create a Student Table
# def studentData():
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS student 
#                 (id INTEGER PRIMARY KEY,
                
#                  stdId text,
#                  name text,
#                  email text,
#                  phone text,
#                  gender text,
#                  dob text,
#                  department text)
#         """)
#     conn.commit()
#     conn.close()

# # Start ADD Student
# def addStudentInfo(stdId, name, email, phone, gender, dob, department):
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?)", 
#                    (stdId, name, email, phone, gender, dob, department))
#     conn.commit()
#     conn.close()

# # Dispaly data
# def displayInfo():
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM student")
#     rows = cursor.fetchall()
#     conn.close()
#     return rows

# # UPDATE info Method
# # UPDATE info Method
# def updateStudentInfo(studentID, id, name, email, phone, gender, dob, department):
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE student SET
#         stdId=?,
#         name=?,
#         email=?,
#         phone=?,
#         gender=?,
#         dob=?,
#         department=?
#         WHERE id=?
#     """, (id, name, email, phone, gender, dob, department, studentID))

#     conn.commit()
#     conn.close()

# #DELETE Student information
# def deleteStudentInfo(id):
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM student WHERE id =?", (id,))
#     conn.commit()
#     conn.close()


# database.py

import sqlite3
import hashlib

# create a Student Table
def studentData():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS student 
                (id INTEGER PRIMARY KEY,
                
                 stdId text,
                 name text,
                 email text,
                 phone text,
                 gender text,
                 dob text,
                 department text)
        """)
    conn.commit()
    conn.close()

# Start ADD Student
def addStudentInfo(stdId, name, email, phone, gender, dob, department):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?)", 
                   (stdId, name, email, phone, gender, dob, department))
    conn.commit()
    conn.close()

# Dispaly data
def displayInfo():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows

# UPDATE info Method
# UPDATE info Method
def updateStudentInfo(studentID, id, name, email, phone, gender, dob, department):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE student SET
        stdId=?,
        name=?,
        email=?,
        phone=?,
        gender=?,
        dob=?,
        department=?
        WHERE id=?
    """, (id, name, email, phone, gender, dob, department, studentID))

    conn.commit()
    conn.close()

#DELETE Student information
def deleteStudentInfo(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE id =?", (id,))
    conn.commit()
    conn.close()

# User Authentication
def user_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""

                    CREATE TABLE IF NOT EXISTS user(
                        id  INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )

        """)
    conn.commit()
    conn.close()

# add user(admin)
def insert_user(username, password):
    user_table()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()



# Verify the user
def authentic_user(username, password):
    user_table()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM user WHERE username=? AND password=?", (username, hashed_password))
    result = cursor.fetchone()
    conn.commit()
    conn.close()

    if result:
        print("Authentication successful: User found in the database.")
        return True
    else:
        print("Authentication failed: Invalid username or password.")
        return False
