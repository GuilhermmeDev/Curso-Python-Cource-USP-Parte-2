from random import randint

def lista_grande(n):
    lista = []
    for i in range(n):
        n = randint(1,1000000)
        lista.append(n)
    return lista
print(lista_grande(100))
