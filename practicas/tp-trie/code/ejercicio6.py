from linkedlist import *
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
  #CASOS BASE: 
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