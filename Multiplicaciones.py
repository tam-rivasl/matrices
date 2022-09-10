from array import array
from calendar import c
from re import A
import numpy as np
#La multiplicaciones de matrices, debe ser homonologa, es decir la filas de la matriz 1 debe ser igual a las columnas de la matriz b

W = np.array([[4,0],
              [1,2],
              [7,8]])

Z = np.array([[6,3,2,9],
              [1,5,4,8]])

#Para realizar la multiplicacion se debe realizar con dot es decir
#X=W*Z = X= W.dot(Z)
X= W.dot(Z)

print(X)

print("###############################################")
      
      
      
#Materiales y modelos
A = np.array([[1,2],
             [3,2]])
#Modelos y meses 
B = np.array([[290,312],
             [345,413]])
#Materiales y meses
C = A.dot(B) 
print(C)
print("#####################################################")
#Los elementos c21 y c11

C21 = C[1,0]
C11 = C[0,0]

print(f"Se utilizaron {C21} kilos de aluminio en enero ")
print(f"Se utilizaron {C11} kilos de aluminio en enero")