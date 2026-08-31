#Data analysis mein kabhi data missing hota hai:

import numpy as np

marks = np.array([80, 70, np.nan, 90, 65])

print(np.isnan(marks))

#Output:

#[False False  True False False]

#Matlab third value NaN (missing value) hai.

#Missing values count karna
print(np.sum(np.isnan(marks)))

#🧠 Yaad rakho
#np.isnan()
 #   ↓
#check karta hai
 #   ↓
#value missing/NaN hai?
#    ↓
#True / False

import numpy as np

marks = np.array([80, np.nan, 70, np.nan, 90, 65])

print("Missing check:", np.isnan(marks))
print("Missing count:", np.sum(np.isnan(marks)))

# nan ke output value ko change krna

numbers = np.array([10, np.nan, 30, np.nan, 50])

updated = np.nan_to_num(numbers, nan=0)

print(updated)