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
print("")
print("Ejercicio 4: busco palabras con patron P")

insert(T,String("Put"))
insert(T,String("Pet"))
insert(T,String("Pita"))
insert(T,String("Pan"))
insert(T,String("Pau"))
printLista(buscoPatron(T,"P",3))

"""#Ejercicio 5

T1 = Trie()
T1.root = TrieNode()
insert(T1,String("corazon"))
insert(T1,String("como"))
insert(T1,String("andas"))
insert(T1,String("holanda"))
insert(T1,String("hola"))

T2 = Trie()
T2.root = TrieNode()
insert(T2,String("como"))
insert(T2,String("andas"))
insert(T2,String("corazon"))
insert(T2,String("holanda"))
insert(T2,String("hola"))
print(arbolesIdenticos(T1,T2))

#Ejercicio 6

print("")
print("¿Cadenas Invertidas?")
T3 = Trie()
T3.root = TrieNode()
insert(T3,String("abcd"))
insert(T3,String("fdsa"))
insert(T3,String("holi"))
insert(T3,String("dcba"))
insert(T3,String("asdf"))
print(cadenasInvertidas(T3))

#Ejercicio 7

print("")
print("Autocompletar")
T7 = Trie()
T7.root = TrieNode()
insert(T7,String("groenlandia"))
insert(T7,String("groenlandes"))
insert(T7,String("madera"))
insert(T7,String("mamá"))
insert(T7,String("semaforo"))
print("Autocompletar ma (madera y mamá)")
cadena = "ma"
print(autoCompletar(T7,cadena))
print("Autocompletar groen (groenlandia y groenlandes)")
cadena = "groen"
print(autoCompletar(T7,cadena))
print("Autocompletar sem (semaforo)")
cadena = "sem"
print(autoCompletar(T7,cadena))"""