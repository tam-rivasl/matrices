import numpy as np
#Sumatorias:
#suma resta arimetica (cantidad constante)
#El reto es geometrica (razon)
#Guia pruena https://colab.research.google.com/drive/1QiJ1NSuUaTHjVaJKI_ctB_IV5Mh5T9dg?usp=sharing#scrollTo=5sBLekgBMLTx
#Ejercicio 1:

#La población de un ciudad, actualmente de 5.000.000 habitantes, crece a una tasa anual del 2,3%. Definimos  Hi  como la cantidad de habitantes de esta ciudad estimada para dentro de  i  años.

#a) Indique el tipo de sucesión al cual corresponde este caso. Justifique su respuesta.

#b) Escriba una expresión, que dependa del lugar del término, para la sucesión  hi .

#c) ¿Cuántos habitantes se estima que habrá dentro de 12 años?

#d) ¿Cuántos años deben transcurrir para que la población estimada sea 7.879.210 habitantes?


a1 = 50000*1.03
a2 = a1*1.03
a3 = a2*1.03
print(a1,a2,a3)

#probar que tipo de sucesion es:

#Arimetica
b1 = a3 - a2
b2 = a2 - a1
print( b1, b2)

#Geometrica:
c1 = a3/a2
c2= a3/a2

print(c1, c2)

#es una sucesion aritmetica

#Ejercicio 4:

d = np.array([[300, 272, 240],
              [260,180,324]])

f = np.array([[320,290,240],
              [230,220,210]])
#a
g = d+f

#b
print(f"La matriz G pero en la guia sale como A es: {g}")

#c
g12 = g[0,1]

print(f"El elemento a12 es {g12}")


