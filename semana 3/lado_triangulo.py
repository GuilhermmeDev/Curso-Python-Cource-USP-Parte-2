class Triangulo:

    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b and self.a != self.c or self.b != self.a and self.b == self.c or self.c == self.a and self.c != self.b:
            return 'isósceles'
        elif self.a != self.b != self.c:
            return 'escaleno'
        
    
