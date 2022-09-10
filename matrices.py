import numpy as np

E = np.array ([[8,2,1],
               [-5,6,7]])

F = np.array([[3,4,0],
              [4,-3,9]])

G= E+F
print("Ejercicio 1")
print("matriz G: ", G)

##################################

a = np.array([[2.6,4.8,1.8,0.9],
              [3.2,4.4,2.5,2.8],
              [2.4,3.6,3.8,2.5]])

b= np.array([[3.6,2.5,3.0,2.5],
             [4.5,5.0,3.5,3.8],
             [2.9,3.0,4.6,4.0]])

s= a+b
d = b-a
print("#################################################")
print("Ejercicio 2:")
print("Matriz S =: ", s)
print("Matriz D =: ", d)

###########INTERPRETACION#################
print("Matriz ubicada en s24: Las ventas subieron o bajaron y blablabla")

print("#################################################")
print("Ejercicio3: ")

h= np.array([[71,80,75,90],
      [65,58,74,82]])

j= np.array([[75,83,80,94],
     [67,60,78,85]])

v= j-h

#NOTACION MATRICIAL
v23 = v[1,2]
v14 = v[1,1]
print("Se debe realizar una substraccion para obtener matriz V")
print("Matriz V =", v)
print(f"El aumento de peso de la mujer 3 = {v23} kilos")
print(f"El aumento de peso del hombre 2 = {v14} Kilos")
print("#################################################")
print("Interprete los elementos a21, 14 y v22")
a21= h[1,0]
b14 =j[0,3]
v22 =v[1,1]
print(f"La mujer 1 pesaba {a21} kg antes de las fiestas")
print(f"La mujer 1 pesaba {b14} kg antes de las fiestas")
print(f"La mujer 1 pesaba {v22} kg antes de las fiestas")


################ Ejercicio clases sabado ###################

v1 = np.array([[30,34,20]
    [ 45,20,16],
    [ 14,26,25]])

T2 = np.array([[35,30,26],
              [52,25,18]
              [23,24,32]])

A2  = v + T2
print("La produccion mensual total de ambas plantas serian en la matriz", A2)