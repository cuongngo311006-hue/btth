print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
s = input("Nhập câu: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
