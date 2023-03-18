from algo1 import *
from linkedlist import *
import random
from mystack import *
from myqueue import *
from mypriorityqueue import *
from math import *


class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

#SEARCH    
def searchR(current, element):
    if (current == None):
        return None

    if (current.value == element):
        return current.key

    leftNode = searchR(current.leftnode, element)
    if (leftNode != None):
        return leftNode

    rightNode = searchR(current.rightnode, element)
    if (rightNode != None):
        return rightNode
      
def search(B, element):
    return searchR(B.root, element)



#INSERT 
def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      newNode.parent = currentNode
      currentNode.rightnode = newNode
      return newNode.key
    else:
      return insertR(newNode, currentNode.rightnode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      newNode.parent = currentNode
      currentNode.leftnode = newNode
      return newNode.key
    else:
      return insertR(newNode, currentNode.leftnode)
  elif newNode.key == currentNode.key:
    return None

def insert(B,element,key):
  newNode = BinaryTreeNode()
  newNode.value = element
  newNode.key = key
  if B.root == None:
    B.root = newNode
    return B.root.key
  else:
    return insertR(newNode, B.root)
    
#DELETE
def searchKeyR(current, key):
    if (current == None):
        return None
    if (current.key == key):
        return current
    rightNode = searchKeyR(current.rightnode, key)
    if (rightNode != None):
        return rightNode
    leftNode = searchKeyR(current.leftnode, key)
    if (leftNode != None):
        return leftNode
def delete(B, element):
    key = search(B, element)
    if (key == None):
        return None
    else:
        node = searchKeyR(B.root, key)
        return deleteR(B, node)


def deleteKey(B, key):
    key = searchKeyR(B.root, key)
    if (key == None):
        return None
    else:
        node = searchKeyR(key)
        return deleteR(B,current)
      



#CASO 1: el nodo a eliminar es una hoja
#CASO 2a: el nodo a eliminar tiene un hijo del lado izquierdo
#CASO 2b: el nodo a eliminar tiene un hijo en el lado derecho
#CASO 3: el nodo a eliminar tiene dos hijos

def deleteR(B, current):
    if (current == None):
        return current

    #Caso 1
    if (current.leftnode == None and current.rightnode == None):

        if (current.parent.leftnode != None and current.parent.leftnode == current):
            current.parent.leftnode = None

        if (current.parent.rightnode != None and current.parent.rightnode == current):
            current.parent.rightnode = None

    #Caso 2a
    elif (current.leftnode != None and current.rightnode == None):
        if (current.parent.leftnode != None and current.parent.leftnode == current):
            current.parent.leftnode = current.leftnode
        if (current.parent.rightnode != None and current.parent.rightnode == current):
            current.parent.rightnode = current.leftnode
          
    #Caso 2b
    elif (current.leftnode == None and current.rightnode != None):
        if (current.parent.leftnode != None and current.parent.leftnode == current):
            current.parent.leftnode = current.rightnode
        if (current.parent.rightnode != None and current.parent.rightnode == current):
            current.parent.rightnode = current.rightnode
          
    #Caso 3
    #Puedo elegir el mayor de los nodos menores o el menor de los nodos mayores
    else:
        """
					biggestnode = biggestNode(current.leftnode)

					biggestnode.parent = None
					if(current.leftnode == biggestnode):
						current.leftnode = None
					if(current.rightnode == biggestnode):
						current.rightnode = None
					biggestnode.leftnode = current.leftnode
					biggestnode.rightnode = current.rightnode
					if(biggestnode.rightnode != None):
						biggestnode.rightnode.parent = biggestnode
					if(biggestnode.leftnode != None):
						biggestnode.leftnode.parent = biggestnode
					B.root = biggestnode

  					"""

        smallestnode = smallestNode(current.rightnode)

        smallestnode.parent = None
        if (current.leftnode == smallestnode):
            current.leftnode = None
        if (current.rightnode == smallestnode):
            current.rightnode = None
        smallestnode.leftnode = current.leftnode
        smallestnode.rightnode = current.rightnode
        if (smallestnode.rightnode != None):
            smallestnode.rightnode.parent = smallestnode
        if (smallestnode.leftnode != None):
            smallestnode.leftnode.parent = smallestnode
        B.root = smallestnode

    return current.key


def biggestNode(current):
    if (current.rightnode != None):
        currentNode = biggestNode(current.rightnode)
        if (currentNode != None):
            return currentNode
    else:
        return current


def smallestNode(current):
    if (current.leftnode != None):
        currentNode = smallestNode(current.leftnode)
        if (currentNode != None):
            return currentNode
    else:
        return current
    
#ACCESS
    #Función recursiva que busca la key
def accessR(currentNode, key):
	if currentNode == None: return

	if currentNode.key == key:
		return currentNode
	
	right = accessR(currentNode.rightnode, key)
	if right != None: 
		return right
	
	left = accessR(currentNode.leftnode, key)
	if left != None: 
		return left

def access(B, key):
	currentNode = accessR(B.root, key)
	if currentNode == None: return
	else: return currentNode.value

#UPDATE
def updateR(currentNode, element, key):
  if currentNode.key == key:
    currentNode.value = element
  else:
    if currentNode.rightnode != None:
      if currentNode.rightnode.key == key:
        currentNode.rightnode.value = element
        return key
      else: return updateR(currentNode.rightnode, element, key)
    elif currentNode.leftnode != None:
      if currentNode.leftnode.key == key:
        currentNode.leftnode.value = element
        return key
      else: return updateR(currentNode.leftnode,element, key)
    elif currentNode.rightnode == None and currentNode.leftnode == None:
      return None

def update(L, element, key):
  if L.root == None:
    return None
  else:
    return updateR(L.root, element, key)


#InOrder
class LinkedList:
  head=None
  
def traverseInOrderR(current, L):
  if current != None:
    traverseInOrderR(current.leftnode, L)
    enqueue(L, current.value)
    traverseInOrderR(current.rightnode, L)
  return L

def traverseInOrder(B):
  if B.root==None:
    return None
  else:
    current = B.root
    L = LinkedList()
    return traverseInOrderR(current,L)


#In Post Order

def traverseInPostOrder(B):
  L=LinkedList()
  traverseInPostOrderR(B.root,L)
  return L

def traverseInPostOrderR(nodo,L):
  if nodo!=None:
    traverseInPostOrderR(nodo.leftnode,L)
    traverseInPostOrderR(nodo.rightnode,L)
    enqueue(L,nodo.value)


#In Pre Order

def traverseInPreOrder(B):
  L=LinkedList()
  traverseInPreOrderR(B.root,L)
  return L

def traverseInPreOrderR(nodo,L):
  if nodo!=None:
    enqueue(L,nodo.value)
    traverseInPreOrderR(nodo.leftnode,L)
    traverseInPreOrderR(nodo.rightnode,L)
    
#Traverse Bread First
    
def traverseBreadFirst(B):
#Inserto los elementos que debo visitar en el orden que necesito que se recorran
  queue = LinkedList()
#Almaceno los valores finales
  finalList = LinkedList()
  if (B.root == None):
    return None
  else:
    enqueue(queue,B.root)
    while (queue.head != None):
#Puntero que hace referencia a los elementos en el orden en el que fueron introducidos en la queue
      currentNode = dequeue(queue)
      enqueue(finalList,currentNode.value)
#Se introducen los elementos de izquierda a derecha, y luego en este orden seran señalados por el puntero
      if (currentNode.leftnode != None):
        enqueue(queue,currentNode.leftnode)
      if (currentNode.rightnode != None):
        enqueue(queue,currentNode.rightnode)
    return finalList

#------------------------CHEQUEAR SI ES UN BST------------------------
    #Recorrido In Order en relación a las KEYS, para luego poder compararlas en la lista L
def traverseInOrderKEY_R(current, L):
  if current != None:
    traverseInOrderKEY_R(current.leftnode, L)
    enqueue(L, current.key)
    traverseInOrderKEY_R(current.rightnode, L)
  return L

def traverseInOrderKEY(B):
  if B.root==None:
    return None
  else:
    current = B.root
    L = LinkedList()
    return traverseInOrderKEY_R(current,L)
    
def checkBST(B):
  if B.root == None:
    return None
  if B.root.rightnode == None and B.root.leftnode == None:
    return True
  #Lista traverse in roder que me almacena las key, para luego compararlas
  L = traverseInOrderKEY(B)
  menor = L.head
  mayor = L.head.nextNode
  while mayor != None:
    if menor.value < mayor.value:
      menor = menor.nextNode
      mayor = mayor.nextNode
    else:
      return False
    return True

#----------------------¿BT2 subarbol de BT1?-------------------------
def subtreeR(A, S):
  while S.nextNode != None:
    if A.nextNode.value == S.nextNode.value:
      return subtreeR(A.nextNode,S.nextNode)
    else: return False
  return True

#1°: verifico con la lista de traverse in order, y si esta me da true:
#2°: verifico con la lista traverse in post order, y si esta me da true, entonces confirmo que BT2 es un subárbol de B
  
def subtree(B, BT2):
  if B.root == None or BT2.root == None:
    return None
  A = traverseInOrder(B)     #A = Árbol
  S = traverseInOrder(BT2)   #S = Subárbol
  currentA = A.head
  currentS = S.head
  while currentA != None:
   if currentA.value != currentS.value:
    currentA = currentA.nextNode
   else:
    if subtreeR(currentA,currentS) != False:
      A = traverseInPostOrder(B)     #A = Árbol
      S = traverseInPostOrder(BT2)   #S = Subárbol
      currentA = A.head
      currentS = S.head
      while currentA != None:
        if currentA.value != currentS.value:
          currentA = currentA.nextNode
        else:
         return subtreeR(currentA,currentS)
    else: return False


#-------------------¿ÁRBOL BINARIO BALANCEADO?------------------------

def isBalancedR(current):
  if current == None:   #CASO
    return 0            #BASE
  left = isBalancedR(current.leftnode)
  right = isBalancedR(current.rightnode)
  return (max(left, right)+1)

def isBalanced(B):
  if B.root == None:
    return None
  elif B.root != None and B.root.rightnode == None and B.root.leftnode == None:
    return True
  else:
    leftSide = isBalancedR(B.root.leftnode)
    rightSide = isBalancedR(B.root.rightnode)
    if abs(leftSide-rightSide) <= 1:
      return True
    else:
      return False