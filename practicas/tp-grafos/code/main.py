from dictionary import *
from graph import *

LV = [0,1,2,3,4,5]
LA = [(0,1),(0,2),(1,3),(3,5),(5,2)]
grafo = createGraphx2(LV, LA)

print("")
print("Existe camino entre v1 y v2?")
print(existPath(grafo, 2, 3))


print("")
print("Es un grafo completo?")
LV = [0,1,2,3,4,5]
LA = [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
grafo1 = createGraphx2(LV, LA)
print(isComplete(grafo1))

print("")
print("Es un grafo conexo?")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(2,3),(3,4)]
grafo2 = createGraphx2(LV, LA)
print(existPath(grafo2, 0, 3))
print(isConnected(grafo2))


print("")
print("Es un arbol?")
print(isTree(grafo2))




print("")
print("BFS LISTA")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(4,1),(0,3),(2,3),(3,4)]
grafo3 = createGraphx2(LV, LA)
printLista(convertToBFSTree(grafo3, 2))
