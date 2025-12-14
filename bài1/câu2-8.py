print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

a, b = 1, 2
total = 0

print(a, end=" ")
while a < 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
    print(a, end=" ")

print("\nSum of even numbers in fibonacci series:", total)
