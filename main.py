import tkinter as tk

app = tk.Tk()
app.geometry('400x300') 
app.title("Password Strength Analyzer")

app.resizable(False, False)

title_font = ("Arial", 20, "bold")
title_label = tk.Label(app, text='Password Strength Checker', font=title_font, fg='#FFF', bg='#000')
title_label.pack(pady=20)

password_label = tk.Label(app, text="Enter your password:", fg='#FFF', bg='#000', font=("Arial", 12))
password_label.pack(pady=5)

password_entry = tk.Entry(app, font=("Arial", 12), show="*")  
password_entry.pack(pady=10)

result_label = tk.Label(app, text="Password strength: ", fg='#FFF', bg='#000', font=("Arial", 10), wraplength=380)
result_label.pack(pady=10)

def analyze_strength():
    password = password_entry.get()

    if len(password) < 6:
        result = "Weak (Too short)"
    elif len(password) < 8:
        result = "Moderate (Good length, but needs more)"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        result = "Strong (Good mix of letters and numbers)"
    else:
        result = "Weak (Add more variety, e.g., special characters)"

    result_label.config(text=f"Password strength: {result}")

analyze_button = tk.Button(app, text="Analyze", command=analyze_strength, font=("Arial", 12))
analyze_button.pack(pady=10)

app.mainloop()
