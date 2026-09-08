# unique() ka kaam hai kisi column ke andar unique/different values dikhana.
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 75000, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data  )
print(df["Department"].unique())
print(df["Age"].unique())

# Next: value_counts()

print(df["Department"].value_counts())

# 🐼 Next Topic: groupby()

df.groupby("Department")["Salary"].mean()
print(df.groupby("Department")["Salary"].mean())

# Group by sum
print(df.groupby("Department")["Salary"].sum())

#Ab 3 important operations yaad rakho:
df.groupby("Department")["Salary"].mean()

#➡️ Average salary

df.groupby("Department")["Salary"].sum()

#➡️ Total salary

df.groupby("Department")["Salary"].max()

#➡️ Highest salary

df.groupby("Department")["Salary"].min()

#➡️ Lowest salary


print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].mean())

#Next: groupby() + count()
print(df.groupby("Department")["Name"].count())

#🔥 Ab ek powerful groupby() practice

#Hum ek hi command mein multiple calculations nikal sakte hain.
print(
    df.groupby("Department")["Salary"].agg(
        ["count", "mean", "max", "min", "sum"]
    )
)