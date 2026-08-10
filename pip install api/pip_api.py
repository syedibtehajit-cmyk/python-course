#import requests
#print("request library sucessful")


#response = requests.get("https://api.github.com")

#print(response.status_code)
#print(response.json())
#data=response.json()
#print(data["current_user_url"])l

# ak dynamic free api data bheja ha
import requests

student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=student
)

#print(response.status_code)
#print(response.json())

#api ko se data delet karwana

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/101"
)

print(response.status_code)