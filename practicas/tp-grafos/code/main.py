from dictionary import *
from graph import *

LV = [0,1,2,3,4,5]
LA = [(0,1),(0,2),(1,3),(3,5)]
grafo = createGraphx2(LV, LA)
printDic(grafo)

"""print("")
print("Existe camino entre v1 y v2?")
print(existPath(grafo, 2,3))"""


print("")
print("Es un grafo completo?")
LV = [0,1,2,3,4,5]
LA = [(0,0),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
grafo1 = createGraphx2(LV, LA)
print(isComplete(grafo1))

print("")
print("Es un grafo conexo?")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(2,3)]
grafo2 = createGraphx2(LV, LA)
print(isConnected(grafo2))



print("")
print("Es un arbol?")
print(isTree(grafo2))


print("")
print("BFS LISTA")
LV = [0,1,2,3,4,5,6,7,8,9,10]
LA = [(0,1),(1,2),(4,1),(0,3),(2,3),(7,8),(7,9),(9,5),(5,2),(6,1),(10,3)]
grafo3 = createGraphx2(LV, LA)
BFS = (convertToBFSTree(grafo3, 2))
if BFS != None:
    printDic(BFS)

print("")
print("DFS LISTA")
LV = [0,1,2,3,4,5,6,7,8,9,10]
LA = [(0,0),(1,2),(4,1),(0,3),(2,3),(7,8),(7,9)]
grafo3 = createGraphx2(LV, LA)
DFS = (convertToDFSTree(grafo3, 2))
printDic(DFS)

print("")
print("COUNT CONNECTIONS (Distintos conjuntos conexos en un mismo grafo)")
print("")
print(countConnections(grafo3))

print("")
print("mejor camino")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(1,3),(1,4),(2,4)]
grafo4 = createGraphx2(LV, LA)
BFS = (convertToBFSTree(grafo4, 0))
printDic(BFS)

print("mejor camino")
printLista((bestRoad(grafo3, 7,8)))