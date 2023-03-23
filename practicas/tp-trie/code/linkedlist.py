from algo1 import *
class Node:
  value=None
  nextNode=None

class Node:
  value=None
  nextNode=None
class LinkedList:
  head=None
  

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
    
def addInOrder (L, element): #(primero en entrar queda en la cabeza)
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
  current = L.head
  contador = 0
  while current != None:
    current = current.nextNode
    contador += 1
  return contador

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
def checkOrder(L):
  menorAmayor=True
  current1 = L.head
  current2 = L.head.nextNode
  while current2 != None:
    if current1.value > current2.value:
      menorAmayor=False
    current1 = current1.nextNode
    current2 = current2.nextNode
  if menorAmayor==True:
    return True
  else:
    return False

def revert(L):
	newList = LinkedList()
	long = length(L)
	current = L.head
	for i in range(long):
		long -= 1
		add(newList, current.value)
		current = current.nextNode
	return newList

def move(L,posInicio,posFinal):
  element=access(L,posInicio)
  size=length(L)
  if posInicio > posFinal:
    initialPosition = posInicio
    finalPosition = posFinal
  elif posInicio < posFinal:
    initialPosition = posInicio-1
    finalPosition = posFinal+1
  else:
    return
  insert(L,element,finalPosition)
  current = L.head
  if posInicio == 0:
    L.head = current.nextNode
  else:
    for i in range (0,initialPosition):
      current = current.nextNode
    current.nextNode = current.nextNode.nextNode