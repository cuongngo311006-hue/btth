print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
from tkinter import *


def NewFile(): print("New File!")
def OpenFile(): print("Opening File...")
def InsText(): print("Inserting Text...")
def InsPic(): print("Inserting Picture...")
def About(): print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)


filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)


insertmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
