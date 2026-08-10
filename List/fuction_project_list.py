#🎯 Assignment
#Sirf ye banao.
#show_students()
#Jo
#List ke andar jitne bhi students hain
#Sab print kare


students = []

student1={
    "name" : "Ali",
    "age" : 30,
    "city" :"karachi"
}
student2={
    "name" : "adil",
    "age" : 35,
    "city" :"Faislabad"
}
student3={
    "name" : "Ahmed",
    "age" : 25,
    "city" :"Lahore"
}
students.append(student1)
students.append(student2)
students.append(student3)

def student_add():
    
         

         while True:
        
                try:
                  stud_name=input("Enter A StudentName")
                  stud_age=int(input("Enter your age"))
                  stud_city=input("Enter A City")
                  student={
                                        "name": stud_name,
                                         "age": stud_age,
                                        "city" :stud_city
                       
                       
                                                        }             
                     
                  students.append(student)
                  print("student add successfully")
                  break



               
                except:
                 print("invalid ")
            
           
 
   

           
            



def show_student():
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
   for i in students:
           
        
        print("Student Name",i["name"],"student Age",i["age"],"student City",i["city"])
        
   
def search_student():
    show_input_student=input("enter name in data for search ")
    found=False
    for i in students:
        if(i["name"] == show_input_student):
            found=True
            print("Student Name",i["name"],"student Age",i["age"],"student City",i["city"])
            break
    if(found==False):
     print("Student Not Found")
         

#search_student()
#show_student()

student_add()  
  
show_student()
     

