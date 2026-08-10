# function with parameters
#def Bye():
   # print ("good bye")
#Bye()
#Bye()
#Bye()

#def square(number):
  #  print(number*number)
#square(5)

#Student_name=input("Enter Student Name :")
#def square(student_name):
   # print("You input student name :",student_name)
#square(Student_name)

# square input number

#square_number=int(input("Enter a Number :"))
#def inp(square_number):
   # print("Youre enter number square :",square_number*square_number)
#inp(square_number)


# question 1 task

def fuc_sum(sumnum):
    total=0
    for i in range(1,sumnum +1):
        total=total+i
    return total
    
       
    
print(fuc_sum(5))

def fuc_odd_num(oddsum):
    total=0
    for i in range(1,oddsum +1):
     if (i % 2 !=0):
       total=total+i
    return total
print(fuc_odd_num(5))

def even_odd_sum(even,odd):
   odd_sum=0
   even_sum=0
   for i in range (1,even +1):
    if(i % 2==0):
        
       even_sum=even_sum+i
   else:
         odd_sum=odd_sum+i
   return odd_sum,even_sum
print(even_odd_sum(10,10))