print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
from itertools import islice

def file_read(fname):
    with open(fname, "w", encoding="utf-8") as f:
        f.write("Python Exercises\n")
        f.write("Java Exercises")

    with open(fname, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

file_read("abc.txt")
