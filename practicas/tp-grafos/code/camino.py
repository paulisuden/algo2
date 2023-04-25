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



"""    vertices[v].head.value = "g"
    vertices[v].head.nextNode.value = 0
    vertices[v].head.nextNode.nextNode.value = None"""