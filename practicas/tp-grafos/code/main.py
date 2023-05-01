from dictionary import *
from graph import *


print("EJERCICIO 1")
LV = [0,1,2,3,4,5]
LA = [(0,1),(0,2),(1,3)]
grafo = createGraphx2(LV, LA)
printDic(grafo)
print("")


print("EJERCICIO 2")
print("Exist path?")
print(existPath(grafo, 1, 4))

print("")
print("EJERCICIO 3")
print("Es un grafo conexo?")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(2,3)]
grafo2 = createGraphx2(LV, LA)
print(isConnected(grafo2))


print("")
print("EJERCICIO 4")
print("Es un arbol?")
print(isTree(grafo2))

print("EJERCICIO 5")
print("")
print("Es un grafo completo?")
LV = [0,1,2,3,4,5]
LA = [(0,0),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
grafo1 = createGraphx2(LV, LA)
print(isComplete(grafo1))

print("")
print("EJERCICIO 6")
print("convertir a arbol. aristas q hay que borrar:")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(2,3),(3,0),(1,3),(3,4)]
grafo6 = createGraphx2(LV, LA)
lista = convertTree(grafo6)
printLista(lista)

print("")
print("EJERCICIO 7")
LV = [0,1,2,3,4,5,6,7,8,9,10]
LA = [(0,0),(1,2),(4,1),(0,3),(2,3),(7,8),(7,9)]
grafo7 = createGraphx2(LV, LA)
print("COUNT CONNECTIONS (Distintos conjuntos conexos en un mismo grafo)")
print("")
print(countConnections(grafo7))


print("")
print("EJERCICIO 8")
print("BFS LISTA")
LV = [0,1,2,3,4,5,6,7,8,9,10]
LA = [(0,1),(1,2),(4,1),(0,3),(2,3),(7,8),(7,9),(9,5),(5,2),(6,1),(10,3)]
grafo3 = createGraphx2(LV, LA)
BFS = (convertToBFSTree(grafo3, 2))
if BFS != None:
    printDic(BFS)

print("")
print("DFS LISTA")
print("EJERCICIO 9")
LV = [0,1,2,3,4,5,6,7,8,9,10]
LA = [(0,0),(1,2),(4,1),(0,3),(2,3),(7,8),(7,9)]
grafo3 = createGraphx2(LV, LA)
DFS = (convertToDFSTree(grafo3, 2))
printDic(DFS)


print("")
("EJERCICIO 10")
print("mejor camino")
LV = [0,1,2,3,4]
LA = [(0,1),(1,2),(2,3),(3,4)]
grafo10 = createGraphx2(LV, LA)
bestRoad(grafo10,0,4)
