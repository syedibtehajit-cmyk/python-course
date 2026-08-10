import json

stud = {
    "name" : "Ahmed",
    "age" : 26,
    "city":"karachi"
    



}

data = '{"name": "Ahmed", "age": 26}'

print(json.dumps(stud))
print(json.loads(data))