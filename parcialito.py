#1.
#   a.To tablet
#        x = -33 .... 92
#        ( x // 2 ) - 3 = -19 .. 43 
   
#    b.Implementacion con While

#   b.While implementacion:
#
#   y = -33
#   while ( y < 99 ):
#       x = y
#       print("valor...",x)
#       x = ( x // 2 ) - 3
#       print("valor...",x)
#       y += 1

#2.
def snake_a_camel(snake_case):
    """ Devuelve una cadena en formato CamelCase
        [snake_case = str] 
        pre: se asume que la cadena snake_case tiene el formato SNAKE_CASE
    """
    if snake_case == "":
        return 
    
    listas_palabras = snake_case.split("_")
    palabras = []
    
    for palabra in listas_palabras:
        palabras.append( palabra[0].upper()+palabra[1:] )
    
    return "".join(palabras)
        
#3.
def maximos_columna(matriz):
    """ Devuelve una lista con los maximos de cada columna
        [matriz = lista de lista]
        pre: se asume que la matriz contiene al menos una fila y un elemento
    """
    if matriz == []:
        return
    
    max_columnas = []
    for col in range( len( matriz[0] ) ):
        fila = []
        
        for fil in range( len( matriz ) ):
            fila.append( matriz[fil][col] )
            
        max_columnas.append( max(fila) )
     
     return max_columnas
     
