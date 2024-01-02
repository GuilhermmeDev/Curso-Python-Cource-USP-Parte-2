class Triangulo:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.tuple = (a,b,c)
    def semelhantes(self,triangulo):
        c = 0
        for pos,n in enumerate(self.tuple):
            if self.tuple[pos] % triangulo.tuple[pos] == 0 or triangulo.tuple[pos] % self.tuple[pos] == 0:
                c += 1
        return c == 3
