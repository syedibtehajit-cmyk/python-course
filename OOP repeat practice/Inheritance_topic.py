class Animal:
    def speak(self):
        print("Animal Make Sound")


class dog(Animal):
    def speak(self):
        super().speak()
        print("dogs are barked")
dog1=dog()
dog1.speak()