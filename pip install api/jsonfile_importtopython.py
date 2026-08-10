import json
#is dictnory ko jason ki file mein save krwaya hun
#student1={
   # "name":"ibtehaj",
  #  "age":30,
 #   "city":"karachi"



#}

#with open("student.json","w") as file:
 #   json.dump(student1,file)

#json file se python mein read karwana
new_student ={
   "name":"Adil",
   "Age":35,
   "city":"karachi"

   
}


with open("student.json","r") as file:
   data=json.load(file)
#data.append(new_student)   
# update data list in dictnary
   #data[1]["Age"]=10
   #delelt krne ke lie json file se data
data.pop(2)


with open("student.json","w") as file:

   json.dump(data,file,indent=4)
