print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
f1 = open("data.txt", "r")
f2 = open("copy.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()

print("Sao chép file thành công")
