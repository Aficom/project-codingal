import tkinter as tk
def show_text():
    user_input = entry.get()
    if user_input.strip().lower() == "myself":
        result_label.config(text="Hello! I am a Python Tkinter script.")
    else:
        result_label.config(text="Kichu paowa jayni! Onukripa kore 'myself' likhun.")
root = tk.Tk()
root.title("Input Check App")
root.geometry("400x250")
instruction_label = tk.Label(root, text="Nicher box-e 'myself' likhun:", font=("Arial", 12))
instruction_label.pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)
submit_btn = tk.Button(root, text="Submit", font=("Arial", 11, "bold"), command=show_text, bg="#4CAF50", fg="white")
submit_btn.pack(pady=15)
result_label = tk.Label(root, text="", font=("Arial", 11), fg="blue")
result_label.pack(pady=10)
root.mainloop()