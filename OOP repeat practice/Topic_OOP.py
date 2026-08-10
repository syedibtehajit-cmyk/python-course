#class car:
 #   pass
#car1 = car()
#car2 = car()
#print(car1)
#print(car2) 

#class student:


    
 # self.name=name
   # self.age=age

#student1=student("ibtehaj",30)

#print(student1.name)
#print(student1.age)

#Attribute + Method ko ek saath dekho

#class student:
    #def __init__(self,name):
   #     self.name = name
  #  def introduce(self):
 #       print("My name is",self.name)
        

#student1=student("ibtehaj")
#student2=student("Ali")
#student3=student("Ahmed")

#student1.introduce()
#student2.introduce()
#student3.introduce()
   
# OOP Inheritance topic

#class Animal:
 #   def speak(self):
  #      print("Animals are sound")
   # def loud(self):
    #    print("Dog are loud")

#class cat(Animal):
 #   def speak(self):
  #      print("Meon")


#cat1=cat()
# method Over riding
#cat1.speak()



#lass dog(Animal):
  #  pass
#dog1=dog()
#dog1.loud()

# encapsulation

#class bankaccount():
 #   def __init__(self,balance):
  #      self.__balance=balance
        
   # def get_balance(self):
    #    return self.__balance 
    
    #def deposit(self,amount):
     #   self.__balance +=amount

#account1 = bankaccount(5000)
#account1.deposit(2000)
#print(account1.get_balance())

#class car:
 #   def __init__(self,brand,color):
  #      self.brand=brand
   #     self.color=color
    #def show_info(self):
     #   print("Car Brand",self.brand)
      #  print("Car Color",self.color)
#car1 = car("Toyaota","Black")
#car2 = car("Honda","White") 
#car1.show_info()
#car2.show_info()

#class house:
 #   def __init__(self,house,price):
  #      self.house=house
   #     self.price=price

    ##def show_house(self):
      #  print("house location", self.house)
       # print("house price", self.price) 

# inheritance class
#class luxuray(house):
 #   def show_luxury(self):
  #      print("this house is swinming pool")
 


#house1 = house("northnazmabad",150000000)

#house2 = house("northkarachi",100000000)
#luxhouse=luxuray("DHA",5000000000)
#luxhouse.show_house()
#luxhouse.show_luxury()
#house1.show_house()
#house2.show_house()

# METHOD OVERRIDING TOPIC

#class Animal():
 #      def speak(self):
 #             print("Animal sound")
#class cat(Animal):
      # pass
 #      def speak(self):
  #            super().speak()
   #           print("Meow")
    

#cat1=cat()
#cat1.speak()

# super ka kaam Parent ke methods ko call karna hai Animal parent aur dog child ha

#class Animal():
    #def __init__(self,name):
   #     self.name=name
  #  def show_animal(self):
 #       print("Show Dog Name",self.name)

#class Dog(Animal):
    #def __init__(self, name,bread):
    #    super().__init__(name)
   #     self.bread=bread
  #  def show_dog(self):
 #       print("Dog bread",self.bread)



#dog1=Dog("Tommy","German shepard")
#dog1.show_dog()

# Encapsulation jo class ke andar method direct acces ni deskta

#class BankAccount():
 #   def __init__(self,balance):
  #      self.__balance=balance
  #  def show_acount(self):
   #     print("Your Balance is",self.__balance)

#    def deposit(self, amount):
 #        if amount > 0:
  #        self.__balance += amount
   #      else:
    #         print("invalid deposit")

    #def withdrwal(self,amount):
     #   if  amount <= self.__balance:
      #      if amount > 0:
       #      self.__balance -= amount
        #    else:
         #       print("invalid amount")
        #else:
         #   print("insufficent balance")
            



#account1=BankAccount(5000)
#account1.show_acount()
#account1.deposit(2000)
#account1.show_acount()

#account1.withdrwal(-1000)
#account1.show_acount()

# Composition Topic
# Task1
#class Engine():
  #  def start(self):
 #       print("Engine start")
#class Car:
    #def __init__(self):
   #     self.engine=Engine()
  #  def start_car(self):
  #      self.engine.start()
 #       print("car started")
        
#car1=Car()
#car1.start_car()
#task2

#class battery():
  #  def charge(self):
 #       print("batter charging")
#class mobile:
    #def __init__(self):
    #    self.battery=battery()
   # def start_charging(self):
  #      self.battery.charge()
 #       print("mobile is working")

#mob1=mobile()
#mob1.start_charging()

#task3

class Engine():
    def start(self):
        print("Engine started")

class GPS:
    def location(self):
        print("Location Found")

class car:
    def __init__(self):
        self.Engine=Engine()
        self.GPS=GPS()
    def Driving(self):
        self.Engine.start()
        self.GPS.location()
        print("Car is driving")
car1=car()
car1.Driving()