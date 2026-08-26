#student_list=[]


number_of_students = int(input("How many students do you want to add? "))

for i in range(number_of_students):
       print("Enter Student", i + 1, "Details")
       Student_name=input("Enter your Name: ")
       math_marks=int(input("Enter math Marks : "))
       english_marks=int(input("Enter English Marks : "))
       Sceince_marks=int(input("Enter Sceince Marks : "))

       total=math_marks+english_marks+Sceince_marks

       average = total / 3


       percentage = (total/300)*100


       print("Student Name",Student_name)
       print("----------------")
       print("English Marks",english_marks)
       print("----------------")
       print("Sceince Marks",Sceince_marks)
       print("----------------")
       print("Math Marks",math_marks)
       print("----------------")
       print("Total Marks",total)
       print("----------------")
       print("Average",average)
       print("----------------")
       print("Percentage",percentage)

       if percentage >=80:
           print("Grade A1")
       elif percentage >= 70:
          print("Grade A")
       elif percentage >= 60:
         print("Grade B")
       elif percentage >= 50:
         print("Grade C")
       elif percentage >= 40:
         print("Grade D")
       else:
          print("Grade F")


    