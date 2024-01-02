def conta_letras(frase,contar="vogais"):
    c = 0
    vogais = ['A','a','E','e','I','i','O','o','U','u']
    for l in frase:
        if contar == "vogais":
            if l in vogais:
                c += 1
        elif contar == "consoantes":
            if l not in vogais:
                c += 1
    return c

conta_letras('programamos em python','consoantes')