from dictionary import *
from myqueue import *
from linkedlist import *
"""Ejercicio 1
Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo con la representación por 
Lista de Adyacencia.

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una 
conexión entre dos vértices.
Salida: retorna el nuevo grafo"""

def createGraphx2(LV, LA): # representa la arista(v,w) en la lista de ady de v y w
    grafo = [None]*len(LV)

    for i in range(0,len(LV)):
        for j in range(0,len(LA)):

            if LA[j][0] == LV[i]:
                insertInOrder(grafo, i, LA[j][1])
            elif LA[j][1] == LV[i]:
                insertInOrder(grafo, i, LA[j][0])
    printDic(grafo)
    return grafo

def createGraphx1(LV, LA): #representa la arista(v,w) en una sola lista de ady (de v ó w)
    grafo = [None]*len(LV)

    for i in range(0,len(LV)):
        for j in range(0,len(LA)):
            if LA[j][0] == LV[i]:
                insertInOrder(grafo, i, LA[j][1])
    printDic(grafo)
    return grafo


"""def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario."""

#(utilizo createGraphx1)

def existPath_R(grafo,L, v1, v2,current):
    #lista de V1
    if current == None: #recorri toda la lista y no encontre un camino    (CASO BASE)
        return False
    else:
        new_v1 = current.value #new_v1 = key:  voy a buscar en la lista de mi nueva key a v2

        if searchGrafo(grafo,new_v1,v2) == True: 
            return True
        else: # si no lo encontre paso a la siguiente key de la lista inicial L
            return existPath_R(grafo,L, v1, v2, current.nextNode)



def existPath(grafo, v1, v2):
    if searchGrafo(grafo,v1,v2) == True: 
        return True
    else:
        if grafo[v1] == None:  #si v1 no esta conectado con ningun vértice
            return False
        else:
            L = grafo[v1] #la lista que voy a recorrer es en la cual la key = v1
            camino = existPath_R(grafo,L, v1, v2, L.head)
            return camino


"""Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario."""

def isConnected(grafo): 
    cantVertices = len(grafo)-1

    for i in range (0,cantVertices):
        for j in range(i,cantVertices):
            if i != j:
                if existPath(grafo, i, j) == False:
                    return False
                    break


"""Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""
def isTree(grafo): 
    ciclo = convertToBFSTree_CICLO(grafo, 1)
    if ciclo == True:
        return False
    elif ciclo == False:
        return True
#misma funcion para convertir a un bfs solo que me devuelve si hay ciclo o no en vez de la lista BFS
def convertToBFSTree_CICLO(grafo, v):
    ciclo = False
    long = len(grafo)+1
    #nuevo diccionario para guardar los vertices con su color, distancia y padre
    vertices = [None]*(long)
    #key = i, color vértice = w, distancia = None, padre = None
    #en una hash, en la posicion del numero del vertice, añado a la lista los datos anteriores
    for i in range (0,long):
        value = False
        insertInOrder(vertices, i, value) #inserto arco de retroceso (ciclo)       
        value = None
        insertInOrder(vertices, i, value) #inserto padre
        value = None
        insertInOrder(vertices, i, value) #inserto distancia
        value = "w"
        insertInOrder(vertices, i, value) #inserto color

    #al vertice v le doy color = grey, distancia = 0 y padre = None ya esta predefinido antes
    vertices[v].head.value= "g"
    vertices[v].head.nextNode.value= 0
    
    #creo lista BFS donde voy a ir "armando" el arbol y Q donde voy a encolar y desencolar los vertices

    BFS = LinkedList()
    Q = LinkedList()
    #añado la raiz al arbol (v)
    addInOrder(BFS,v)
    #encolo el primer vertice a Q
    enqueue(Q,v)

    while Q.head != None:
        u = dequeue(Q)
        #voy a recorrer la lista de adyacencia del vertice u en la hash
        currentGrafo = grafo[u].head
        long = length(grafo[u])

        for i in range(0,long):
            key = currentGrafo.value
            currentVertices = vertices[key].head
            if currentVertices.value == "w":
                currentVertices.value = "g" #color
                currentVertices.nextNode.value = (vertices[u].head.nextNode.value + 1) #distancia
                currentVertices.nextNode.nextNode.value = u #padre
                enqueue(Q,key)
                addInOrder(BFS,key)

            elif currentVertices.value == "g":
                currentVertices.nextNode.nextNode.nextNode.value = True #hay ciclo (arco de retroceso)   
                ciclo = True
                break
                       
            currentGrafo= currentGrafo.nextNode

        vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
    return ciclo




"""Ejercicio 5 
Implementar la función que responde a la siguiente especificación.
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.
"""
#(considerando que el grafo es simple)
def isComplete(grafo):  
    cantVertices = len(grafo)-1
    for i in range(0,cantVertices):
        if length(grafo[i]) != cantVertices:
            return False
            break
    return True

"""Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""

def convertToBFSTree(grafo, v):
    ciclo = False
    long = len(grafo)+1
    #nuevo diccionario para guardar los vertices con su color, distancia y padre
    vertices = [None]*(long)
    #key = i, color vértice = w, distancia = None, padre = None
    #en una hash, en la posicion del numero del vertice, añado a la lista los datos anteriores
    for i in range (0,long):
        value = False
        insertInOrder(vertices, i, value) #inserto arco de retroceso (ciclo)       
        value = None
        insertInOrder(vertices, i, value) #inserto padre
        value = None
        insertInOrder(vertices, i, value) #inserto distancia
        value = "w"
        insertInOrder(vertices, i, value) #inserto color

    #al vertice v le doy color = grey, distancia = 0 y padre = None ya esta predefinido antes
    vertices[v].head.value= "g"
    vertices[v].head.nextNode.value= 0
    
    #creo lista BFS donde voy a ir "armando" el arbol y Q donde voy a encolar y desencolar los vertices

    BFS = LinkedList()
    Q = LinkedList()
    #añado la raiz al arbol (v)
    addInOrder(BFS,v)
    #encolo el primer vertice a Q
    enqueue(Q,v)

    while Q.head != None:
        u = dequeue(Q)
        #voy a recorrer la lista de adyacencia del vertice u en la hash
        currentGrafo = grafo[u].head
        long = length(grafo[u])

        for i in range(0,long):
            key = currentGrafo.value
            currentVertices = vertices[key].head
            if currentVertices.value == "w":
                currentVertices.value = "g" #color
                currentVertices.nextNode.value = (vertices[u].head.nextNode.value + 1) #distancia
                currentVertices.nextNode.nextNode.value = u #padre
                enqueue(Q,key)
                addInOrder(BFS,key)

            elif currentVertices.value == "g":
                currentVertices.nextNode.nextNode.nextNode.value = True #hay ciclo (arco de retroceso)   
                ciclo = True
                       
            currentGrafo= currentGrafo.nextNode

        vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
    return BFS


        

"""Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
"""

def convertToDFSTree(Grafo, v):


    

