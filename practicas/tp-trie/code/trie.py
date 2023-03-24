from linkedlist import *

class Node:
  value=None
  nextNode=None

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
    if current.value.key == palabra[caracter]:
      node = current.value
      break
    L = L.nextNode
  #si el caracter no existe, lo agrego
  if current == None:
    node = TrieNode()
    #node.parent = 
    node.children = LinkedList()
    node.key = palabra[caracter]
    add(L, node)

  #end of word
  if caracter == len(palabra)-1:
    node.value.isEndOfWord = True

  #llamo a la funcion recursiva para el próximo caracter
  insertR(node.children, palabra, caracter+1)
    





