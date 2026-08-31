import numpy as np

a = np.array([ #2D mein axis important hota hai
    [10, 20],
    [30, 40]
])

b = np.array([
    [50, 60],
    [70, 80]
])



#axis=0 → neeche rows add
#axis=1 → side mein columns add
print(np.concatenate((a, b), axis=1))
print(np.concatenate((a, b), axis=0))