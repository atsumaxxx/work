import tkinter as tk

# Create main window
frm = tk.Tk()

# Change window size
frm.geometry('600x400')

# Change window title
frm.title("test Window")

# Edit label
label = tk.Label(frm, text="Hello,World")
# Display label
label.grid()

# Create Button
button = tk.Button(frm, text="Button1", command="pushed")
button.grid()

editBox = tk.Entry(width=50)
editBox.insert(tk.END,"てすと")
editBox.grid()

frm.mainloop()

