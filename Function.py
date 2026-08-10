
# Basic Function
def greet():
    print("hello")
greet()

# Funtion with Parameter
def add_number(a,b,c):
    return(a+b+c)
result = add_number(10,4,42)
print(result)



def squ(e,f):
    return(e*f)
result = squ(8,8)
print(result)

# function with condition

def checksalary(salary):
    if salary >100000:
        return "high salary"
    elif salary <= 50000:
        return "low salary"
    else:
        return("medium salary")
usersalary = int(input("enter your salary"))
print (checksalary(usersalary))
