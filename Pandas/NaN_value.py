#NaN ka matlab:

#Not a Number / value missing hai
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 71300, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data)
df.loc[2, "Age"] = None
df.loc[3, "Salary"] = None

print(df)


#2️⃣ Missing values check karna
print(df.isnull())

#Ye True / False batayega.

#True = value missing hai.


#3️⃣ Har column mein kitni missing values hain?

#Ye bohat important command hai:

print(df.isnull().sum())

#Example:

##Name          0
#Age           1
#Salary        1
#Department    0

#🐼 dropna() — Missing wali row delete

print(df.dropna())

#fillna() — Missing value ko fill karna

#Age mein jo missing hai, usko average Age se fill karo.
print(df["Age"].mean())

#Salary ke liye:
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print(df["Salary"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)