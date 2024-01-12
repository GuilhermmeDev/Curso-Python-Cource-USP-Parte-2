class Ordenadores:
    def selecao_direta(self,lista):
        for i in range(len(lista)-1):
            pos_min = i
            for j in range(i+1,len(lista)):
                if lista[j] < lista[pos_min]:
                    pos_min = j
            lista[i],lista[pos_min] = lista[pos_min],lista[i]
        return lista
    
    def bolha(self,lista):
        for i in range(len(lista)-1,0,-1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        return lista
    
    def bolha_curta(self,lista):
        for i in range(len(lista)-1,0,-1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
                    trocou = True
            if not trocou:
                return
