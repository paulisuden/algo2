import algo1
from linkedlist import *
import random
import math


#Ejercicio 4:
"""Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del medio de 
la lista contiene antes que él en la lista la mitad de los elementos menores que él. 
Explique la estrategia de ordenación utilizada."""


def ordeno_antes(L,current,medio):
  print(current.value)
  #en esta 1er parte llevo los elementos mas grandes que 'medio' a su derecha y me aseguro de tener antes de el elementos mas chicos
  if current != medio:
    if current.value > medio.value:
      aux = current
      next = current.nextNode
      delete(L,current.value)
      aux.nextNode = medio.nextNode
      medio.nextNode = aux
      ordeno_antes(L,next,medio)
    else:
      ordeno_antes(L,current.nextNode,medio)
  else:
    return L
  

def ordeno_dps(L,current,medio):
  #en esta 2da parte llevo los elementos mas chicos que 'medio' a su izq y me aseguro de tener antes de el elementos mas chicos y dps los mas grandes
  if current != None:
    if current.value < medio.value:
      aux = current
      next = current.nextNode
      delete(L,current)
      add(L,aux.value)
      ordeno_dps(L,next,medio)
    else:
      ordeno_dps(L,current.nextNode,medio)
  else:
    return L
  
class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None

L = LinkedList()
add(L,9)
add(L,10)
add(L,6)
add(L,1)
add(L,4)
add(L,5)
add(L,8)
add(L,2)
add(L,3)
add(L,7)
printLista(L)

mitadPos = math.trunc(length(L)/2)
medio = L.head
for i in range(1,mitadPos):
  medio = medio.nextNode

print (medio.value)

ordeno_antes(L,L.head,medio)
printLista(L)

"""ordeno_dps(L,medio.nextNode,medio)

printLista(L)
"""


#EJERCICIO 5

"""Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y 
un entero n y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional."""

"""A una función recursiva le paso como parametro la lista, el entero, current y element, 
(en donde ambos estan definidos como L.head al principio). 
Luego, con un bucle for recorro la suma primero sumando el primer elemento con los demás hasta obtener como resultado el entero. 
Si el bucle for termina y no lo encontre, ahora sumo el segundo elemento de la lista con los demás, y asi sucesivamente hasta finalizar el recorrido.
Como uso una funcion recursiva y dentro de ella un bucle for, la complejidad es de O(n log n)"""

class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None

L = LinkedList()
for i in range(10):
  add(L,random.randint(1,10))
print('Lista:')
printLista(L)
print('')

n = 7

def ContieneSuma(L,n):
  element = L.head
  current= L.head
  ContieneSumaR(L, n, element, current.nextNode)

def ContieneSumaR(L,n,element,current):
  for i in range(length(L)-1):
    if current != element and (element.value + current.value) == 7:
      return print ('True')
      break
    else:
      current = current.nextNode
  if current == element:
    return print('False')
  else:
    ContieneSumaR(L,n,element.nextNode,L.head)

ContieneSuma(L,n)

#EJERCICIO 4
"""Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del medio de 
la lista contiene antes que él en la lista la mitad de los elementos menores que él.  
Explique la estrategia de ordenación utilizada."""



