numbers = [10, -5, 20, -8, 30, -1, 15]

sum = 0
count =0

for i in numbers:
    if(i > 0):
        sum = sum + i
        count=count+1

print("sum =",sum,"Count =",count)