# Do arrays ko rows ke taur par upar-neechay combine karta hai.
import numpy as np

a=np.array([10,20,30])
b=np.array([40,50,60])
c=np.array([70,80,90])
#vstack
  # ↓
#vertical
  # ↓
#rows add
 #  ↓
#upar + neeche

result= np.vstack((a,b,c))
print(result)


# H_stack

result= np.hstack((a,b,c))
print(result)
