print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
ds = input("Nhập các từ: ").split()

max_len = max(len(tu) for tu in ds)

print("Độ dài lớn nhất:", max_len)
print("Các từ dài nhất:")
for tu in ds:
    if len(tu) == max_len:
        print(tu)
