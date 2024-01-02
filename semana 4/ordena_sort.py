def ordena(lista):
    tam_lista = len(lista)
    for i in range(tam_lista):
        pos_menor = i
        for j in range(i+1,tam_lista):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
    return lista

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ordena(lista)