import pandas as pd

#Pandas se hum easily:

#Excel/CSV data read kar sakte hain
#Missing values handle kar sakte hain
#Data filter kar sakte hain
#Columns add/remove kar sakte hain
#Average, maximum, minimum nikal sakte hain
#Data ko ML model ke liye prepare kar sakte hain


data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [25, 30, 27],
    "Salary": [60000, 80000, 75000]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df["Age"])
print(df["Salary"])

print(df.shape)