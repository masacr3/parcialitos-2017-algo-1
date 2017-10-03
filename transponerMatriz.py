def transponerMatriz(matriz):
    """ transpone una matriz cualquiera
        matriz = lista de lista
        pre: se asume q la matriz contiene por lo menos una fila
    """
    lencol = len(matriz[0])
    lenfila = len(matriz)
    
    matrizTranspuesta = []
    
    for j in range(lencol):
        fila = []
        
        for i in range(lenfila):
            fila.append( matriz[i][j])
        
        matrizTranspuesta.append(fila)
    
    return matrizTranspuesta
