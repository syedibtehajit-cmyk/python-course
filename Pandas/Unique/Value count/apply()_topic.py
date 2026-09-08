#pply() ka simple matlab:

#Har value/row par apna function/rule apply karna.

#Example: Hum Salary ke basis par ek new column Salary_Level banana chahte hain:

#Salary >= 70,000 → "High"
#Salary < 70,000 → "Low"
import pandas as pd


data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 75000, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data  )

def salary_level(salary):
    if salary >= 70000:
        return "High"
    else:
        return "Low"

df["Salary_Level"] = df["Salary"].apply(salary_level)

print(df)

#Isse har employee ki salary check hogi aur new column banega.



#Next: apply() ka short practical

#Ab hum Age ke basis par category banayenge:

#Age >= 30 → "Senior"
#Age < 30 → "Junior"

def age_level(age):
    if age >= 30:
        return "Senior"
    else:
        return "Junior"

df["Age_Level"] = df["Age"].apply(age_level)

print(df)