from linkedlist import *
from myqueue import *

class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None


class Trie:
	root = None
class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

"""T = Trie()
T.root = TrieNode()"""

"""insert(T,element) 
Descripción: inserta un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida
"""
def insert(T,element):
  #La lista no esta creada
  if T.root.children == None:
  #creo la lista 
  #inserto el primer caracter (0)
    T.root.children = LinkedList()
    """    node = TrieNode()
    node.parent = T.root
    node.key = element[0]
    node.children = LinkedList()
    add(T.root.children, node)"""
    #asigno L a la lista que voy a recorrer ahora
    #L = T.root.children
  #funcion recursiva que insertara el resto de los caracteres
  insertR(T.root.children,element,0,T.root)

def insertR(L, palabra, caracter,parent):
  #caso base
  if caracter == len(palabra): 
    return

  #debo averiguar si ya existe el caracter que quiero insertar
  if L == None:
    current = TrieNode()
    current.parent = parent
    current.children = LinkedList()
    current.key = palabra[caracter]
    add(L, current)
  else:
    current = L.head
    while current != None:
      #busco el caracter en la lista
      if current.value.key == palabra[caracter]:
        current = current.value
        break
      current = current.nextNode
    #si el caracter no existe en la lista, lo agrego
    if current == None:
      current = TrieNode()
      current.parent = parent
      current.children = LinkedList()
      current.key = palabra[caracter]
      add(L, current)

  #end of word
  if caracter == len(palabra)-1:
    current.isEndOfWord = True
    return 

  #llamo a la funcion recursiva para el próximo caracter
  #mis parametros son: la prox lista, la palabra, el prox caracter y el current que será el padre
  insertR(current.children, palabra, caracter+1,current)


"""
search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie) y el valor del elemento (palabra)
Salida: Devuelve False o True según se encuentre el elemento.
"""

def search(T,element):
  #El árbol esta vacio
  if T.root.children == None:
     return False
  else:
    return searchR(T.root.children,element, 0,)

def searchR(L,element,caracter):
  L = L.head
  #busco el caracter
  while L != None:
    #si lo encuentro lo guardo en node y rompo el bucle
    if L.value.key == element[caracter]:
      node = L.value
      break
    L = L.nextNode
  if L == None:
    return False
  #pregunto si el caracter que encontre es el ultimo de la palabra que busco
  if caracter == (len(element)-1):
    if node.isEndOfWord == True:
      return True
    else:
      return False
  else:
    return searchR(node.children,element,caracter+1)



"""Ejercicio 3
delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie) y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True según se haya eliminado el elemento.
CASOS
*El elemento no se encuentra en el trie. No se modifica la estructura del trie
*El elemento está presente y es único (ninguna parte del elemento contiene a otro). Se borran todos los nodos.
*El elemento es parte de otro elemento más largo (prefijo). 
 Se lo desmarca al indicador de fin de palabra para ese elemento.
*El elemento está presente y tiene al menos un elemento incluido. 
Se eliminan los nodos desde el final de la palabra hasta la primera hoja del elemento más largo.
"""
def delete(T,element):
  if T.root.children == None:
    return False
  else:
    return deleteR(T.root.children,element, 0)
  
def deleteR(L,element,caracter):
  current = L.head
  while current != None:
    if current.value.key == element[caracter]:
      node = current.value
      break
    current = current.nextNode
  if current == None: #no se encuentra la palabra (C1)
    return False

  if caracter == len(element)-1:
  #El elemento está presente y es único ó tiene al menos un elemento incluido (C2y4).
    if node.isEndOfWord == True and node.children.head == None:
      return deleteCaso2y4(L,node) #(node = current.value)

    #la palabra esta pero no tiene marcada la ultima letra como fin de palabra 
    elif node.isEndOfWord == False:
      return False
    #la palabra esta pero es prefijo de otra: desmarco el indicador de fin de palabra (C3)
    elif node.isEndOfWord == True and node.children != None:
      node.isEndOfWord = False
      return True
  else:
    return deleteR(node.children,element,caracter+1)

#me pregunto si al eliminar el nodo la lista ahora esta vacia o no. de estar vacía, 
#puedo eliminar al nodo padre, caso contrario, NO puedo eliminar al nodo padre y hasta ahi llega mi eliminacion
#node.parent apunta a todo lo que tiene(children, key, etc)

def deleteCaso2y4(L,node): #node = L.value
  newNode = node.parent
  #pregunto si la lista tiene un elemento o mas:
  if newNode.children.head.nextNode == None:
    if newNode.children.head != None: #pregunto si no es la root
    #tiene un solo elemento
      deleteL(newNode.children, node)
      deleteCaso2y4(L,newNode)
    else: return True
  else:
    #tiene más de un elemento:
    deleteL(newNode.children, node)
  return True




"""Ejercicio 4
Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas 
las palabras del árbol que empiezan por p y sean de longitud n. """

def buscoPatron(T,patron,n):
  if T.root.children == None:
    return None
  else:
    current = T.root.children.head
    while current != None:
      if current.value.key == patron:
        lista = current.value.children
        current = lista.head
        break
      current = current.nextNode
    if current == None:
      return None
  while current != None:
    palabra = LinkedList()
    enqueue(palabra, patron)
    buscoPalabras(T,patron,n,lista,current,1,palabra)
    current = current.nextNode
  if current == None:
    return 


def buscoPalabras(T,patron,n,lista,current,cont,palabra):
  while (cont != n) and (current != None):
    enqueue(palabra,current.value.key)
    if cont != n-1:
      lista = current.value.children
      current = lista.head
    return buscoPalabras(T,patron,n,lista,current,cont+1,palabra)

  if current == None and cont != n:
    return
  elif cont == n:
    if current.value.isEndOfWord == True:
      printLista(palabra)
      return
    else:
      return 
  else:
    return

##return??
    
