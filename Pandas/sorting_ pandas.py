import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 75000, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data  )
print(df.sort_values("Salary")

)
#Sabse kam salary → sabse zyada salary.
print(df.sort_values("Salary", ascending=False))
# zyada salary se kam salary

