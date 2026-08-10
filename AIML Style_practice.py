def classify_num(x):
    if x%2==0:
        return"Even"
    else:
        return"Odd"
    
for n in range(1,11):
    print(n, "is",classify_num(n))