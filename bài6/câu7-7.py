print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

filename = "input.txt"

count = 0
with open(filename, "r", encoding="utf-8") as f:
    for _ in f:
        count += 1

print("Số dòng trong tệp:", count)
