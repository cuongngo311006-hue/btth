print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ")
        return

    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R

    print("Chu vi hình tròn =", chu_vi)
    print("Diện tích hình tròn =", dien_tich)


R = float(input("Nhập bán kính R: "))
Tinh(R)
