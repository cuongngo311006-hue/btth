print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

result = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))

print(",".join(result))
