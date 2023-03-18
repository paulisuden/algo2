import algo1
from linkedlist import *
import random
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



