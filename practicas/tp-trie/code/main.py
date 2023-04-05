from trie import *
from algo1 import *

class Trie:
	root = None
class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

T = Trie()
T.root = TrieNode()


insert(T,String("Hola"))
insert(T,String("Holi"))
insert(T,String("Holu"))
insert(T,String("Pa"))
insert(T,String("Pat"))
insert(T,String("ca"))

print(delete(T,String("Pa")))
print(search(T,String("Pa")))

#Ejercicio 4
insert(T,String("Put"))
insert(T,String("Pet"))
insert(T,String("Pita"))
insert(T,String("Pan"))
insert(T,String("Pau"))
buscoPatron(T,"P",3)

#Ejercicio 5
T1 = Trie()
T1.root = TrieNode()
insert(T1,String("corazon"))
insert(T1,String("como"))
insert(T1,String("andas"))
insert(T1,String("holanda"))
insert(T1,String("hola"))

T2 = Trie()
T2.root = TrieNode()
insert(T2,String("hola"))
insert(T2,String("como"))
insert(T2,String("andas"))
insert(T2,String("holanda"))
insert(T2,String("corazon"))
print(arbolesIdenticos(T1,T2))

     