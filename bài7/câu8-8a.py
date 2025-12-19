print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
from tkinter import *

root = Tk()
root.title("Thông tin cá nhân")

labels = ["Họ tên:", "Ngày sinh:", "MSSV:", "Ngành học:"]
for i, text in enumerate(labels):
    Label(root, text=text).grid(row=i, column=0, padx=10, pady=5, sticky=W)
    Entry(root).grid(row=i, column=1, padx=10, pady=5)

root.mainloop()
