print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

def tim_max_min(ds):
    ds_sort = ds.copy()   
    ds_sort.sort()
    min_val = ds_sort[0]
    max_val = ds_sort[-1]
    return min_val, max_val


n = int(input("Nhập số lượng phần tử: "))
ds = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)


min_val, max_val = tim_max_min(ds)


print("Phần tử nhỏ nhất:", min_val)
print("Phần tử lớn nhất:", max_val)


print("Vị trí phần tử nhỏ nhất:", ds.index(min_val) + 1)
print("Vị trí phần tử lớn nhất:", ds.index(max_val) + 1)
