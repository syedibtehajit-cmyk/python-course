import numpy as np
marks = np.array([45, 80, 32, 90, 67, 25, 75])
print(marks > 50)
print(marks[marks > 50])

# 1️⃣ AND — dono conditions true hon
print(marks[(marks >= 50) & (marks <= 80)])

#2️⃣ OR — koi ek condition true ho
print(marks[(marks < 40) | (marks > 80)])

#Practice
print("Between 60 and 90:", marks[(marks >= 60) & (marks <= 90)])