print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
data = ["Python", "C++", "Java", "PHP"]

f = open("list.txt", "w")
for item in data:
    f.write(item + "\n")
f.close()

print("Đã ghi danh sách vào file")
