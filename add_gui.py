import tkinter as tk

def add():
    num1 = int(num1_val.get())
    num2 = int(num2_val.get())
    sum = num1 + num2     
    res.config(text= f"Result: {sum}")

window = tk.Tk()
window.title("ADD")

num1_l= tk.Label(window,text="First Num")
num1_val = tk.Entry(window)
num2_l= tk.Label(window,text="Second Num")
num2_val = tk.Entry(window)
bt = tk.Button(window,text="ADD",command=add)
res = tk.Label(window,text="")

num1_l.pack()
num1_val.pack()
num2_l.pack()
num2_val.pack()
bt.pack()
res.pack()

window.mainloop()