import numpy as np
# row sum = axis  
#marks = np.array([
  #  [80, 70, 90], #sum wise
  #  [60, 75, 85],
 #   [90, 88, 95]
#])

#print("Student Totals: row wise", np.sum(marks, axis=1),"Student sum column wise",np.sum(marks, axis=0))


#print(np.sum(marks, axis=1))  #Student Total
#print(np.mean(marks, axis=1))  # Student Average


# mean ka matlab ha average nikalna

marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 95]
])

print(np.mean(marks, axis=1))   
print(np.mean(marks, axis=0))


print("Subject Average:", np.mean(marks, axis=0))

print("Student Minimum:", np.min(marks, axis=1))
print("Student Maximum:", np.max(marks, axis=1))


print("Subject Minimum:", np.min(marks, axis=0))
print("Subject Maximum:", np.max(marks, axis=0))