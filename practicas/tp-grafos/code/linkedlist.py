from algo1 import *
class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None

def printLista(L):
  current = L.head
  while current != None:
    print(current.value, end=" ")
    current = current.nextNode
  print('')

def add(L,element):
  current = L.head
  nuevoNodo = Node()
  nuevoNodo.value = element
  
  if current == None:
    L.head = nuevoNodo
  else:
    nuevoNodo.nextNode = current
    L.head = nuevoNodo
    
def addInOrder (Q, element): #(primero en entrar queda en la cabeza)
  current =Q.head
  newNode = Node()
  newNode.value = element
  if current == None:
    Q.head = newNode
  else:
    current = Q.head
    while current.nextNode != None:
      current = current.nextNode
    current.nextNode = newNode
  return

def search(L,element):
  current = L.head
  currentPos = 0
  contador = 0
  while contador == 0 and current != None:
    if current.value == element:
      return currentPos
      contador += 1
    else:
      current = current.nextNode
      currentPos += 1

def insert(L,element,position):
  current = L.head
  currentPos = 0
  if position == 0:
    add(L,element)
    return position
  elif current == None:
    return None
  elif position > 0:
    nuevoNodo = Node()
    nuevoNodo.value = element
    
    if currentPos+1 == position:
      nuevoNodo.nextNode = current.nextNode
      current.nextNode = nuevoNodo
      
    else:
      while currentPos < position-1 and current != None:
        current = current.nextNode
        currentPos += 1
      if current == None:
        return None
      else:
        nuevoNodo.nextNode = current.nextNode
        current.nextNode = nuevoNodo
  return position

def delete(L,element):
  position = search(L, element)
  current = L.head
  if position == 0:
    L.head = L.head.nextNode
    return position
  elif position == None: 
    return 
  else:
    for i in range (0, position-1):
      current = current.nextNode
    current.nextNode = current.nextNode.nextNode
    return position

def length(L):
  if L != None:
    current = L.head
    contador = 0
    while current != None:
      current = current.nextNode
      contador += 1
    return contador
  else:
    return 0

def access(L,position):
  current = L.head
  if position == 0:
    return current.value
  else:
    for i in range (0, position):
      if current == None: 
        return None
      current = current.nextNode
    return current.value
     
def update(L,element,position):
  current = L.head
  contador = 0
  if position == 0:
    current.value = element
    return position
  else: 
    while current != None and contador < position:
      current = current.nextNode
      contador += 1
    if current == None:
      return 
    else:
      current.value = element
  return position