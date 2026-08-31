import numpy as np
marks = np.array([80, 70, 90, 65])

print("Marks:", marks)
print("Data Type:", marks.dtype)

# Integer se Float mein convert krna

import numpy as np

marks = np.array([80, 70, 90, 65])

new_marks = marks.astype(float)

print("Original:", marks)
print("Original Type:", marks.dtype)

print("New:", new_marks)
print("New Type:", new_marks.dtype)

numbers = np.array([10.5, 20.7, 30.9, 40.2])

new_numbers = numbers.astype(int)

print("Original:", numbers)
print("Converted:", new_numbers)