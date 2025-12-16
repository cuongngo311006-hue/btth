print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
f = open('D:/a.txt', 'r', encoding='utf-8')

char = 0
wc = 0
lc = 0

for line in f:
    lc += 1
    for k in range(len(line)):
        char += 1
        if line[k] == ' ':
            wc += 1
    wc += 1   # từ cuối dòng

print("The no. of chars is", char)
print("The no. of words is", wc)
print("The no. of lines is", lc)

f.close()
