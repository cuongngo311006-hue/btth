print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist


# Chương trình chính
ds = list(map(int, input("Nhập list: ").split()))
print("Danh sách sau khi sắp xếp:")
print(bubbleSort(ds))
