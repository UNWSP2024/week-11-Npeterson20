import tkinter as tk
from tkinter import messagebox

def show_info():
    # Display the name and address in a message box
    messagebox.showinfo("Info", "Name: Nolan\nAddress: 1580 Creek View Drive")

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Name and Address")

    # Set the dimensions of the window
    root.geometry("300x200")

    # Create the Show Info button
    show_button = tk.Button(root, text="Show Info", command=show_info, font=("Arial", 12))
    show_button.pack(pady=20)

    # Create the Quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("Arial", 12))
    quit_button.pack(pady=20)

    # Start the main loop
    root.mainloop()

create_gui()
