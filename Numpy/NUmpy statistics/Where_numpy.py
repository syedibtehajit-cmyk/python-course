import numpy as np
marks = np.array([45, 80, 32, 90, 67, 25, 75])
result = np.where(marks >= 60, "Good", "Needs Improvement")



#np.where() se actual values change karna



marksS = np.array([35, 55, 72, 28, 90, 40, 65])

new_marks = np.where(marksS < 40, 40, marksS)

print("Original:", marksS)
print("Updated:", new_marks)