def sao_multiplicaveis(m1,m2):
    nLinhas = len(m2)
    for l in m1:
        nCol = len(l)
    if nLinhas == nCol:
        return True
    else:
        return False
    
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1,m2))