print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
nums = input("Nhập các số (cách nhau bởi dấu phẩy): ")
lst = nums.split(",")

odd_list = []

for x in lst:
    if int(x) % 2 != 0:
        odd_list.append(int(x))

print(odd_list)
