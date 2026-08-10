# accending number sorted
#numbers = [5, 2, 8, 1, 3]

#sorts=sorted(numbers)
#print(sorts)

# descending order sorted no
#sorts_des=sorted(numbers,reverse=True)
#print(sorts_des)

# topic list in tuples sorted with key 

students = [
    ("Ali", 85),
    ("Ahmed", 92),
    ("Sara", 78)
]

result= sorted(students,key=lambda x:x[1])
print(list(result))