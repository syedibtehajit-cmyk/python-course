# concatenate() ka matlab hai arrays ko join/combine karna.

import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print(result)
