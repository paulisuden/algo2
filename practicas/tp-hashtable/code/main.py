from dictionary import *
import math


m = 7
dic = [None]*m
insert1(m,dic,5,"cinco")
insert1(m,dic,7,"siete")
insert1(m,dic,34,"trinta y cuatro")
insert1(m,dic,57,"cincuenta y siete")
insert1(m,dic,29,"veintinueve")
print("")


print("SEARCH:")
print(search1(m,dic,5))
print(search1(m,dic,57))
print("")

print("DELETE:")
(delete(m,dic,5))
(delete(m,dic,57))
print("")

print("Permutacion ejercicio 4")  
print(permutation("hola","aloh"))
print("")

print("Elementos unicos lista ejercicio 5") 
L = [1,5,6,7,8,5]
print(L)
print(elementosUnicos(L))
print("")

print("Comprension basica ejercicio 6") 
cadena = "aabcccccaaa"
print(cadena)
print(comprensionBasica("aabcccccaaa"))
print("")

print("subcadena ejercicio 8") 
print("abracadabra, cada")
print(subcadena("abracadabra","cada"))
print("")

print("¿S ⊆ T?: Ejercicio 9")
S = [2,3,4,5]
T = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(S)
print(T)
print(S_subcjo_T(S,T))
print("")

