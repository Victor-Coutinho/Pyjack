from tupy import *

class game():
    def __init__(self,jogador,dealer,baralho,dealer_score,jogador_score,): 
        self.jogador = jogador
        self.dealer = dealer
        self.baralho = baralho
        self.dealer_score = dealer_score
        self.jogador_score = jogador_score
	
        
    def start(self):
        """Inicia o jogo"""
        if self.jogador.total <= 21:
            while self.dealer.total < self.jogador.total:
                carta = self.baralho.pega_carta_do_topo()
                self.dealer.pegar_outra_carta(carta)
                self.dealer_score.atualiza(carta.valor)
                "verificar se o dealer tem um A"
                if self.dealer.temAs and self.dealer.total > 21:
                    self.dealer.total -= 10
                    self.dealer.temAs = False
                    self.dealer_score.decrementa(10)
		
        if self.dealer.total > 21:
            toast("Jogador Ganhou", )
        elif self.jogador.total > 21:
            toast("Dealer Ganhou",)
        elif self.jogador.total > self.dealer.total:
            toast("Jogador Ganhou",)
        elif self.jogador.total < self.dealer.total:
            toast("Dealer Ganhou",)
        else:
            toast("Empate",)
