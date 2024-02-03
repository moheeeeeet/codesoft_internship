import random
import string
import tkinter as qt
from tkinter import Entry,Label,Button

def pass_123():
        length = int(length_entry.get())
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation
        mix = lowercase + uppercase + numbers + symbols
        password = random.sample(mix, min(length, len(mix)))
        final_password = "".join(password)
        password_entry.delete(0, qt.END)
        password_entry.insert(0, final_password)
  
def for_copy():
    generated_password = password_entry.get()
    mca.clipboard_clear()
    mca.clipboard_append(generated_password)
    mca.update()
      
mca = qt.Tk()
mca.title(" Random Password")

mca.geometry("300x300")
mca.configure(bg="teal")

length_entry_label = Label(mca, text="Enter password length:", bg="salmon")
length_entry_label.pack(pady=10)

length_entry = Entry(mca)
length_entry.pack(pady=10)

generate_button = Button(mca, text="Generate Password", command=pass_123, bg="lightblue")
generate_button.pack(pady=10)

password_entry = Entry(mca, font=("Times New Roman", 12, "bold"))
password_entry.pack(pady=10)

copy_button = Button(mca, text="Copy to Clipboard", command=for_copy, bg="lightgreen")
copy_button.pack(pady=20)

mca.mainloop()
