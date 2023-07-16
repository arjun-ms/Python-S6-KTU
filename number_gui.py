import tkinter as tk

def check():
    num = int(num1_val.get())
    if num < 0:
        res.config(text= f"{num} is negative")
    elif num > 0:
        res.config(text= f"{num} is positive")
    else:
        res.config(text= f"{num} is zero")

window = tk.Tk()
window.title("Number Check")

num_l = tk.Label(window,text="Enter a number")
num1_val = tk.Entry(window)
bt = tk.Button(window,text="Check",command=check)
res = tk.Label(window,text="")

num_l.pack()
num1_val.pack()
bt.pack()
res.pack()

window.mainloop()