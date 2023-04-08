import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a Text widget and set its height and width
label = tk.Text(root, height=2, width=30, wrap="none")
label.pack(side="top", fill="both", expand=True)

# Create a Scrollbar widget and attach it to the Text widget
scrollbar = tk.Scrollbar(root, orient="horizontal")
scrollbar.pack(side="bottom", fill="x")

label.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=label.xview)

# Insert some text into the Text widget
label.insert("end", "This is a long label that can be scrolled horizontally if it exceeds the width of the Text widget.")

root.mainloop()
