import tkinter as tk
from tkinter import ttk, messagebox
import register_face
import face_recognition_lock

root = tk.Tk()
root.title("Face Lock System")
root.geometry("700x500")
root.configure(bg='#1e1e2f')

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook', background='#1e1e2f')
style.configure('TNotebook.Tab', background='#222244', foreground='white', padding=[10, 5])

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# === Register Tab ===
register_tab = tk.Frame(notebook, bg='#1e1e2f')
notebook.add(register_tab, text='Register Face')

name_var = tk.StringVar()
dept_var = tk.StringVar()
roll_var = tk.StringVar()

tk.Label(register_tab, text='Name:', fg='white', bg='#1e1e2f').pack()
tk.Entry(register_tab, textvariable=name_var).pack()

tk.Label(register_tab, text='Department:', fg='white', bg='#1e1e2f').pack()
tk.Entry(register_tab, textvariable=dept_var).pack()

tk.Label(register_tab, text='Roll Number:', fg='white', bg='#1e1e2f').pack()
tk.Entry(register_tab, textvariable=roll_var).pack()

def call_register():
    register_face.register(name_var.get(), dept_var.get(), roll_var.get())

tk.Button(register_tab, text='Register Face', command=call_register).pack(pady=10)

# === Lock/Unlock Tab ===
folder_tab = tk.Frame(notebook, bg='#1e1e2f')
notebook.add(folder_tab, text='Face Lock Folder')

folder_name_var = tk.StringVar()
tk.Label(folder_tab, text='Folder Name:', fg='white', bg='#1e1e2f').pack()
tk.Entry(folder_tab, textvariable=folder_name_var).pack()

tk.Button(folder_tab, text='Create Folder', command=lambda: face_recognition_lock.create_folder(folder_name_var.get())).pack(pady=5)
tk.Button(folder_tab, text='Lock Folder', command=lambda: face_recognition_lock.lock_folder(folder_name_var.get())).pack(pady=5)
tk.Button(folder_tab, text='Unlock Folder', command=lambda: face_recognition_lock.unlock_folder(folder_name_var.get())).pack(pady=5)

root.mainloop()