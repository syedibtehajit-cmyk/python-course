# different class same method different object ko polymorphism kahte han

class dog:
    def speak(self):
        print("dog are barked")
class cat:
    def speak(self):
        print("Meon")

dog1=dog()
cat1=cat()
dog1.speak()
cat1.speak()