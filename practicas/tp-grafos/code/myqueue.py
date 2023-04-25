from algo1 import *
from linkedlist import *

#First in - First out
#Incorporo un nuevo elemento a la cola
def enqueue(Q,element):
  #Añado en orden: first in está en la cabeza
  current =Q.head
  newNode = Node()
  newNode.value = element
  if current == None:
    Q.head = newNode
  else:
    while current.nextNode != None:
      current = current.nextNode
    current.nextNode = newNode
  return

#Quito el primer elemento que ingresé a la cola
def dequeue(Q):
  
  if Q.head == None:
    return 
  else: 
    current = Q.head
    element = current.value
    Q.head = current.nextNode
    return element