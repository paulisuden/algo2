from dictionary import *
from myqueue import *
from linkedlist import *
from mystack import *
"""Ejercicio 1
Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo con la representación por 
Lista de Adyacencia.

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una 
conexión entre dos vértices.
Salida: retorna el nuevo grafo"""

#EJERCICIO 1

def createGraphx2(LV, LA): # representa la arista(v,w) en la lista de ady de v y w
    grafo = [None]*len(LV)

    for i in range(0,len(LV)):
        for j in range(0,len(LA)):

            if LA[j][0] == LV[i]:
                insertInOrder(grafo, i, LA[j][1])
            elif LA[j][1] == LV[i]:
                insertInOrder(grafo, i, LA[j][0])

    #caso en que si hay algun vertice que no esta conectado con nadie(None) LO REPRESENTO CON -1
    for i in range(0,len(LV)):
        if grafo[i] == None:
            insertInOrder(grafo, i, -1)

    #printDic(grafo)
    return grafo

def createGraphx1(LV, LA): #representa la arista(v,w) en una sola lista de ady (de v ó w)
    grafo = [None]*len(LV)

    for i in range(0,len(LV)):
        for j in range(0,len(LA)):
            if LA[j][0] == LV[i]:
                insertInOrder(grafo, i, LA[j][1])
    #printDic(grafo)
    return grafo

#EJERCICIO 2
"""Implementar la función que responde a la siguiente especificación.
def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario."""

def existPath(grafo, v1, v2): 
    dfs = convertToDFSTree(grafo,v1)
    #busco en key = 0 porque esa es la posicion en el slot en donde voy a encontrar el arbol con raiz v1
    path = searchGrafo(dfs,0,v2)
    return path

"""Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario."""
#EJERCICIO 3
def isConnected(grafo): 
    dfs = convertToDFSTree(grafo,1)
    #printDic(dfs)
    long = len(dfs)
    cant = 0
    conexo = True
    #si mi hash DFS tiene mas de una lista en los slot, quiere decir que hay mas de un arbol y entonces no es conexo
    for i in range(0,long):
        if dfs[i] != None:
            cant += 1
        if cant > 1:
            conexo = False
            break
    return conexo
               

#EJERCICIO 4
"""Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""
def isTree(grafo): 
    ciclo = convertToBFSTree_CICLO(grafo, 1)
    if length(ciclo) == 0:
        return True
    else:
        return False
    
#misma funcion para convertir a un bfs solo que me devuelve si hay ciclo o no en vez de la lista BFS
def convertToBFSTree_CICLO(grafo, v):
    #ciclo = False
    ciclo = LinkedList()
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
                add(ciclo,(u,key)) 
                #ciclo = True
                       
            currentGrafo= currentGrafo.nextNode

        vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
    return ciclo



#EJERCICIO 5
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

#EJERCICIO 6
"""Implementar una función que dado un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol. 
Respetar la siguiente especificación. 
def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
"""
def convertTree(grafo):
    lista = convertToBFSTree_CICLO(grafo, 0)
    return lista

#EJERCICIO 7
"""Parte 2
Implementar la función que responde a la siguiente especificación.
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
"""

def countConnections(grafo):
    dfs = convertToDFSTree(grafo,1)
    #printDic(dfs)
    long = len(dfs)
    cant = 0
    conexo = True
    #si mi hash DFS tiene mas de una lista en los slot, quiere decir que hay mas de un arbol y entonces no es conexo
    for i in range(0,long):
        if dfs[i] != None:
            cant += 1
    return cant


#EJERCICIO 8
"""Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""

def convertToBFSTree(grafo, v):
    if isConnected(grafo) == True:
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
        
        #contador de niveles en el arbol
        j = -1

        #creo lista BFS donde voy a ir "armando" el arbol y Q donde voy a encolar y desencolar los vertices

        BFS = [None]*long
        Q = LinkedList()

        #encolo el primer vertice a Q
        enqueue(Q,v)

        while Q.head != None:
            j += 1
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
                    insertInOrderBFS(BFS, j, u, key)
                elif currentVertices.value == "g":
                    currentVertices.nextNode.nextNode.nextNode.value = True #hay ciclo (arco de retroceso)   
                    ciclo = True
                        
                currentGrafo= currentGrafo.nextNode

            vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
        return BFS
    
    else: return None

 
       
#EJERCICIO 9
"""Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
"""

def convertToDFSTree(grafo, u):
    long = len(grafo)
    #nuevo diccionario para guardar los vertices con su color, distancia y padre
    vertices = [None]*(long)
    arcosRetroceso = [None]*(long)
    arcoAvance = [None]*(long)
    arcoCruce = [None]*(long)
    arcosRetroceso_T_o_F = False
    #key = i, color vértice = w, distancia = None, padre = None
    #en una hash, en la posicion del numero del vertice, añado a la lista los datos anteriores

    time = 0
    j = -1

    for i in range (0,long):

        value = None
        insertInOrder(vertices, i, value) #inserto time final  NEXTNODE.NEXTNODE.NEXTNODE

        value = None
        insertInOrder(vertices, i, value) #inserto padre     NEXTNODE.NEXTNODE

        value = time
        insertInOrder(vertices, i, value) #inserto time      NEXTNODE

        value = "white"
        insertInOrder(vertices, i, value) #inserto color     HEAD

    DFS = [None]*(len(grafo)+1)
    for i in range (0,long):
        if vertices[i].head.value == "white":

            if i != 0: #si es igual a 0 es el caso de el primer vertice = RAIZ
                u = vertices[i].head.key
            j += 1
            DFS = convertToDFSTreeR(grafo,u,vertices,j,time,DFS,arcosRetroceso,arcosRetroceso_T_o_F,arcoAvance,arcoCruce)
    return DFS


def convertToDFSTreeR(grafo,u,vertices,j,time,DFS,arcosRetroceso,arcosRetroceso_T_o_F,arcoAvance,arcoCruce):

    time += 1
    vertices[u].head.value = "grey" 
    vertices[u].head.nextNode.value = time

    long = length(grafo[u])

    if grafo[u].head.value != -1:
        currentGrafo = grafo[u].head
        currentVertices = vertices[u].head

        for i in range(0,long):
            key = currentGrafo.value
    
            if vertices[key].head.value == "white":
                vertices[key].head.nextNode.nextNode.value = u
                insertInOrderBFS(DFS, j, u, key)
                convertToDFSTreeR(grafo,key,vertices,j,time,DFS,arcosRetroceso,arcosRetroceso_T_o_F,arcoAvance,arcoCruce)
            #ARCO RETROCESO
            elif vertices[key].head.value == "grey":
                arcosRetroceso_T_o_F = True
                insertInOrder(arcosRetroceso, key, u)
                insertInOrder(arcosRetroceso, u, key)
            #ARCO AVANCE O CRUCE
            elif vertices[key].head.value == "black":
                #si una arista de avance o cruce conecta dos componentes conexos quiere decir que existe una ruta entre ellos que NO pasa
                #por la raíz del arbol DFS
                
                #Son aristas (u,v) que no son parte del árbol y conectan u a un descendiente v (vértice sucesor).
                if vertices[u].head.nextNode.value < vertices[key].head.nextNode.value:
                    insertInOrder(arcoAvance, u, key)
                else:
                #Pueden ir entre vértices dentro de un mismo árbol (siempre que v no sea ancestro de u), o entre distintos árboles DFS.            
                    insertInOrder(arcoCruce, u, key)

            currentGrafo = currentGrafo.nextNode
            

        currentVertices.value = "black"
        time += 1
        currentVertices.nextNode.nextNode.nextNode.value = time

    else:
        #caso en que un vertice no esta conectado con ningun otro vertice
        key = u
        insertInOrderBFS(DFS, j, u, None)
    return DFS


#EJERCICIO 10
"""
Implementar la función que responde a la siguiente especificación.
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. 
En caso de que no exista camino se retorna la lista vacía.
Con bfs"""
def BFS_Vertices(grafo, v):
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
        
        #contador de niveles en el arbol
        j = -1

        #creo lista BFS donde voy a ir "armando" el arbol y Q donde voy a encolar y desencolar los vertices

        BFS = [None]*long
        Q = LinkedList()

        #encolo el primer vertice a Q
        enqueue(Q,v)

        while Q.head != None:
            j += 1
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
                    insertInOrderBFS(BFS, j, u, key)
                elif currentVertices.value == "g":
                    currentVertices.nextNode.nextNode.nextNode.value = True #hay ciclo (arco de retroceso)   
                    ciclo = True
                        
                currentGrafo= currentGrafo.nextNode

            vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
        return vertices

def convertToBFSTree_NoConexo(grafo, v):

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
        
        #contador de niveles en el arbol
        j = -1

        #creo lista BFS donde voy a ir "armando" el arbol y Q donde voy a encolar y desencolar los vertices

        BFS = [None]*long
        Q = LinkedList()

        #encolo el primer vertice a Q
        enqueue(Q,v)

        while Q.head != None:
            j += 1
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
                    insertInOrderBFS(BFS, j, u, key)
                elif currentVertices.value == "g":
                    currentVertices.nextNode.nextNode.nextNode.value = True #hay ciclo (arco de retroceso)   
                    ciclo = True
                        
                currentGrafo= currentGrafo.nextNode

            vertices[u].head.value = "b" #termino de visitar todos los nodos adyacentes a u 
        return BFS
    

def bestRoad(grafo,s,v):
    vertices = BFS_Vertices(grafo,s)
    bestRoad_R(s,v,vertices)

def bestRoad_R(s,v,vertices):
    if v == s:
        print(s)
        return 
    elif vertices[v].head.nextNode.nextNode.value == None:
        return print(None)
    else:
        bestRoad_R(s,vertices[v].head.nextNode.nextNode.value,vertices)
        print(v)

