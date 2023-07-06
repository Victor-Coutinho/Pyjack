from Jogador import *
from tupy import *
from score import *
from game import *

class button(Image):
	def __init__(self) -> None:
		self.file = 'button.png'
		self.x = 150
		self.y = 400
		
	def update(self):
		"""Verifica se o botão foi clicado e adiciona uma carta ao jogador verificando se o jogador tem um A"""
		if  0< mouse.x < 275 and 365 < mouse.y < 425 :
			if  mouse.is_button_just_down() and jogador1.total < 21:
				cartax = baralho.pega_carta_do_topo()
				jogador1.pegar_outra_carta(cartax)
				jogador_score.atualiza(cartax.valor)
				if jogador1.temAs and jogador1.total > 21:
					jogador1.total -= 10
					jogador1.temAs = False
					jogador_score.decrementa(10) 
			
class stand(Image):
	def __init__(self) -> None:
		self.file = 'stand.png'
		self.x = 150
		self.y = 460

	def update(self) -> None:
		"""Verifica se o botão foi clicado e inicia o jogo"""
		if 0 < mouse.x < 275 and 425 < mouse.y < 475:
			if mouse.is_button_just_down():
				dealer.carta2.file = dealer.carta2.nome + " of " + carta2.naipe + ".png"
				dealer_score.atualiza(dealer.carta2.valor)
				game.start()
				
#--------definindo as imagens---------------
fundo = Fundo()
botão = button()
stand = stand()

#--------definindo as cartas----------------
baralho = Baralho()
baralho.embaralha()

#--------definindo o jogador-------------
carta1 = baralho.pega_carta_do_topo()
carta2 = baralho.pega_carta_do_topo()
jogador1 = jogador(carta1,carta2)
jogador_score = Score(100,320)
jogador_score.atualiza(jogador1.total)

#--------definindo o dealer-------------
carta3 = baralho.pega_carta_do_topo()
carta4 = baralho.pega_carta_do_topo()
dealer = Dealer(carta3,carta4)
dealer_score = Score(100,60)
dealer_score.atualiza(dealer.total - carta4.valor)

#--------definindo o game-------------
game = game(jogador1,dealer,baralho,dealer_score,jogador_score)





run(globals())
