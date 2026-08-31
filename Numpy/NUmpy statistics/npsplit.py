import numpy as np

#concatenate() → arrays ko join karta hai.

#split() → array ko parts mein divide karta hai.

numbers = np.array([10, 20, 30, 40, 50, 60, 70,80])

result = np.split(numbers, 4)

print(result)