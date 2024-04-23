"""
Esercizio b
"""
import numpy as np

def clip(x):
   for i in range (0, len(x)):
       np.sort(x[i])
       for j in range(0, len(x[i])-1):
           x[i][j] = 0
           
A = np.array([[1,2,3,4], 
              [5,6,7,8], 
              [9,10,11,12], 
              [13,14,15,16]])

clip(A)
print(A)