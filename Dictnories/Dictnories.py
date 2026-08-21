# Dictnary bana add adn update krna .
#student={
  #  "Name":"Ali",
    #"Age":30,
    #"Course":"CS"
#}
#student["Age"]=35 #updatve kia
#student["address"]=" karachi" # Add kia
#del student["Age"] # ye dictnaries se delete karne ke lie use hota ha
#print(student) # Print


# Use get in Dichnory
#print(student.get("Name")) # 1st output name ali is waja se ke wo dicnary ke andar ha
#print(student.get("color"))# ye dichnory ke andar ni ha is waja se output None ha
#print(student.get("color",18))# ye is mein iski value and key dono to gert de dua warna none hota upar line mein ha
#print(student.get("Age",65))# ye dictnary ki value chordega and default pe agar upar di hui value pe get lagenge to

student = {
    "name": "Ali",
    "age": 20
}

print(student.items())

#for loop in python key anvalue print
car = {
    "brand": "Suzuki",
    "model": "Every"
}

for key, value in car.items():
    print(key, value)

