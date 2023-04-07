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
    T.root.children = LinkedList()
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

def buscoPatron(T,prefijo,n):
  long=len(prefijo)
  if T.root.children == None:
    return None
  else:
    current = T.root.children.head
    i = 0
    #Busco el patrón
    while current != None and i < long:
      if current.value.key == prefijo[i]:
        current = current.value.children.head
        i+=1
      elif i < long:
        current = current.nextNode
  if current == None:
    return None
  else:
    lista =LinkedList()
    buscoPalabras(0,current,prefijo,lista,n-1)
    return lista
  
def buscoPalabras(cont,current,palabra,lista,n):
  if current == None:
    return lista

  if current.nextNode is None: #es hijo único:
    palabra += current.value.key
    cont+=1
    if cont == n and current.value.isEndOfWord == True: #si es un nodo hoja, agrego la palabra a la lista
      add(lista,palabra)
    elif cont == n and current.value.isEndOfWord != True: 
      current.value.children.head = None
      cont = 0
    buscoPalabras(cont,current.value.children.head,palabra,lista,n) #paso a la siguiente lista

  else: #no es hijo unico
    palabra1 = palabra #guardo cadena hasta donde es hijo unico (ej, guardo "co": "corazon" y "como")
    while current is not None:
      palabra += current.value.key
      cont += 1
      if cont == n and current.value.isEndOfWord == True: #si es un fin de palabra, agrego la palabra a la lista
        add(lista,palabra)
      elif cont == n and current.value.isEndOfWord != True: 
        current = current.value.children.head
        cont = 0
      buscoPalabras(cont,current.value.children.head,palabra,lista,n) #paso a la siguiente lista
      current = current.nextNode 
      palabra = palabra1
      cont = len(palabra)-1
    
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
  
"""Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. 
Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de 
derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo
abcd y dcka no son invertidas ya que difieren en un carácter."""

def cadenasInvertidas(T3):
  listaPalabras = LinkedList()
  palabraInvertida = False
  return cadenasInvertidasR(T3,T3.root.children.head,"",listaPalabras,palabraInvertida)

def cadenasInvertidasR(T3,current,palabra,lista,palabraInvertida):
  #CASOS BASE: deberia terminar de ejecutarse??????????
  if palabraInvertida == True:
    return print("True")
  
  elif current == None:
    return False

  if current.nextNode is None: #es hijo único:
    palabra += current.value.key
    if current.value.isEndOfWord == True: #si es un nodo hoja, agrego la palabra a la lista
      palabraInv = ""
      m = len(palabra)-1
      for i in range(0,len(palabra)):
        palabraInv += palabra[m-i]
      palabraInvertida = search(T3,palabraInv)
      if palabraInvertida != True:
        palabra = ""
      else:
        print(palabraInv)
        print(palabra)
      
    cadenasInvertidasR(T3,current.value.children.head,palabra,lista,palabraInvertida) #paso a la siguiente lista

  else: #no es hijo unico
    while current is not None:
      palabra += current.value.key
      if current.value.isEndOfWord == True: #si es un nodo hoja, agrego la palabra a la lista
        palabraInv = ""
        for i in range(len(palabra)-1,0):
          palabraInv += palabra[i]  
        palabraInvertida = search(T3,palabraInv)
        if palabraInvertida != True:
          palabra = ""
        else:
          print(palabraInv)
          print(palabra)
          break
      cadenasInvertidasR(T3,current.value.children.head,palabra,lista,palabraInvertida) #paso a la siguiente lista
      current = current.nextNode 

"""EJERCICIO 7: Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, 
que dado el árbol Trie T y la cadena “pal” devuelve la forma de auto-completar la palabra. Por ejemplo, 
para la llamada autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o 
“groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que representa 
el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo, autoCompletar(T, ma’) 
devolvería “” si T presenta las cadenas “madera” y “mama”. """

def autoCompletar(T,prefijo):
  long=len(prefijo)
  if T.root.children == None:
    return None
  else:
    current = T.root.children.head
    i = 0
    #Busco el patrón
    while current != None and i < long:
      if current.value.key == prefijo[i]:
        current = current.value.children.head
        i+=1
      elif i < long:
        current = current.nextNode
  if current == None:
    return None
  
  #completo palabra
  palabra = ""
  if current.nextNode != None:
    return None
  
  while current != None and current.nextNode == None: #mientras sea hijo unico
    palabra += current.value.key
    current = current.value.children.head

  #si current == None entonces la palabra se completo totalmente.
  if current == None:
    return palabra
  
  #si no es hijo unico corto y devuelvo hasta donde lo fue.
  elif current.nextNode != None:
    return palabra




