from trie import *


class Trie:
	root = None
class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

#cadena = String("Hola")
insert(T,String("Hola"))
insert(T,String("Holi"))
insert(T,String("Holu"))

print(search(T,String("Hola")))