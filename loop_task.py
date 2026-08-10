# odd number prinf for loop
#for i in range(1,21,2):
   # print(i)
# Even number prinf for loop
#for i in range(2,21,2):
  #  print(i)

#for i in range(10,101,10):
   # print(i)

#for i in range(1,11):
   # if(i % 2 ==0):
   #     print(i," Even number")
   # else:
   #     print(i,"Odd number")
#table make for Loop input user

#table = int(input("Enter Table Number: "))
#for i  in range  (1,11):
  #  print(table,"x",i,"=",table*i)
# User se ek number lo.

# Uske baad 1 se us number tak ka sum nikalo.
#Example:
#Input:
#5
#Output:
#Sum = 15
 #Answer

#usernumber = int(input("enter your number :"))
#usernumber = usernumber +1
#total=0
#for i in range(1,usernumber):
    
   # total=total+i
#print(total)

# odd number ka sum

#Userno = int(input("enter your number :"))
#Userno=Userno+1
#total=0

#for i in range (1,Userno):
  #  if(i %2!=0):
   #     total=total+i


#print("Odd no user input sum",total)

# Even number ka sum
#Userno = int(input("enter your number :"))
#Userno=Userno+1
#total=0
#total1=0

#for i in range (1,Userno):
   # if(i %2==0):
  #      total1=total1+i

#for i in range (1,Userno):
 #   if(i %2!=0):
 #       total=total+i


#print("Even no user input sum",total1,"odd no user input sum",total)





#Userno = int(input("enter your number :"))
#Userno=Userno+1
#total=0
#total1=0

#for i in range (1,Userno):
   # if(i %2==0):
     #   total1=total1+1

#for i in range (1,Userno):
   # if(i %2!=0):
    #    total=total+1


#print("Even no user input count",total1,"odd no user input count",total)

# userse wohi number lena ha jo 3 se divide ho uska sum

#SSSuser_input= int(input("Enter a number end of sum :"))
#total=total=0
#for i in range (1,user_input +1):
  # if(i % 3 == 0):
     #   total=total+i
#print(total)      


# 5 se divide ho aur count ho
#user_input= int(input("Enter a number count divide by 5 :"))
#count=0
#for i in range (1,user_input +1):
  #  if(i % 5 == 0):
  #      count=count+1
#print(total)  

user_input= int(input("Enter a number :"))
even_sum=0
odd_sum=0
even_count=0
odd_count=0
for i in range (1,user_input +1):
    if(i % 2 == 0):
        even_sum=even_sum+i
        even_count=even_count+1
    else:
        odd_sum=odd_sum+i
        odd_count=odd_count+1
        
print("even sum",even_sum,"Even Count",even_count,"odd sum",odd_sum,"odd count",odd_count,)      


    
      



   


   