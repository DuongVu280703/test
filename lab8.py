import tkinter as tk
from tkinter import Text, Menu, filedialog, messagebox

def new_file():
    if text_area.get("1.0", tk.END) != '\n':
        save_changes = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if save_changes:
            save_file()
        elif save_changes is None:
            return
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))

def exit_app():
    if text_area.get("1.0", tk.END) != '\n':
        save_changes = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if save_changes:
            save_file()
        elif save_changes is None:
            return
    root.quit()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def undo():
    text_area.event_generate("<<Undo>>")

def about():
    messagebox.showinfo("About", "This is a simple Notepad application built with Tkinter.")

root = tk.Tk()
root.title("Notepad")

menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Undo", command=undo)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

text_area = Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

root.mainloop()
