

#Largest
numbers =[]
for i in range(5):
 numb=int(input("enter number :"))
 numbers.append(numb)

 largest = numbers[0]
 smallest = numbers[0]
 even1= 0
 odd1= 0
 total=0

        
 for numb in numbers:
        total+=numb
       

        if numb > largest:
            largest=numb
        if numb<smallest:
            smallest=numb
            
        if numb % 2 == 0:
            even1+=1
        else :
            odd1+=1
 average1=total/len(numbers)


print("Largest Number",largest)
print("---------------")
print("Smallest Number",smallest)
print("---------------")
print("Even",even1)
print("---------------")
print("Odd",odd1)
print("---------------")
print("Total",total)
print("---------------")
print("Average",average1)


