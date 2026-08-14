
# Task 1
#even=7
#if even %2 ==0:
  #  print("even")
#else:
   # print("Odd")

#task 2


#check=0
#if check >0:
 #   print("Postive number")

#elif check <0 :
 #   print("Negative")

#else:
   # print("Zero")

# task 3

#a=25
#b=15

#if a>b:
 #   print("A is greater")
#elif b>a:
 #   print("B is greater")
#elif a==b:
   # print("Both are Equal")

#task 4

#age=17
#has_id=False

#if age >= 18 :
 #   has_id=True
#    print("Allowed")
#else:
#    print("not Allowed")

#task 4

#age = 15
#has_parent = True

#if age >= 18 or has_parent:
 #   print("Allowed")
#else:
    #print("Not Allowed")

# Task 5

#attendance=60
#fees_paid=True

#if attendance>=75 and fees_paid:
 #   print("Eligible Exam")
#else:
  #  print("InEligible Exam")


# Task 6

#marks=59

#if marks >= 90 :
#    print("Grade A")
#elif marks >=80 and marks <= 89 :
 #       print("Grade B") 
#elif marks >=70 and marks <= 79:
 #       print("Grade C") 
#elif marks >=60 and marks <= 69:
 #       print("Grade D")
#else:
 #      print("Failed") 

# task 7 

#secret =6
#guess =6
#if guess == secret:
#   print("Correct")
#elif guess < secret:
 #   print("Too Low")
#elif guess > secret:
 # print("Too High")


# Task 8


#is_logged_in = True

#if not is_logged_in:
 #   print("Please login")
#else:
 #   print("Welcome")
# Task 9

#age = 17
#is_banned = False

#if not is_banned and age >= 18:
 #   print("Allowed")
#else:
 # print("Not Allowed")
    

#for i in range (1,21):
   # if i %2==0:
    # print(i)

#for i in range (1,21):
   # if i %2==1:
    # print(i)

#total=0
#for i in range (1,21):
  #  if i %2==0:
 #    total+=i
#print(total)

#total=0
#for i in range (1,21):
 #   if i %2!=0:
  #   total+=i
#print(total)

#even_count=0
#odd_count=0

#for i in range (1,21):
   # if i %2==0:
   #  even_count+=1
  #  if i%2!=0:
 #      odd_count+=1
#print("even count",even_count,"odd count",odd_count)


#even_sum=0
#odd_sum=0

#for i in range (1,21):
 #   if i %2==0:
  #   even_sum+=i
   # if i%2!=0:
    #   odd_sum+=i
#print("even count",even_sum,"odd count",odd_sum)


#count=0
#sum=0
#for i in range(1,51):
 #   if i%3==0:
  #   count+=1
   #  sum+=i
    
#print("count",count,"Sum",sum)

#largest = 1
#for i in range(1,21):
  #  if i>largest:
 #       largest=i
#print(largest)

#numbers = [15, 4, 27, 9, 2, 18]
#small = numbers[0]
#for i in numbers:
  #  if i<small:
 #       small=i
#print(small)


#numbers = [15, 4, 27, 9, 2, 18]
#largest = numbers[0]
#total_sum=0
#even_count=0
#samllest =numbers[0]
#for i in numbers:
 #   total_sum+=i
  #  if i>largest:
   #     largest=i
        
   # if i%2==0:
       
    #    even_count+=1
    #if i<samllest:
     #   samllest=i
   
    

#print("Largest number",largest,"smallest",samllest,"sum",total_sum,"even count",even_count)
#numbers2 = [15, 4, 27, 2, 18]
#for i in numbers2:
  #  if i==9:
  #      print("Found")
 #       break
        
#else:
       # print("not found")

#numbers = [3, 8, 12, 5, 7, 10, 15, 20]

#for i in numbers:
    #if i %5 ==0:
     #continue
    
    
   
    #print(i)

#x= 1 

#while x<=10:
   #if  x%2==0:
    #  print(x)
   #x+=1

#x=1
#total=0
#while x<=20:
  #  if x%2==1:
  #      total+=x
        
 #   x+=1
#print(total)
#
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         x = 1
#even = 0
#odd = 0

#while x <= 20:

   # if x % 2 == 0:
   #     even += x

  #  if x % 2 == 1:
 #       odd += x

 #   x += 1

#print("Even sum:", even)
#print("Odd sum:", odd)

#x = 1

#while x <= 7:
#    if x == 7:
 #       break

  #  print(x)
   # x += 1

x=1
while x<=10:
    if x==5:
      x+=1
      continue
    print(x)
    x+=1