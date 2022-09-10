import numpy as np

################ Ejercicio clases sabado ###################


V1 = np.array([[30,34,20],
    [ 45,20,16],
    [ 14,26,25]])

T2 = np.array([[35,30,26],
              [52,25,18],
              [23,24,32]])

A2  = V1 + T2
print("La produccion mensual total de ambas plantas serian en la matriz", A2)

#Elemento A21

A21 = A2[1,0]
print(f"El valor corresponde a {A21} mil de pares de zapatos, color blanco para niños")

B = 1.3*V1 +0.9*T2
print(B)

B13 = A2[0,2]
print(f"se tiene {B13} mil pares de zapatos color negro para caballeros.")