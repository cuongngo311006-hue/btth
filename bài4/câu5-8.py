print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")


def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
    return False, -1



ds = list(map(int, input("Nhập list: ").split()))
x = int(input("Nhập giá trị cần tìm: "))

found, pos = Sequential_Search(ds, x)

if found:
    print(True, pos)
else:
    print(False)
