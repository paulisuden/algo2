from linkedlist import *
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
    #inserto el primer caracter (0)
    T.root.children = LinkedList()
    node = TrieNode()
    node.key = element[0]
    add(T.root.children, node)
    #asigno L a la lista que voy a recorrer ahora
    L = T.root.children.head
  #funcion recursiva que insertara el resto de los caracteres
  insertR(L,element,1)

def insertR(L, palabra, caracter):
    #debo averiguar si ya existe el caracter que quiero insertar
  




