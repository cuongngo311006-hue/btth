print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Welcome")

v = IntVar()
v.set(1)  

def show_rank():
     
    messagebox.showinfo("Lựa chọn", f"Bạn đang chọn số: {v.get()}")

 
Radiobutton(root, text="First", variable=v, value=1).grid(row=0, column=0)
Radiobutton(root, text="Second", variable=v, value=2).grid(row=0, column=1)
Radiobutton(root, text="Third", variable=v, value=3).grid(row=0, column=2)

Button(root, text="Click Me", command=show_rank).grid(row=0, column=3, padx=10)

root.mainloop()
