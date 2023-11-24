import os
import tkinter as tk
from tkinter import filedialog

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

# I assigned variable to direct input that is why I cannot again change the directory
# Since it is the global variable first to execute is this variable.
directory_path = filedialog.askdirectory()

def browse_directory():
    global directory_path
    if directory_path:
        list_files(directory_path)


def list_files():
    global directory_path
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    file_listbox.delete(0, tk.END) 

    for file_name in files:
        file_listbox.insert(tk.END, file_name)


def sort_list():
    pass


def rename():
    global directory_path
    prefix = prefix_entry.get()
    folder = directory_path
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    num_digits = len(str(len(files)))
    
    for index, file_name in enumerate(os.listdir(folder)):
        new_name = f"{prefix}{index:0{num_digits}}"
        
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_name)
        os.rename(old_path, new_path)


window = tk.Tk()
window.title("File Renamer")
window.resizable(False,False)

browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack(pady=10)

file_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width=100)
file_listbox.pack(pady=10)

prefix_label = tk.Label(window, text="Enter Prefix:")
prefix_label.pack()

Rename_button = tk.Button(window, text="Rename", command=rename)
Rename_button.pack(pady=10)

prefix_entry = tk.Entry(window)
prefix_entry.pack(pady=5)

window.mainloop()