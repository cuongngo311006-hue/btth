print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def dien_tich(self):
        return math.pi * self.radius ** 2

    def chu_vi(self):
        return 2 * math.pi * self.radius


hinh_tron = Circle(3)
print("Diện tích:", hinh_tron.dien_tich())
print("Chu vi:", hinh_tron.chu_vi())
