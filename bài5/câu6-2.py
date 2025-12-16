print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong



hcn = Hinhchunhat(5, 3)
print(hcn.dien_tich())
