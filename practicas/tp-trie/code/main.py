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

print(delete(T,String("ca")))
#print(search(T,String("ca")))
