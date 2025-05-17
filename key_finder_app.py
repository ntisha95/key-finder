import tkinter as tk
from tkinter import messagebox

# Fungsi saat tombol ditekan (sementara hanya simulasi)
def send_signal():
    messagebox.showinfo("Simulasi", "Sinyal pencarian dikirim (simulasi).")

# GUI
root = tk.Tk()
root.title("Smart Key Finder")
root.geometry("350x180")
root.configure(bg="#f2f2f2")

label = tk.Label(root, text="Tekan tombol di bawah untuk mencari kunci:", bg="#f2f2f2", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Cari Kunci 🔍", command=send_signal, bg="#007acc", fg="white", font=("Arial", 14, "bold"), width=20, height=2)
button.pack(pady=10)

root.mainloop()
