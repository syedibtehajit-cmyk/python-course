# Zip 2 ya zyada lists ko pair bana deta hai.
#names = ["Ali", "Ahmed", "Sara"]
#marks = [80, 90, 75]

#result = zip(names,marks)
#print(list(result))
#zip loop ke sath

cities = ["Karachi", "Lahore", "Islamabad"]

temperature = [35, 32, 30]

for cit, temp in zip(cities,temperature):
    print(cit,temp)
