def encontra_impares(lista):
    imp = []
    if len(lista) == 1:
        if lista[0] % 2 == 1:
            imp.append(lista[0])
            return imp
        else:
            return []
    else:
        if lista[0] % 2 == 1:
            imp.append(lista[0])
        lista.pop(0)
        imp = imp + encontra_impares(lista)
    return imp
    
l = [5,2,4,6,9,13]
print(encontra_impares(l))
    