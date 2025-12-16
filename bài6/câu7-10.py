print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
f = open("text.txt", "r")
words = f.read().split()
f.close()

max_len = len(max(words, key=len))
longest_words = [w for w in words if len(w) == max_len]

print("Từ dài nhất:", longest_words)
