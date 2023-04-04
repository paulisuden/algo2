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

insert(T,String("Put"))
insert(T,String("Pet"))
insert(T,String("Pita"))
insert(T,String("Pan"))
insert(T,String("Pau"))
buscoPatron(T,"P",3)

T1 = Trie()
T1.root = TrieNode()
insert(T1,String("hola"))
insert(T1,String("como"))
insert(T1,String("andas"))

T2 = Trie()
T2.root = TrieNode()
insert(T2,String("hola"))
insert(T2,String("andas"))
insert(T2,String("como"))

#mismoTrie(T1.root.children,T2.root.children)