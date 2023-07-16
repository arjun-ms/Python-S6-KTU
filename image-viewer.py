import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Image Viewer")
window.geometry("800x800")

img = Image.open("image.png")
# Create an ImageTk.PhotoImage object to display the image on the Canvas widget
photo = ImageTk.PhotoImage(img)

# Create a Label widget and display the image on it
label = tk.Label(window, image=photo)
label.pack()

# Start the GUI main event loop
window.mainloop()
