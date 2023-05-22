from linkedlist import *
import math 

"""
dictionary = Array(m,0)
Nota: dictionary puede ser redefinido para lidiar con las colisiones por encadenamiento

insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1) en el diccionario (dictionary). Resolver colisiones por 
encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción y el valor del key a insertar 
Salida: Devuelve D

delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo el key a eliminar.  
Entrada: El diccionario sobre el que se quiere realizar la eliminación y el valor del key que se va a eliminar.
Salida: Devuelve D"""

class dictionaryNode:
    value = None
    key = None
    nextNode = None
class dictionary:
    head = None

###########################################            GRAFOS            ##########################################################
#inserto los elementos en la posicion de su propio valor de key (pos==key)
def insertInOrder(dic, key, value):
    if dic[key] == None: #array en esa pos vacío
        #creo una lista                                        
        L = dictionary()
        addDic(L,key,value)                               
        dic[key] = L                                           
    else: #encadenamiento
        addDic(dic[key],key,value)
    return dic 

def insertInOrderBFS(BFS, i, key, value):
    #Inserta en el diccionario del nivel 0(hijos de raiz) al n
    if BFS[i] == None: 
        #creo una lista                                        
        L = dictionary()
        addDic(L,key,value)                               
        BFS[i] = L                                           
    else: #encadenamiento
        addDic(BFS[i],key,value)
    return BFS 














def searchGrafo(dic,key,value):
    #busca si hay una arista entre (key,value)
    if dic[key] == None:
        return False
    else: #busco key
        current = dic[key].head
        while current != None:
            if current.value == value:
                break
            current = current.nextNode
        if current == None:
            return False
        else:
            return True

def searchPos(dic,key):    #busco el slot en donde se encuentra determinada key
    pos = 0
    long = len(dic)
    while pos < long:
        if dic[pos] != None:
            current = dic[pos].head
        if current.key == key:
            return pos
            break
        pos += 1
    if pos == long:
        return None         





##########################################                              ##########################################################
def printDic(dic):
    long = len(dic)
    print("[", end= "")
    for i in range (0,long):
        if dic[i] == None:
            print("None,", end= "")
        else:
            current = dic[i].head
            print("{", end= "")
            while current != None:
                p = (current.key,current.value)
                print(p, end=" ")
                current = current.nextNode
            print("}", end= "")
            print(",", end= "")   
    print("]")
    print("")


def addDic(L,key,value):
  current = L.head
  nuevoNodo = Node()
  nuevoNodo.key = key
  nuevoNodo.value = value
  if current == None:
    L.head = nuevoNodo
  else:
    nuevoNodo.nextNode = current
    L.head = nuevoNodo


"""insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1) en el diccionario (dictionary). Resolver colisiones por 
encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción y el valor del key a insertar 
Salida: Devuelve D"""

def insert1(m,dic,key,value):
    pos = int(key % m) #metodo division
    if dic[pos] == None: #array en esa pos vacío
        #creo una lista                                        
        L = dictionary()
        addDic(L,key,value)                               
        dic[pos] = L                                          
    else: #encadenamiento
        addDic(dic[pos],key,value)
    return dic

def insert2(A,m,dic,key,value):
    pos = int(m*((key*A)%1)) #metodo multiplicacion
    if dic[pos] == None: #array en esa pos vacío
        #creo una lista                                        
        L = dictionary()
        addDic(L,key,value)                               
        dic[pos] = L                                          
    else: #encadenamiento
        addDic(dic[pos],key,value)
    return dic

"""search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra."""

def search1(m,dic,key):
    pos = key % m #funcion hash (k mod m)
    if dic[pos] == None:
        return None
    else: #busco key
        current = dic[pos].head
        while current != None:
            if current.key == key:
                break
            current = current.nextNode
        if current == None:
            return None
        else:
            return current.value

def search2(A,m,dic,key):
    pos = int(m*((key*A)%1)) #metodo multiplicacion
    if dic[pos] == None:
        return None
    else: #busco key
        current = dic[pos].head
        while current != None:
            if current.key == key:
                break
            current = current.nextNode
        if current == None:
            return None
        else:
            return current.value         
"""delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo el key a eliminar.  
Entrada: El diccionario sobre el que se quiere realizar la eliminación y el valor del key que se va a eliminar.
Salida: Devuelve D"""

def delete(m,dic,key):
    pos = key % m #funcion hash (k mod m)
    if dic[pos] == None:
        return None
    else: #busco key                                   
        current = dic[pos].head
        while current != None:
            if current.key == key:
                current.key = None
                current.value = None
                break
            current = current.nextNode
        return dic
    

"""Ejercicio 4
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, 
se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = ‘hola’ , P = ‘ahlo’
Salida: True, ya que P es una permutación de S

Ejemplo 2:
Entrada: S = ‘hola’ , P = ‘ahdo’
Salida: Falso, ya que P tiene al carácter ‘d’ que no se encuentra en S por lo que no es una permutación de S
"""


def permutation(s,p):
    if len(p) != len(s):
        return False
    else:
        m = ord("z")-ord("a") #m = tamaño del abecedario
        dic = [None]*m

        #inserto los caracteres del string p en el diccionario en la posicion de su propio valor de key (pos==key)
        for i in range (0,len(p)):
            key = (ord(p[i])-ord("a"))
            insertPosKey(dic, key, 1)

        #"inserto", comparo los caracteres del string s en el diccionario: 
        #si encuentro un caracter que ya existe, le resto 1 a value
        #si hay un caracter q no existe, quiere decir que no esta en la otra cadena y no son permutaciones
        for i in range (0,len(p)):
            key = (ord(s[i])-ord("a"))
            permutacion = comparoCaracteres(dic, key, 1)
            if permutacion == False:
                break

        if permutacion == True:
            for i in range (0,len(p)):
                key = (ord(p[i])-ord("a"))
                #reviso que todos los value == 0, caso contrario no es una permutación
                permutacion = esPermutacionFinal(dic, key)
                if permutacion == False:
                    break

        return permutacion 

#inserto los elementos en la posicion de su propio valor de key (pos==key)
def insertPosKey(dic, key, value):         
    if dic[key] == None: #array en esa pos vacío
        #creo una lista                                        
        L = dictionary()
        addDic(L,key,value)                               
        dic[key] = L                                          
    else: 
        dic[key].head.value += 1      #voy contando cuantas veces aparece la misma letra en la cadena
    return dic  

def comparoCaracteres(dic, key, value):
    if dic[key] == None: #Hay un caracter distinto
        return False                             
    else: 
        dic[key].head.value -= 1 #le resto 1 a value (objetivo: llegar a value = 0)
    return True  

def esPermutacionFinal(dic, key):
    if dic[key].head.value == 0:
        return True
    else:
        return False


"""Ejercicio 5
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. 
Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición
"""
def elementosUnicos(L):
    m = len(L)-1
    A = (math.sqrt(5)-1)/2
    dic = [None]*m
    for i in range(0,len(L)): #inserto los elementos en el diccionario
        current = L[i]
        if i != 0: #antes de insertar otro elemento me aseguro de que ya no se haya insertado
            duplicado = search2(A,m,dic,current)
            if duplicado != None: break #si ya se insertó antes, dejo de agregar elementos al diccionario y devuelvo False
        insert2(A,m,dic,current,current)
    
    if duplicado != None:
        return False
    else: return True #si nunca se encontro un elemento duplicado y se termino con la insercion, devuelvo True


"""Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. 
Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e 
implementar una función de hash apropiada para los códigos postales argentinos."""

def codigoPostal(dic,codigo):
    nro = (int(codigo[1])+int(codigo[2])+int(codigo[3])+int(codigo[4]))
    #la key es la suma de los numeros dddd y la suma de las letras en ASCII con peso segun su ubicacion
    key = (ord(codigo[0])*10^3+ord(codigo[5])*10^2+ord(codigo[5])*10+ord(codigo[5])+nro)
    m = 10007 #un numero primo grande
    insertValue_i(dic, key, codigo)
    return dic


"""Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. 
Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, 
su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). 
Justificar el coste en tiempo de la solución propuesta."""

def comprensionBasica(cadena):
    m = 122         #ord("z")
    #guardo cada caracter en la posicion del numero de su key, es decir que solo en su posicion pueden haber los mismos caracteres
    #en el campo value voy guardando las ocurrencias de cada letra por vez.
    dic = [None]*m
    newCadena = ""
    for i in range(0,len(cadena)):
        if i != 0:
            if cadena[i-1]!=cadena[i]: #si los caracteres cambian, cuento las ocurrencias del anterior y las agrego a la nueva cadena
                newCadena1 = cadenaComprimida(cadena[i-1],ord(cadena[i-1]),dic, "")
                newCadena += newCadena1
        key = ord(cadena[i])
        insertPosKey(dic, key, 1)
    if cadena[i-1]==cadena[i]:
        newCadena1 = cadenaComprimida(cadena[i-1],ord(cadena[i-1]),dic, "")
        newCadena += newCadena1
    else:
        newCadena1 = cadenaComprimida(cadena[i],ord(cadena[i]),dic, "")
        newCadena += newCadena1
    if len(newCadena) == len(cadena):
        return cadena
    else:
        return newCadena

def cadenaComprimida(caracter,key,dic,cadenaComprimida): #en esta cadena agrego el caracter y el numero de veces q se repite
    ocurrencia = ocurrencias(dic,key)
    cadenaComprimida += caracter
    cadenaComprimida += str(ocurrencia)
    return cadenaComprimida

def ocurrencias(dic,key): #obtengo la cant de ocurrencias y pongo el valor de esa letra en 0, por si vuelve a aparecer en otro caso
    ocurrencia = dic[key].head.value
    dic[key].head.value = 0
    return ocurrencia


"""Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la 
forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo 
de la solución propuesta.
Ejemplo
Entrada: S = ‘abracadabra’ , P = ‘cada’
Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)
"""
def subcadena(l,c):
    m = (len(l)-len(c)+1)
    final = (len(c))
    cadena=""
    dic = [None]*m
    pos = 0
    for i in range (0,m):
        cadena = l[i:i+final]
        insertValue_i(dic, pos, cadena)
        pos += 1
    indice = searchKey(m,dic,c)
    return indice


def insertValue_i(dic, key, value):         #INSERTO UN ELEMENTO EN EL POSICION pos QUE TENGO EN MI BUCLE FOR
    #creo una lista                                        
    L = dictionary()
    addDic(L,key,value)                               
    dic[key] = L                                          
    return dic  

def searchKey(m,dic,value):                 #busca la key a partir de tener como dato el value
    pos = 0                                 #la complejidad es O(m) ya que en el peor caso recorre todo el diccionario pero
    #busco value                            #este no tendra encadenamientos
    key = None
    for i in range(0,m):
        if dic[i].head.value == value:
            key = dic[i].head.key
            break
    return key


"""Ejercicio 9
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una 
tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo 
propuesto?"""

#Ingreso en la hash table el conjunto mas grande. Luego busco cada elemento del otro conjunto en la hash table, 
#si al menos uno no está, ya no es un subconjunto.

def S_subcjo_T(s,t):

    m = 19 #nro primo
    dic = [None]*m

    for i in range (0,len(t)):
        insert1(m,dic,t[i],t[i])

    for i in range(0,len(s)):
        subcjo = search1(m,dic,s[i])
        if subcjo == None:
            break
        
    if subcjo == None: return False
    else: return True

        