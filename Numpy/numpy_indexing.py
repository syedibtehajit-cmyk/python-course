import numpy as np
marks = np.array([
    [80, 70, 90],
    [80, 70, 90],
    [80, 70, 90]
])

print("Index no 1",marks[0])

print("Index no 2",marks[1])
print("Index no 3",marks[2])

#specipfic specific ke lie pehle  is mein row 0 column 2
  #    Column
   #      0   1   2
#       ┌───┬───┬───┐
#Row 0  │80 │70 │90 │
 #      ├───┼───┼───┤
#Row 1  │80 │70 │90 │
#       ├───┼───┼───┤
#Row 2  │80 │70 │90 │
 #      └───┴───┴───┘


print("Range index",marks[1,0])
print("Range index",marks[2,1])


#pure 1st row and second row

print(marks[0, :])
#print(marks[0:2, :])

#column
#iska matlab jitna column chaie 0 1 2
print(marks[:, :2])
#iska matlab sirf 2 column
#print(marks[:, 2])