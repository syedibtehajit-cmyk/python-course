name=input("enter ,name")




#file write
#file=open("admin.txt","w")
#data=file.write(name)
#file.close()

#file append
file=open("admin.txt" , "a")
data=file.write("\n"+name)
file.close()

#file read on file handling
file=open("admin.txt","r")
data=file.read()

file.seek(0)#dobara pointer shuru se start kra ta ha
print(data)
file.close()

# this is use as a professionally work on same but is not to use file.close() 

with open("students.txt", "r") as file:
    print(file.readline())# on line read in documents

    file.seek(0)

    print(file.readline())

    # print(file.readlines()) # this is read mulply lines as a pointer