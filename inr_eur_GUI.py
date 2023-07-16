# Write a GUl-based program that allows the user to convert amount in Indian
# Rupees to amount in Euro.
# The interface should have labeled entry fields for these two values. These
# components should be arranged in a grid where the labels occupy the first row
# and the corresponding fields occupy the second row.
# At start-up, the Rupees field should contain 0.0, and the Euro field should contain
# 0.0. The third row in the window contains two command buffons, labeled R->E
# and E->R. When the user presses the first buffon, the program should use the data
# in the Rupee field to compute the amount in Euro, which should then be output
# to the Euro field. The second button should perform the inverse function.

import tkinter as tk

def convert_to_eur():
    inr = int(inr_entry.get())
    eur = inr*0.001
    eur_entry.delete(0,tk.END)
    eur_entry.insert(0,eur)
    
def convert_to_inr():
    eur = int(eur_entry.get())
    inr = eur*92
    inr_entry.delete(0,tk.END)
    inr_entry.insert(0,inr)
     
window = tk.Tk()
window.title("Currency Converter")
window.geometry("800x800")

inr_label = tk.Label(window, text="Enter amount in INR: ")
inr_entry = tk.Entry(window)
inr_entry.insert(0,"0.0")
eur_label = tk.Label(window, text="EUR: ")
eur_entry = tk.Entry(window)
eur_entry.insert(0,"0.0")
inr_eur = tk.Button(window, text="INR->EUR",command=convert_to_eur)
eur_inr = tk.Button(window, text="EUR->INR",command=convert_to_inr)

inr_label.grid(row=0,column=0)
inr_entry.grid(row=1,column=0)
eur_label.grid(row=0,column=1)
eur_entry.grid(row=1,column=1)
inr_eur.grid(row=0,column=2)
eur_inr.grid(row=1,column=2)

window.mainloop()