from algo1 import * 


def search(Array, element): 
	for i in range(len(Array)): 
		if Array[i] == element: 
			return i 
	return

def insert(Array,element,position):
  if len(Array) > position-1:
    Array[len(Array)-1] = None 
    
    for i in range (0, (len(Array)-position+1)): 
      Array[len(Array) - (i+1)] = Array[(len(Array)-1) - (i+1)] 
      
    Array[position-1] = element 
    return print('Posición:', position) 
  else: 
    return print('None') 
    
def delete(Array, element): 
	position = search(Array, element) 
	if position == None: return 
	for i in range(position, len(Array)): 
		if i+1 < len(Array): 
			Array[i] = Array[i+1] 
		else:
			Array[i] = None 
	return position
def length(Array): 
  contador = 0
  for i in range (0, len(Array)):
    if Array[i] != None:
      contador += 1
  return contador
      
  
    
    