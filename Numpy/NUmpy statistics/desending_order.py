import numpy as np

numbers = np.array([45, 12, 89, 34, 67, 23])

sorted_numbers = np.sort(numbers)

print("Ascending:", sorted_numbers)
print("Descending:", sorted_numbers[::-1])