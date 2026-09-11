import pandas as pd
import numpy as np

print("Business Sales Analysis Project Started")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)


df = pd.read_csv("C:/Users/Ibtehaj IT/Documents/python-course/Pandas/Business Sales Data Analysis/data/sales_data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Basic Data Inspection
print(df.head())
print(df.shape)
print(df.info())

#Missing Values Check
print(df.isnull().sum())

#Date ko proper Date format mein convert Karna
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print(df.info())

#Duplicate records check
print("Duplicate rows:", df.duplicated().sum())

#hamari categorical columns mein values exactly kya hain.
print("Categories:", df["Category"].unique())
print("Regions:", df["Region"].unique())
print("Customer Types:", df["Customer_Type"].unique())
#Numeric data validation
print("Quantity <= 0:", (df["Quantity"] <= 0).sum())
print("Sales <= 0:", (df["Sales"] <= 0).sum())
print("Profit <= 0:", (df["Profit"] <= 0).sum())

#orders ki sales ko add karke overall business sales nikalna
total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

#Total Profit

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

#KPI nikalte hain: Profit Margin % — yani sales mein se kitna percent actual profit hai.
profit_margin = (total_profit / total_sales * 100) if total_sales != 0 else 0
print("Profit Margin (%):", profit_margin)
#kaunsa product sab se zyada Sales generate kar raha hai.
product_sales = df.groupby("Product")["Sales"].sum()
print("Product Sales:")
print(product_sales)
#Product-wise Profit
product_profit = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)

print(product_profit)

#Ab Product-wise Profit Margin % calculate karte hain.
product_analysis = df.groupby("Product")[["Sales", "Profit"]].sum()

product_analysis["Profit_Margin_%"] = (
    product_analysis["Profit"] / product_analysis["Sales"]
) * 100

print(product_analysis.sort_values("Profit_Margin_%", ascending=False))

#Region-wise Sales & Profit Analysis
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

print(region_analysis.sort_values("Sales", ascending=False))

#egion-wise Profit Margin %
region_analysis["Profit_Margin_%"] = (
    region_analysis["Profit"] / region_analysis["Sales"]
) * 100

print(region_analysis.sort_values("Profit_Margin_%", ascending=False))

#Customer Type analysis
customer_analysis = df.groupby("Customer_Type")[["Sales", "Profit"]].sum()

print(customer_analysis)

#Profit Margin %.
customer_analysis["Profit_Margin_%"] = (
    customer_analysis["Profit"] / customer_analysis["Sales"]
) * 100

print(customer_analysis.sort_values("Profit_Margin_%", ascending=False))

#monthly sales performance
df["Month"] = df["Order_Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

#monthly Profit
monthly_profit = df.groupby("Month")["Profit"].sum()

print(monthly_profit)

#monthly profit margin
monthly_analysis = df.groupby("Month")[["Sales", "Profit"]].sum()

monthly_analysis["Profit_Margin_%"] = (
    monthly_analysis["Profit"] / monthly_analysis["Sales"]
) * 100

print(monthly_analysis)