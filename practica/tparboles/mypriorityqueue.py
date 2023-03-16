from algo1 import *
from linkedlist import *

class PriorityNode:
  value=None
  nextNode=None
  priority=None

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
    if current.priority <= priority:
      Node.nextNode = current
      Q.head = Node
      return position
    else: 
      while current.nextNode != None:
        position += 1
        if current.nextNode.priority >= priority:
          current = current.nextNode
        else:
          Node.nextNode = current.nextNode
          current.nextNode = Node
          return position

      current.nextNode = Node
      position += 1
      return position

def dequeue_priority(Q):
  current = Q.head
  if current == None:
    return
  else:
    element = current.value
    Q.head = current.nextNode
  return element
  

    