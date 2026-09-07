import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [25, 30, 27, 35, 24],
    "Salary": [60000, 80000, 71300, 90000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data)
# Boneus column add kia calulation au add kia 

# row mein kuch change karna ho to istarah bhi karskte han
df.loc[2, "Salary"] = 75000
df["Bonus"] = df["Salary"] * 0.10

print(df)


# Delete row & column
# column delete 
df = df.drop("Bonus", axis=1)

print(df)

#2. Ek row delete

#Agar Ayesha (index 4) ko delete karna ho:

df = df.drop(4, axis=0)
#axis=0 → ↓ rows
#axis=1 → → columns
print(df)