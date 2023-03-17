from algo1 import *
from linkedlist import *
import random
from mystack import *
from myqueue import *
from mypriorityqueue import *
from math import *


class AVLTree:
	root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None
  h = None

"""Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol binario resultante sea un árbol AVL.  """
#una vez insertado el nuevo nodo, debo: 
#1) recorrer el arbol desde el nodo insertado hacia la raiz, 
#2) calcular el bf y height de cada nodo en el camino y 
#3) rebalancear de ser necesario

#######INSERT 

def update_bf(B,node):
  if node != None:
  #caso 1) nodo padre con un solo hijo (a la der o izq):
    if (node.rightnode != None and node.leftnode == None):
      node.h += 1
      node.bf = (node.h)
    elif (node.leftnode != None and node.rightnode == None):
      node.h += 1
      node.bf = -(node.h)
    #caso 2) nodo padre con dos hijos:
    elif (node.rightnode != None and node.leftnode != None):
      node.h = max(node.rightnode.h, node.leftnode.h)+1
      node.bf = node.leftnode.h - node.rightnode.h
    #caso 3) no existe ningun hijo:
    elif (node.rightnode == None and node.leftnode == None):
      node.h = 0
      node.bf = 0

    #verificamos si el nodo es ladeado a la derecha o izquierda
    if (node.bf < -1) or (node.bf > 1):
      reBalance(B)
    #llamo a la funcion recursiva
    update_bf(B,node.parent)
  else:
    return B

def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      newNode.parent = currentNode
      currentNode.rightnode = newNode
      return newNode
    else:
      return insertR(newNode, currentNode.rightnode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      newNode.parent = currentNode
      currentNode.leftnode = newNode
      return newNode
    else:
      return insertR(newNode, currentNode.leftnode)
  elif newNode.key == currentNode.key:
    return None

def insert(B,element,key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key
  newNode.h = 0
  newNode.bf = 0
  if B.root == None:
    B.root = newNode
    return B
  else:
    node = insertR(newNode, B.root)
    if node != None:
      update_bf(B,node.parent)
  return B

"""reBalance(AVLTree) 
Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad."""


def reBalanceR(AVLTree,current):
  if current == None:   #caso base
    return
    
  if current.bf < 0:
    if current.rightnode.bf > 0:
      rotateRight(AVLTree,current.rightnode)
      rotateLeft(AVLTree,current)
    else:
      rotateLeft(AVLTree,current)
  elif current.bf > 0:
    if current.leftnode.bf < 0:
      rotateLeft(AVLTree,current.leftnode)
      rotateRight(AVLTree,current)

  reBalanceR(AVLTree,current.leftnode)     #llamadas recursivas
  reBalanceR(AVLTree,current.rightnode)

def reBalance(AVLTree):
  reBalanceR(AVLTree,AVLTree.root)
  return AVLTree                #devuelvo el arbol balanceado



"""calculateBalance(AVLTree) 
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol"""


def calculateHeight(current):
  if current == None:   #CASO
    return 0            #BASE    
  else:
    bf = calculateHeight(current.leftnode)-calculateHeight(current.rightnode)+1
    left = calculateHeight(current.leftnode)
    right = calculateHeight(current.rightnode)
    return bf

def calculateBalanceR(current):
  if current == None:
    return
  else:
    current.bf = calculateHeight(current.leftnode)-calculateHeight(current.leftnode)
    calculateBalanceR(current.rightnode)
    calculateBalanceR(current.leftnode)
    return

def calculateBalance(AVLTree):
  calculateBalanceR(AVLTree.root)
  return
  

def rotateLeft(T,avlnode):
  newRoot = avlnode.rightnode #asigno la nueva raiz
  newRoot.leftnode = avlnode
  
  if avlnode.rightnode.leftnode != None: #si la nueva raiz tiene un hijo izq:
    newRoot.leftnode.rightnode = avlnode.rightnode.leftnode  #hijo der de la vieja raiz
    newRoot.leftnode.rightnode.parent = avlnode #actualizo parent

#actualizo parent de la nueva raiz
  if avlnode.parent == None: #si la raiz vieja es la raiz
    T.root = newRoot
  else: #sino pregunto si la vieja raiz esta a la der o izq del padre
    if avlnode.parent.rightnode != avlnode: 
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
      
  avlnode.parent = newRoot

def rotateRight(T,avlnode):
  newRoot = avlnode.leftnode  #asigno la nueva raiz
  newRoot.rightnode = avlnode 

  if avlnode.leftnode.rightnode != None: #si la nueva raiz tiene un hijo derecho:
    newRoot.rightnode.leftnode = avlnode.leftnode.rightnode  #es el hijo izquierdo de la vieja raiz
    newRoot.rightnode.leftnode.parent = avlnode #actualizo parent
#actualizo parent de la nueva raiz
  if avlnode.parent == None: #si la raiz vieja es la raiz
    T.root = newRoot
  else: #sino pregunto si la vieja raiz esta a la der o izq del padre
    if avlnode.parent.rightnode == avlnode: 
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
   
  avlnode.parent = newRoot

"""Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol binario resultante sea un árbol AVL."""

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
        return deleteR(B,node)
      
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
      node = current.parent
      current.parent.leftnode = None

    if (current.parent.rightnode != None and current.parent.rightnode == current):
      node = current.parent
      current.parent.rightnode = None
    
    #Caso 2a
  elif (current.leftnode != None and current.rightnode == None):
    node = current.leftnode
    if (current.parent.leftnode != None and current.parent.leftnode == current):
      current.parent.leftnode = current.leftnode
    if (current.parent.rightnode != None and current.parent.rightnode == current):
      current.parent.rightnode = current.leftnode
          
    #Caso 2b
  elif (current.leftnode == None and current.rightnode != None):
    node = current.rightnode
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
        node = smallestnode
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

  #con la variable node voy guardando los nodos segun la condición para luego actualizar el bf del AVL
  #una vez eliminado el nodo, llamo a la funcion update_bf   
  update_bf(B,node)  #actualizo height y bf
  return B #retorno el arbol balaceado

  
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

  
####################################################################################################################

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