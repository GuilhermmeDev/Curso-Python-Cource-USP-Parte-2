def busca(lista,e):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro+ultimo)//2
        print(meio)
        if lista[meio] == e:
            return meio
        else:
            if lista[meio] < e:
                primeiro = meio + 1
            else:
                ultimo = meio - 1
    return False
