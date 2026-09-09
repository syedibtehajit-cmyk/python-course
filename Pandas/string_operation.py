#Names ko CAPITAL letters mein convert karna:
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 75000, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data  )

print(df["Name"].str.upper())

#Names ko lowercase mein:

print(df["Name"].str.lower())

#3️⃣ New column banana

#gar hum original Name ko change nahi karna chahte aur uppercase ka new column banana ho:
df["Name_Upper"] = df["Name"].str.upper()

print(df)

#1️⃣ contains() — kisi text ko search karna

#Check karo kaun se employees IT department mein hain:

#Boolean Output
print(df["Department"].str.contains("IT"))
#Aur actual IT employees filter karne ke liye:
print(df[df["Department"].str.contains("IT")])

# replace() + strip()

print(df["Department"].str.replace("IT", "Information Technology"))
#IT ko doosre text se replace karta hai.

#strip():
print(df["Name"].str.strip())

# Ye text ki length/count of characters batata hai:
print(df["Name"].str.len())