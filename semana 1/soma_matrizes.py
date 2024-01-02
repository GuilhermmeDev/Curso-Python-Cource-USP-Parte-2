def dimensoes(matriz):
    Cl = 0  #contador de linha
    Cc = 0  #contador de coluna
    for i in matriz:
        Cl += 1
        Cc = len(i)
    return Cl,Cc

def soma_matrizes(m1,m2):
    matriz = [] #lista vazia para a nova matriz
    if dimensoes(m1) == dimensoes(m2):
        for posL,l in enumerate(m1):   # posL significa a posição da linha a ser iterada.
            linha = []
            for posC,c in enumerate(l):  # posC significa a posição da coluna a ser iterada.
                s = m1[posL][posC] + m2[posL][posC]   # o termo somado será igual a lista da primeira matriz na posição da linha com a coluna iterada mais a segunda matriz nessa mesma posição.
                linha.append(s)
            matriz.append(linha)
        return matriz
    elif dimensoes(m1) != dimensoes(m2):  #comparação das dimensões das duas matrizes
        return False
        

m1 = [[1], [2],[3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)