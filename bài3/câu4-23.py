print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
s = input("Nhập câu: ")

chu = 0
so = 0

for ch in s:
    if ch.isalpha():
        chu += 1
    elif ch.isdigit():
        so += 1

print("Số chữ cái:", chu)
print("Số chữ số:", so)
