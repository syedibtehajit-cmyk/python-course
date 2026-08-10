# decorator ka matlab fuction ko variable mein store krna
def welcome():
    print("welcome")

star=welcome

star()


# Nested Function
def teacher():

    def student():
        print("Learning Python")

    student()

teacher()


#Function ko Argument ke taur par Pass Karna

#Yahi Decorators ki foundation hai.

