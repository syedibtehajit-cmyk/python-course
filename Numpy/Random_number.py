import numpy as py
#whole number ke lie
numbers = py.random.randint(1 , 101 ,10)
print(numbers)
#Decmal number random

numbers = py.random.rand(5)
print(numbers)

#random decimal number and shape use 
numbers = py.random.rand(3, 4)

print(numbers)
print("Shape:", numbers.shape)