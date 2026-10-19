"""Простое окно на tkinter."""
import os
from tkinter import Tk, Button, Label


root = Tk()


root.geometry("400x300")
root.title("Моё окно")
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
try:
    root.iconbitmap(icon_path)  
except Exception:
    pass  


label = Label(root, text="Привет, tkinter!", font=("Arial", 14))
label.pack(pady=40)

button = Button(root, text="Нажми меня", font=("Arial", 12))
button.pack()


root.mainloop()
