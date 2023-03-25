from linkedlist import *

class Node:
  value=None
  nextNode=None
class LinkedList:
  head=None
  

class Trie:
	root = None
class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

T = Trie()


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
    node = TrieNode()
    node.key = element[0]
    add(T.root.children, node)
    #asigno L a la lista que voy a recorrer ahora
    L = T.root.children
  #funcion recursiva que insertara el resto de los caracteres
  insertR(L,element,1)

def insertR(L, palabra, caracter):
  #caso base
  if caracter == len(palabra): 
     return
  
  #debo averiguar si ya existe el caracter que quiero insertar
  current = L.head
  while current != None:
    #si existe, le asigno a node el current
    if current.value.key == palabra[caracter]:
      node = current
      break
    L = L.nextNode
  #si el caracter no existe, lo agrego
  if current == None:
    #si no existe, lo creo y creo su respectiva lista
    node = TrieNode()
    #node.parent = 
    node.children = LinkedList()
    node.key = palabra[caracter]
    add(L, node)

  #end of word
  if caracter == len(palabra)-1:
    node.value.isEndOfWord = True

  #llamo a la funcion recursiva para el próximo caracter
  #mis parametros son los nodos hijos de mi nodo (lista), la palabra y el proximo caracter
  insertR(node.children, palabra, caracter+1)


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
    #si lo encuentro lo guardo en none y rompo el bucle
    if L.value.key == element[caracter]:
      node = L.value.key
      break
    L = L.nextNode
  if L == None:
    return False
  #pregunto si el caracter que encontre es el ultimo de la palabra que busco
  elif caracter == (len(element)-1):
    if node.value.isEndOfWord == True:
      return True
    else:
      return False
  else:
    searchR(node.children,element,caracter+1)



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
    return deleteR(T.root.children,element, [0])
  
def deleteR(L,element,caracter):
  L = L.head
  while L != None:
    if L.value.key == element[caracter]:
      node = L.value.key
      break
    L = L.nextNode
  if L == None: #no se encuentra la palabra
    return False
  else:
    if caracter == len(element)-1:
    #El elemento está presente y es único ó tiene al menos un elemento incluido.
      if node.value.isEndOfWord == True and node.children == None:
        delete(L,node)
        deleteCaso2y3(L)

      #la palabra esta pero no tiene marcada la ultima letra como fin de palabra
      elif node.value.isEndOfWord == False:
        return False
      #la palabra esta pero es prefijo de otra: desmarco el indicador de fin de palabra
      elif node.value.isEndOfWord == True and node.children != None:
        node.value.isEndOfWord = False
        return True

def deleteCaso2y3(node):
  if 
  

   
    


