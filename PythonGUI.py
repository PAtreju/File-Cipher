import tkinter as tk
from tkinter import filedialog, ttk
from PythonCipher import CipherFile
from PythonGoogleAPI import main

pc = CipherFile()

key_filename = None
filename = None

def select_key_file():
    global key_filename
    key_filename = filedialog.askopenfilename()
    key_file_label.config(text=key_filename)

def select_file():
    global filename
    filename = filedialog.askopenfilename()
    file_label.config(text=filename)

def encrypt_file():
    if pc.encrypt_file(key_filename, filename) == 0:
        status_label.config(text="Encryption failed.")
    else:
        status_label.config(text="File encrypted successfully.")

def decrypt_file():
    if pc.decrypt_file(key_filename, filename) == 0:
        status_label.config(text="Decryption failed.")
    else:
        status_label.config(text="File decrypted successfully.")

def create_key():
    pc.create_key()
    key_file_label.config(text="Key file created successfully.")

def upload_file():
    if filename is None:
        status_label.config(text="No file selected.")
    else:
        main(filename)
        status_label.config(text="File uploaded successfully.")

root = tk.Tk()
root.geometry("800x600")
root.title("File Encryption/Decryption")
root.configure(bg='light blue')

style = ttk.Style()
style.configure("TButton", font=("Arial", 20), background="blue")
style.configure("TLabel", font=("Arial", 20), background='light blue')

# Key section
key_label = ttk.Label(root, text="Key File:")
key_label.place(relx=0.25, rely=0.1, anchor='center')

select_key_button = ttk.Button(root, text="Select Key File", command=select_key_file)
select_key_button.place(relx=0.25, rely=0.2, anchor='center')

key_file_label = ttk.Label(root, text="")
key_file_label.place(relx=0.25, rely=0.3, anchor='center')

add_key_button = ttk.Button(root, text="Create Key File", command=create_key)
add_key_button.place(relx=0.25, rely=0.4, anchor='center')

key_created_label = ttk.Label(root, text="")
key_created_label.place(relx=0.25, rely=0.5, anchor='center')

# File section
file_label = ttk.Label(root, text="File to Encrypt/Decrypt:")
file_label.place(relx=0.75, rely=0.1, anchor='center')

select_button = ttk.Button(root, text="Select File", command=select_file)
select_button.place(relx=0.75, rely=0.2, anchor='center')

file_label = ttk.Label(root, text="")
file_label.place(relx=0.75, rely=0.3, anchor='center')

encrypt_button = ttk.Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.place(relx=0.75, rely=0.4, anchor='center')

decrypt_button = ttk.Button(root, text="Decrypt File", command=decrypt_file)
decrypt_button.place(relx=0.75, rely=0.5, anchor='center')

# Upload section
upload_button = ttk.Button(root, text="Upload File", command=upload_file)
upload_button.place(relx=0.5, rely=0.7, anchor='center')

reminder_label = ttk.Label(root, text="Remember to encrypt files before uploading!")
reminder_label.place(relx=0.5, rely=0.8, anchor='center')

status_label = ttk.Label(root, text="")
status_label.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()