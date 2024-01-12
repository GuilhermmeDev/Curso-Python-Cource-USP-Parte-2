import ordenadores
import pytest
import conta_tempos
class Testa_Ordenador:

    @pytest.fixture
    def o(self):
        return ordenadores.Ordenadores()
    
    @pytest.fixture
    def l_quase(self):
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)
    
    @pytest.fixture
    def l_aleatoria(self):   # lista aleatoria
        c = conta_tempos.ContaTempos()
        return c.lista_aleatoria(100)
    
    @pytest.fixture
    def l_qord(self):  # Lista quase ordenada
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)
    
    def esta_ordenada(self,l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True
    
    def test_bolha_curta_aleat(self,o,l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selec_dir_aleat(self,o,l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_qord(self,o,l_qord):
        o.bolha_curta(l_qord)
        assert self.esta_ordenada(l_qord)
    
    def test_selec_dir_qord(self,o,l_qord):
        o.selecao_direta(l_qord)
        assert self.esta_ordenada(l_qord)