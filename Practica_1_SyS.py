import numpy as np

#1) Investigue si hay alguna función de numpy que nos devuelva
#la magnitud del número complejo:
Zc1 = 3+4j
print("El numero complejo elejido es:" , Zc1)
print("La magnitud del numero complejo es:", abs(Zc1))

#2) COMPLETAR:
zc1 = 2 + 4j
zc2 = 2 + 6j

zc1_real = np.real(zc1)
zc1_imag = np.imag(zc1)

suma = zc1 + zc2
resta = zc1 - zc2
multiplicacion = zc1 * zc2
division = zc1 / zc2

print('La parte real es:' , zc1_real)
print('La parte imaginaria es:' , zc1_imag)

print('Suma: ', suma)
print('Resta: ', resta)
print('Multiplicacion: ', multiplicacion)
print('Division: ', division)


#Calcular logaritmo de 0
c = 0
print ("e^0 = ", np.exp(c))
print ("log_natural(0) = ", np.log(c))
print ("log10(0) = ", np.log10(c))
#QUEDO MAL EL LOGARITMO DE 0 MMMM AUXILIO

#Calcular logaritmo de infinito
from numpy import inf
d = inf
print ("e^infinito = ", np.exp(d))
print ("log_natural(infinito) = ", np.log(d))
print ("log10(infinito) = ", np.log10(d))

#Use la funcion shape de Numpy para ver las dimensiones de la matriz c.
#Recuerde que puede usar help de la misma para ver como es su uso.
#Primero voy a crear la matriz a y la imprimo, al igual que su traspuesta

a = np.array (([1, 5, 2],[3,4,8]))
a_traspuesta = np.transpose(a)
print ("matriz a: \n", a)
print ("matriz a traspuesta: \n ", a_traspuesta)

#Luego voy a ver su dimension ---NO SALIO



#Muestre los elementos de la columna 2 de la matriz, basandose en lo realizado

C2 = a[:,1]
print ("Segunda columna: ")
print (C2)

#Corregir el error de la siguiente sentencia:
a = np.array(1, 2, 3, 4)
