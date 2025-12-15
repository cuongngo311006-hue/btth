print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
S = input("Nhập chuỗi: ")
chuoi_moi = ""

for ch in S:
    if not ch.isdigit():
        chuoi_moi += ch

print(chuoi_moi)
