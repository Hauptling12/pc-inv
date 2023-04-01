# Import the required libraries in tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create an instance of tkinter frame or window
win = Tk()
win.call("source","dark.tcl")
# Set the size of tkinter window
win.geometry("700x350")

# Create an instance of ttk Style
style = ttk.Style()

# Configure the theme with style
style.theme_use('sun-valley-dark')

# Define a function to show the message
def display_msg():
   messagebox.showinfo("Message", "You are learning Python Tkinter!")

# Add a Customized Label widget
label = ttk.Label(win, text="Hey Folks, I have a Message for You!", font=('Aerial 16'))
label.pack(pady=5)

# Add a Button widget
ttk.Button(win, text="Show Message", command=display_msg).place(x=285, y=98)

win.mainloop()
