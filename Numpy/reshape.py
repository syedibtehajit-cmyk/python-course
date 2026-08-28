import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6 ,7,8])

print(numbers.shape)

numbers = numbers.reshape(4, 2)


print(numbers)
print(numbers.shape)