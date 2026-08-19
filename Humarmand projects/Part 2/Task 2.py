# While Loop
x=0
while x <=20:
    
    if  x%3==0:
     x+=1
     continue
    print(x)
    x+=1

# For loop Nested

for i in range(2,5):
   for k in range(1,11):
       print(i,"x",k,"=",i*k)      

# break & Continoue

for d in range(1,20):
   if d==5 :
      continue
   if d==15:
      break
   print(d)

   #if elif statment this task is working itel.py in folder

   for o in range(1,11):
    

    userinput = int(input("Enter a number"))
    
    if userinput == -99:
         print("Program stopped")
         break
  
    elif userinput > 0:
        print("Positive number")

    
                    

    elif userinput < 0:
        print("negative number")

    else:
        print("Zero")
 

  