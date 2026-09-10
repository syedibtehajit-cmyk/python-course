import pandas as pd
import numpy as np

print("Business Sales Analysis Project Started")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)


df = pd.read_csv("C:/Users/Ibtehaj IT/Documents/python-course/Pandas/Business Sales Data Analysis/data/sales_data.csv")

print(df)