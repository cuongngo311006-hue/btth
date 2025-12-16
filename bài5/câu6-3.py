print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
class Nguoi:
    def getGender(self):
        return "Unknown"


class Nam(Nguoi):
    def getGender(self):
        return "Nam"


class Nu(Nguoi):
    def getGender(self):
        return "Nữ"



nguoi1 = Nam()
nguoi2 = Nu()

print("Giới tính người 1:", nguoi1.getGender())
print("Giới tính người 2:", nguoi2.getGender())

