print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

def binary_search(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False


# Chương trình chính
ds = list(map(int, input("Nhập list (đã sắp xếp): ").split()))
x = int(input("Nhập giá trị cần tìm: "))

print(binary_search(ds, x))
