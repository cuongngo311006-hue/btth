print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.str1.upper())


str1 = IOString()
str1.get_String()
str1.print_String()
