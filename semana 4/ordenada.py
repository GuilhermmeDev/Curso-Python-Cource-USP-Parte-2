def ordena(lista):
    fim = len(lista)
    lista2 = lista[:]
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista2[i],lista2[pos_menor] = lista2[pos_menor],lista2[i]
    return lista2
def ordenada(lista):
    if lista == ordena(lista):
        return True
    else:
        return False

lista=[1,2,3,4,5]   
ordenada(lista)