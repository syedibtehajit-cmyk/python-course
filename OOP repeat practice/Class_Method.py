class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # add method action behaviour
    def introduce(self):
        print("--------------")
        print("my name is",self.name)

        print("My Age is:",self.age)


student1=student("Ibtehaj",35)
student2=student("ali",30)
student3=student("Zee",36)
#print(student1.name)
#print(student1.age)
student1.introduce()
student2.introduce()
student3.introduce()