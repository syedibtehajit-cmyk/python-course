import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [95, 88, 92],
    [60, 68, 75]
])
print("Shape",marks.shape)
#row ke lie
print("student",marks.shape[0])
# sirf column ke lie
print("subjects",marks.shape[1])
# Each student total marks 
student_totals = np.sum(marks, axis=1)
# Each student average
student_totals_average = np.average(marks, axis=1)
# highest marks
student_Highest_Marks = np.max(marks) 
# min marks
student_Min_Marks = np.min(marks) 
# subject wise average
subject_totals_average = np.average(marks, axis=1)

print("Each student's total",student_totals)
print("Each student's average",student_totals_average)
print("Highest mark",student_Highest_Marks)
print("Minimum mark",student_Min_Marks)
print("Subject-wise average",subject_totals_average)


#Shape: (4, 3)
#Students: 4
#Subjects: 3