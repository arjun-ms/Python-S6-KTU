import tkinter as tk
from datetime import datetime

def calculate_age():
    birthdate = birthdate_entry.get()
    birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_label.config(text=f"Your age is {age}")

window = tk.Tk()
window.title("Age Calculator")
window.geometry("800x800")

birth_label = tk.Label(window, text="Enter your birthdate (DD-MM-YY): ")
birthdate_entry = tk.Entry(window)

bt = tk.Button(window, text="Calculate Age" ,command=calculate_age)

age_label = tk.Label(window,text="")

birth_label.pack()
birthdate_entry.pack()
bt.pack()
age_label.pack()
window.mainloop()