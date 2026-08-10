#cubes=[i**3 for i in range (1,21)if i%2==0] 
#print(cubes)

#Aresult = [i * 2 if i % 2 == 0 else i * 3 for i in range(1, 11)]
#print(result) 
#numbers=[i*2 if i % 2 == 0 else "not even" for i in range(1,11)]
#print(numbers)

numbers=[i for i in range(1,11) if i % 2 != 0]
print(numbers)

[i * 2 if i % 2 == 0 else "Odd"
 for i in range(1,11)]
