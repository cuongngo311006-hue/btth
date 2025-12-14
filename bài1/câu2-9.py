print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

a, b = 1, 2
total = 0

s = input("Enter a string: ")
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)
