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
  

class PriorityNode:
  value=None
  nextNode=None
  priority=None

#menor prioridad (peso/costo) para grafos
def enqueue_priority(Q,element,priority):
  current = Q.head
  Node = PriorityNode()
  Node.value = element
  Node.priority = priority
  position = 0

  if current == None:
    Q.head = Node
    return position
  else:
    if current.priority >= priority:
      Node.nextNode = current
      Q.head = Node
      return position
    else: 
      while current.nextNode != None:
        position += 1
        if current.nextNode.priority <= priority:
          current = current.nextNode
        else:
          Node.nextNode = current.nextNode
          current.nextNode = Node
          return position

      current.nextNode = Node
      position += 1
      return Q

def dequeue_priority(Q):
  current = Q.head
  if current == None:
    return
  else:
    element = current.value
    Q.head = current.nextNode
  return element