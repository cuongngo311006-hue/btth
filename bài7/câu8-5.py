print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
v.set(1)

languages = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose your favourite\nprogramming language:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language[0],
                  padx=20, 
                  variable=v, 
                  command=ShowChoice, 
                  value=val).pack(anchor=tk.W)

root.mainloop()
