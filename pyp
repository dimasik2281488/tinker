import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("350x450")
root.configure(bg="#2b2b2b")

text_input = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    anchor="e",
    bg="#3c3f41",
    fg="#ffffff",
    padx=10,
    pady=10
)
text_input.pack(fill="x", padx=15, pady=(15, 5))

text_result = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    anchor="e",
    bg="#3c3f41",
    fg="#499c54",
    padx=10,
    pady=10
)
text_result.pack(fill="x", padx=15, pady=(0, 15))

buttons_frame = tk.Frame(root, bg="#2b2b2b")
buttons_frame.pack(expand=True, fill="both", padx=15, pady=5)

digits_layout = [
    (1, 2, 0), (2, 2, 1), (3, 2, 2),
    (4, 1, 0), (5, 1, 1), (6, 1, 2),
    (7, 0, 0), (8, 0, 1), (9, 0, 2),
    (0, 3, 1)
]

for num, row, col in digits_layout:
    btn = tk.Button(
        buttons_frame,
        text=str(num),
        font=("Arial", 14, "bold"),
        bg="#4e5254",
        fg="#ffffff",
        bd=0,
        command=lambda n=num: print(f"Нажата цифра: {n}")
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

def multiply():
    pass

def divide():
    pass

def summy():
    pass

def diff():
    pass

def result():
    pass

operations_matrix = [
    ("*", multiply),
    ("%", divide),
    ("+", summy),
    ("-", diff),
    ("=", result)
]

    op_btn = tk.Button(
        buttons_frame,
        text=symbol,
        font=("Arial", 14, "bold"),
        bg="#ff8c00" if symbol != "=" else "#4caf50",
        fg="#ffffff",
        bd=0,
        command=func
    )
    op_btn.grid(row=i if i < 4 else 3, column=3 if i < 4 else 2, sticky="nsew", padx=3, pady=3)

for r in range(4):
    buttons_frame.rowconfigure(r, weight=1)
for c in range(4):
    buttons_frame.columnconfigure(c, weight=1)

if __name__ == "__main__":
    root.mainloop()
