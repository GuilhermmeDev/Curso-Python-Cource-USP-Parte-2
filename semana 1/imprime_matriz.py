def imprime_matriz(matriz):
    for l in matriz:
        for pos,c in enumerate(l):
            if pos == len(l)-1:
                print(c)
            else:
                print(c,end=' ')
mat = [[1,2,3],[4,5,6]]
imprime_matriz(mat)