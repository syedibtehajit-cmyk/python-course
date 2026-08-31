import numpy as np
marks = np.array(["80", "70", "90", "65"])
print(marks.dtype)
#Ye normally string type show karega.

#Ab calculations ke liye numbers mein convert:
marks = marks.astype(int)

print(marks)
print(marks.dtype)