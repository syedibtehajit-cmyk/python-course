import requests

#response = requests.get(
 #   "https://jsonplaceholder.typicode.com/posts"
#)

#print(response.status_code)

#data = response.json()

#print(data[:3])
#print(data[2]["title"])
#for post in data:
 #   print(post["userId"])
#user_input=int(input("enter a past id:"))
#found=False
# API FILTERNING CONCEPT
#response = requests.get(
 #   "https://jsonplaceholder.typicode.com/posts"
#)

#data = response.json()

#for post in data:
   # if post["id"] == user_input:
  #      print(post["title"],post["userId"])
 #       found=True

#if found==False:
#  print("post not found")

#status code check krna agar internet band to error show na kare 
#response=requests.get("https://jsonplaceholder.typicode.com/Abd")

#if response.status_code == 200 :
 #  print("Data sucessfully received")
#else:
 #  print("Something went Wrong")

#print(response.raise_for_status())
# error in try and catch

#try:
    #response = requests.get(
     #   "https://jsonplaceholder.typicode.com/abcd"
    #)

   # response.raise_for_status()

  #  print("Data successfully received")


#except requests.exceptions.RequestException as e:
 #   print("API mein HTTP error aa gaya",e)

 # request error and Exception error


#try:
  
 # response= requests.get("https://jsonplaceholder.typicode.com/Abd")

  #response.raise_for_status()
  #print("Success")
#except requests.exceptions.HTTPError:
 # print("HTTP Error")
#except requests.exceptions.RequestException:
  #print("Request Error")


  #Mini project Student for  APi

#try:
    #response = requests.get(
    #    "https://jsonplaceholder.typicode.com/postssss"
   # )

  #  response.raise_for_status()

 #   data = response.json()

#    user_input = int(input("Enter Post ID: "))

    #found = False

   # for post in data:
     #  if post["id"] == user_input:
    #      print(post["title"],post["userId"])
   #       found=True
  #  if found==False:
 #      print("data not found")


#except requests.exceptions.RequestException as e:
 #print("Error:", e)

 # POST SEARCH MINI FOR PROFESSIONAL CODING USING FUNCTION VERSION 2
#def get_post():
      #  response = requests.get(
     #      "https://jsonplaceholder.typicode.com/posts"
    #   )
   
   #     response.raise_for_status()
  #      data = response.json()
 #       return data
       
#try:
    #data = get_post()

   # user_input = int(input("Enter Post ID: "))
  #  found=False

    #for posts in data:
     #   if posts["id"] == user_input:
    #              print(posts["title"],posts["userId"])
   #               found=True
  #  if not found:
 #        print("data not found")

#except requests.exceptions.RequestException as e:
 #   print(e)

# string in search concept
#text = "Python API Project"

#print("API" in text)
#print("Python" in text)
#print("Java" in text)

#MINI SEARCH PROJECT IN STRING VERSION 3

def get_posts():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    data = response.json()

    return data
data = get_posts()
while True:
 try:
    

    choice = int(input(
        "Search by Title = 1, Search by ID = 2, Exit = 3 : "
    ))

    found = False

    if choice == 1:

        user_input = input("Enter title first word: ")

        for post in data:

            if user_input in post["title"]:

                print("-------------------")
                print("ID:", post["id"])
                print("User:", post["userId"])
                print("Title:", post["title"])

                found = True

        if not found:
            print("Data not found")

    elif choice == 2:

        user_input = int(input("Enter ID Search: "))

        for post in data:

            if post["id"] == user_input:

                print("-------------------")
                print("ID:", post["id"])
                print("User:", post["userId"])
                print("Title:", post["title"])

                found = True

        if not found:
            print("Data not found")
    elif choice == 3:
      print("Exit")
      break

  
    else:
      print("Please select only 1 or 2. or 3")
      


 except requests.exceptions.RequestException as e:

    print("API Error:", e)


 except ValueError:

    print("Invalid input. Please enter a valid number.")