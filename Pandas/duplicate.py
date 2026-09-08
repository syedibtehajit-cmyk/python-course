import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 71300, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data)
df.loc[5] = ["Ali", 25, 60000, "IT"]

print(df)
print(df.duplicated())
print(df.duplicated().sum())

# duplicate remove karne ke lie

df = df.drop_duplicates()

print(df)
print(df.duplicated().sum())