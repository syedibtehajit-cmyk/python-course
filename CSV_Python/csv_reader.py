import csv

#with open("student.csv","r") as file:
    #reader = csv.reader(file)

    #for row in reader:
        #if row: # agar row empty ni ha to ye lage ho
            #print(row)
     # write krna csv mein   
with open("student.csv","w",newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["Name","salary"])
    writer.writerow(["mubarak",25000])
    writer.writerow(["jdm",35000])

    # append krwana exsisting file new row add krna


with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ali", 40000])
            