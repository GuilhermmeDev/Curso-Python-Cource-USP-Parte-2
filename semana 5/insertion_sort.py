def insertion_sort(lista):
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > k:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = k
    return lista
