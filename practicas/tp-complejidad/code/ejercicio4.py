import algo1
from linkedlist import *
import random
import math

#Ejercicio 4:
"""Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del medio de 
la lista contiene antes que él en la lista la mitad de los elementos menores que él. (LISTA DE SALIDA) 
Explique la estrategia de ordenación utilizada."""
print('EJERCICIO 4')
class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None

L = LinkedList()
add(L,9)
add(L,2)
add(L,3)
add(L,6)
add(L,4)
add(L,5)
add(L,10)
add(L,8)
add(L,1)
add(L,7)
print('Lista inicial')
printLista(L)
medioPos = math.trunc(((length(L))/2)-1) #(posicion del elemento del medio)
cant = medioPos  #(cantidad de elementos antes del medio)
elemM = cant/2
elemm = cant/2   #(cantidad de elementos menores y mayores antes del medio)

medio = L.head
for i in range(0,medioPos):
  medio = medio.nextNode 

current = L.head
#variables m y M me cuenta la cant de elementos menores y mayores que medio antes de el en la lista
m = 0
M = 0
for i in range(0,medioPos):
  if current.value < medio.value:
    m += 1
  elif current.value > medio.value:
    M += 1
  current = current.nextNode

#Si m>elemm intercambio un valor menor de la izq por otro mayor de la der (de medio), caso contrario si m < elemm

def menorXmayor(L,medioPos):
  #busco menor
  menor = L.head
  for i in range (0,medioPos):
    if menor.value < medio.value:
      menorPos = i
      break
    else:
      menor = menor.nextNode
  #busco mayor
  mayor = medio.nextNode
  for i in range (0,medioPos):
    if mayor.value > medio.value:
      mayorPos = i + medioPos
      break
    else:
      mayor = mayor.nextNode
  update(L,mayor.value,menorPos)
  update(L,menor.value,mayorPos)
  return L

def mayorXmenor(L,medioPos):

  #busco mayor
  mayor = L.head
  for i in range (0,medioPos):
    if mayor.value > medio.value:
      mayorPos = i 
      break
    else:
      mayor = mayor.nextNode

  #busco menor
  menor = medio.nextNode
  for i in range (0,medioPos):
    if menor.value < medio.value:
      menorPos = i + medioPos +1
      break
    else:
      menor = menor.nextNode

  auxMayorValue = mayor.value
  update(L,menor.value,mayorPos)
  update(L,auxMayorValue,menorPos)
  return L

if m > elemm:
  menorXmayor(L,medioPos)
else:
  mayorXmenor(L,medioPos)
print('Lista final:')
printLista(L)