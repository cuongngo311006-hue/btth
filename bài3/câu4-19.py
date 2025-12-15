print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1000000) if la_nguyen_to(i))
print(P)
