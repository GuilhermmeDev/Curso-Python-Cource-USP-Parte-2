def maiusculas(frase):
    numLetras = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    maiu = ''
    for l in frase:
        if ord(l) in numLetras:
            maiu += l
    return maiu

frase = 'Programamos em Python 3'
maiusculas(frase)