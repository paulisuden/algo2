
from trie import *
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


"""Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento 
y False en caso contrario. Se considera que un Trie pertenecen al mismo documento cuando:
1.	Ambos Trie sean iguales (esto se debe cumplir)
2.	Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido 
insertadas en un orden diferente.
En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 
"""
#recorrerTrie, recorre el arbol completo y guarda sus palabras en una LinkedList
#mi funcion recorrerTrieR tiene una complejidad de n^2 ya que dentro de un bucle while llamo a la funcion recursiva n veces.
def recorrerTrie(T1):
  listaPalabras = LinkedList()
  recorrerTrieR(T1.root.children.head,"",listaPalabras)
  return listaPalabras

def recorrerTrieR(current,palabra,lista):
  if current == None:
    return lista

  if current.nextNode is None: #es hijo único:
    palabra += current.value.key
    if current.value.isEndOfWord == True: #si es un nodo hoja, agrego la palabra a la lista
      add(lista,palabra)
    recorrerTrieR(current.value.children.head,palabra,lista) #paso a la siguiente lista

  else: #no es hijo unico
    palabra1 = palabra #guardo cadena hasta donde es hijo unico (ej, guardo "co": "corazon" y "como")
    while current is not None:
      palabra += current.value.key
      if current.value.isEndOfWord == True: #si es un fin de palabra, agrego la palabra a la lista
        add(lista,palabra)
      recorrerTrieR(current.value.children.head,palabra,lista) #paso a la siguiente lista
      current = current.nextNode 
      palabra = palabra1

# arbolesIdenticos busca en T2 las palabras de T1 que anteriormente las agregue a una lista.
def arbolesIdenticos(T1,T2):
  lista = recorrerTrie(T1)
  print("Lista palabras T1:")
  printLista(lista)
  print("")
  print("¿Árboles idénticos?")
  current = lista.head
  while current != None:
    busco = search(T2,current.value)
    if busco == False:
      return False
      break
    else:
      current = current.nextNode
  return busco