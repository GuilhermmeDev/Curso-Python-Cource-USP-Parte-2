def dimensoes(matriz):
    Cl = 0  #contador de linha
    Cc = 0  #contador de coluna
    for i in matriz:
        Cl += 1
        Cc = len(i)
    print(str(Cl) + 'X' + str(Cc))

minha_matriz = [[1],[2],[3]]
dimensoes(minha_matriz)
