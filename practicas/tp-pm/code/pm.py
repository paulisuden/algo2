from dictionary import *
import math
#########################################                  PARTE 1 
#EJERCICIO 2

"""Implementar una función que detecte si una cadena es un Palíndromo. La implementación debe responder a la siguiente especificación:
def isPalindrome(String):
	Descripción: Determina si la cadena es un palíndromo
Entrada: String con la cadena a evaluar.
Salida: Retorna True si la cadena es palíndromo, o False en caso contrario

La función es Palíndromo que devuelve True si una cadena es Palindromo y Falso en caso contrario. Nota: Una cadena es un palíndromo 
si se lee igual en ambos sentidos ej. anitalavalatina, radar.
"""

def isPalindrome(s):
    long = len(s)
    palindrome = True
    if len(s) % 2 != 0:
        r = math.trunc((long-1)/2)
    long = long-1
    for i in range(0,r):
        if s[i] != s[long]:
            palindrome = False
            break
        long -= 1
    return palindrome

#EJERCICIO 13    RABIN KARP
"""Implemente el algoritmo de Rabin-Karp estudiado. Para el mismo deberá implementarse una función de hash que dado un patrón p de tamaño m 
se resuelva en O(1). Considerar lo detallando en las presentación del tema correspondiente a las funciones de hash en Rabin-karp. """

def RK(p, t, q):
    m = len(p)
    n = len(t)
    d = n #long t
    hp = 0
    ht = 0
    h = 1

    for i in range(m-1):
        h = (h*d) % q

    # calculo hash value de p y t
    for i in range(m):
        hp = (d*hp + ord(p[i])) % q
        ht = (d*ht + ord(t[i])) % q

    #encuentro la subcadena en la cadena
    for i in range(n-m+1):
        if hp == ht:
            for j in range(m):
                if t[i+j] != p[j]: #los hash coinciden pero los caracteres no
                    break

            j += 1
            if j == m: #es porque no rompi el bucle anterior entonces encontre la subcadena
                print(p,"found at ", str(i+1))
                break

        if i < n-m: #si no, no podemos desplazarnos a la proxima subcadena porque no alcanza la long
            ht = (d*(ht-ord(t[i])*h) + ord(t[i+m])) % q #a ht le resto el termino de mayor orden y le sumo el de menor orden
            if ht < 0: #para que el hash no sea negativo
                ht += q
        else: return print("None")
"""
t = ((d * (t - v[carácter a eliminar] * h) + v[carácter a agregar] ) mod 13   
  = ((10 * (6 - 1 * 9) + 3 )mod 13   
  = 12 
Donde , h = d^(m-1) = 10 ^(3-1) = 100."""



#EJERCICIO 12     AEF
"""Implementar en pseudo-python un autómata de estados finitos para buscar
cualquier patrón P (consecutivo) en una cadena de texto T."""

def mostrarMatriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for i in range(0, filas):
        print("|", end="  ")
    for j in range(0, columnas):
        print(matrix[i][j], end="  ")
    print("|")


def construirAutomata(patron,m):

    automata = [[0] * 128 for _ in range(m + 1)] #tabla de estados inicializada en 0
    automata[0][ord(patron[0])] = 1 #paso inicial: primera transición del autómata 
    x = 0 #referencia para las transiciones cuando se encuentra un carácter que no coincide en el patrón
    for estado in range(1, m + 1): #para recorrer el patron en todas sus posiciones
        for c in range(128):
            automata[estado][c] = automata[x][c]
        if estado < m:
            automata[estado][ord(patron[estado])] = estado + 1 
            #Si el autómata se encuentra en el estado 'estado' y se encuentra el carácter patron[estado], se realizará una transición hacia el estado 'estado + 1'.
            x = automata[x][ord(patron[estado])] 
            #Esto garantiza que si se encuentra un carácter que no coincide en el patrón, el autómata regresará al estado anterior más largo coincidente para continuar la búsqueda.

    return automata


def AEF(texto, patron):
    n = len(texto)
    m = len(patron)
    automata = construirAutomata(patron,m)
    estado_actual = 0  #q
    for i in range(n):
        estado_actual = automata[estado_actual][ord(texto[i])]   # q = d(q,T[i])
        if estado_actual == m:
            print("Pattern occurs with shift ", i-len(patron)+1)
            break
    if estado_actual != m: 
        return print("None")


#EJERCICIO 14                       KMP

def KMP(t,p):
    n = len(t)
    m = len(p)
    pi = computePrefixFunction(p)
    q = 0
    for i in range(0,n):
        while q > 0 and p[q] != t[i]:
            q = pi[q-1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            print("Pattern occurs with shift", i-m+2)
            #q = pi[q]   -----> en caso de que haya q buscar mas de una ocurrencia
            break
    if q != m:
        return print("None")
    else:
        return

def computePrefixFunction(p):
    m = len(p)
    pi = [0]*m
    pi[0] = 0
    k = 0
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = pi[k]
        if p[k] == p[q]:
            k += 1
        pi[q] = k
    return pi

