print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
def tim_max_min(ds):
    ds.sort()
    return ds[0], ds[-1]


n = int(input("Nhập số lượng phần tử: "))
ds = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)

min_val, max_val = tim_max_min(ds)

print("Phần tử nhỏ nhất:", min_val)
print("Phần tử lớn nhất:", max_val)
