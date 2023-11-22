import tkinter as tk
from tkinter import ttk, END, messagebox
import re
from datetime import datetime

def is_valid_roll(roll_number):
    return roll_number.replace("-", "").isdigit()

def is_valid_name(name):
    return all(c.isalpha() or c.isspace() or c in ["'", ".", "-"] for c in name) and name.strip() != ""


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

def is_valid_phone(phone):
    phone_pattern = r'^\d{11}$'
    return re.match(phone_pattern, phone) is not None

def is_valid_date(dob):
    try:
        datetime.strptime(dob, '%d-%m-%y')
        return True
    except ValueError:
        return False