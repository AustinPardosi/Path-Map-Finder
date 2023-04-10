import tkinter as tk
from tkinter import ttk

# buat window
window = tk.Tk()
window.title("Tabel dengan CustomTkinter")

# buat Treeview
table = ttk.Treeview(window)

# buat kolom pada tabel
table["columns"]=("nama", "umur")

# memberi nama pada masing-masing kolom
table.heading("nama", text="Nama")
table.heading("umur", text="Umur")

# mengatur lebar kolom
table.column("nama", width=100)
table.column("umur", width=100)

# menambahkan data pada tabel
data = [("Andi", 20), ("Budi", 30), ("Cici", 25)]
for i in range(len(data)):
    table.insert("", i, text=str(i+1), values=data[i])

# menampilkan tabel
table.pack()

# jalankan program
window.mainloop()