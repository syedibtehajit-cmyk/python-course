# ak class ka object dosre class ke andar  ban raha ho compostion kahlata ha
class car:
    def show(self):
        print("has a car")
class engine:
    def __init__(self):
        self.car=car()
    def show1(self):
        self.car.show()
e1=engine()
e1.show1()