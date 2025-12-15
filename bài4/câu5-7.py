print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")

import numpy as np

# định nghĩa kiểu dữ liệu có cấu trúc
dt = np.dtype([
    ('name', 'U15'),
    ('class', np.int32),
    ('height', np.float64)
])

# tạo mảng có cấu trúc
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
], dtype=dt)

print("Original array:")
print(students)

# sắp xếp theo chiều cao
students_sorted = students[np.argsort(students['height'])]

print("Sort by height:")
print(students_sorted)



