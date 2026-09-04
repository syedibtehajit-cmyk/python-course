import pandas as pd
#Data framing
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 75000, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)

print(df)

# aik column select krna hoto ye
print(df["Name"])
print(df["Salary"])

#Multiple column ke lie ye
print(df[["Name", "Salary"]])

# filtering ke lie ye use hota ha
print(df[df["Age"] > 30])

#specific filtering ke lie ye use hota ha
print(df[df["Department"] == "IT"])

#Do conditions
print(df[(df["Department"] == "IT") & (df["Salary"] > 60000)])