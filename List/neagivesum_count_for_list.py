
      
#numbers = [10, -5, -20, 30, -8, 15]       
#smallno= numbers[0]
#for i in numbers:
    #if(i < smallno):
    #    smallno=i
#print(smallno)    
#negative and postive sum

numbers = [10, -5, -20, 30, -8, 15]       
negativesum=  0
negativecount= 0
for i in numbers :
    
    if(i<0):
     negativesum=negativesum+i
     negativecount=negativecount+1
     
   

print(negativesum,negativecount) 

 