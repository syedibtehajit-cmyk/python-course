#sets duplicate remove karta ha
#square ={i*i for i in range(1,6)}
#print(square)
#numbers = [10,20,20,30,30,30,40,50]
#duplicate_remove = {i for i in numbers}
#print(duplicate_remove)

emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]
#unique_email={i for i in emails}
#print(unique_email)

# second method duplicate remove in set

unique_email=set(emails)
print(unique_email)

