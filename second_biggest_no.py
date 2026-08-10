numbers = [10, 50,75]
biggest=numbers[0]
second =numbers[0]
duplicate=0

for i in numbers:
    if(i>biggest ):
        second=biggest
        biggest=i


    elif (i>second ):
        second=i

   
        
        
       
print(biggest,second)
