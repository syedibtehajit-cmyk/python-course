import numpy as np
# Copy
marks = np.array([80, 70, 90])

new_marks = marks.copy()

new_marks[0] = 100

print("Original:", marks)
print("New:", new_marks)


#View
numbers = np.array([10, 20, 30])

new_numbers = numbers.view()

new_numbers[1] = 200

print("Original:", numbers)
print("View:", new_numbers)