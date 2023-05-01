from algo1 import *
from linkedlist import *

#Last in - First out

#Ingreso un elemento a la pila

def push(S,element):
  add(S,element)
  return

#Quito el ultimo elemento agregado a la pila

def pop(S):
  if S.head == None: 
    return
  else:
    current = S.head
    element = current.value
    S.head = current.nextNode
    return element
  
  