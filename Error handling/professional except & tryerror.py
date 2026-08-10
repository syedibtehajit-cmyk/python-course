#try:
 #   num=int(input("enter a number"))
  #  print(num)
#except ValueError:
 #   print("enter a valid number")

#try:
 #   num1=int(input("enter a number 1"))
  #  num2=int(input("enter a number"))
  #  print("2 number divide result :",num1/num2)
#except ValueError:
   # print("inter a Valid number")
#except ZeroDivisionError:
   # print("number cannot divide by zero")

try:
    num=int(input("enter anumber"))
except ValueError:
    print("Invalid no")
else:
    print("enter your number is corrected")
finally:
    print("Program Ended")