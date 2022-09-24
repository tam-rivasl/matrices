import numpy as np

#PREGUNTA 5
c = np.array([[300,272,240],
              [260,180,324]])

i = np.array([[320,290,240],
              [230,220,210]])

f = 0.75*c
d = 1.20*i

b= f+d

print(f"Matriz B:", b)
print("########################################")
b23= b[1,2]

print(f"La produccion diara para protectada para el proximo año seria de: {b23} ")

#PREGUNTA 6

m = np.array([[1.5,2.0,2.5],
              [1.25,1.5,1.75]])

p = np.array([[240,250,260,270],
              [260,270,280,290],
              [280,290,300,310]])

print("El orden de las matriz M:", m.shape, "la matriz P:", p.shape)

m21 = m[1,0]
p43 = p[2,3]

print("######################")
print(f"El elemento M21: ", {m21}, "El elemento P43", {p43})

#Pregunta 7

t = m.dot(p)
#q = p.dot(m) #NO SE PUEDE CALCULAR.
print("################################")
print("No se puede calcular la matriz q, ya que las filas y columnas no son iguales")
print("el orden de la matriz t", t.shape)

print(t)

t13 = t[0,2]
t21 = t[1,0]

print(f"peso total en kg, utilizados del material 1 en marzo {t13}")
print(f" kg del material dos requeridos durante la produc. en enero {t21}")
