print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
s = input("Nhập chuỗi: ")
ds = s.split(',')

kq = []
for so in ds:
    if int(so, 2) % 5 == 0:
        kq.append(so)

print(",".join(kq))
