
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
#print(student)
user_searchinput=input("select functions  1select 2update 3 delete")

#user_delete=input("delete by user select 3")
if(user_searchinput=="1"):
      usersearching=input("Enter user whos search")
     
      for i in students:
      
        if(i["name"]==usersearching):
          print(" Searching Data result","Name",i["name"],"Age",i["age"],"City",i["city"])
if (user_searchinput=="2"):
         user_update_name=input("enter user  name")
         user_update=input("enter user update city")
         for i in students:
             if(i["name"]==user_update_name):
                  i["city"]=user_update
                  print(" Searching Data result","Name",i["name"],"Age",i["age"],"City",i["city"])
if (user_searchinput=="3"):
         user_delete=input("enter student name whos delete")
         
         found=False
         for i in students:
             if(i["name"]==user_delete  ):
                  found==True
                  students.remove(i)
                  
                  print(students)
                  break

if(found==False):
     print("Student not found")
              

            
                  
         
                        
 
    
 
     # i["city"]=user_update
      #print (" Searching Data result","Name",i["name"],"Age",i["age"],"City",i["city"])
    #else:
      # print("Student Not found")
  
      


   
        
        
   


    