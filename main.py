from Jogador import *
from tupy import *
from score import *

class button(Image):
	def __init__(self) -> None:
		self.file = 'button.png'
		self.x = 150
		self.y = 400
		
	def update(self):
		if  0< mouse.x < 275 and 365 < mouse.y < 425 :
			if  mouse.is_button_just_down() and jogador1.total < 21:
				cartax = baralho.pega_carta_do_topo()
				jogador1.pegar_outra_carta(cartax)
				jogador_score.atualiza(cartax.valor)
			
class stand(Image):
	def __init__(self) -> None:
		self.file = 'stand.png'
		self.x = 150
		self.y = 460

	def update(self) -> None:
		if 0 < mouse.x < 275 and 425 < mouse.y < 475:
			if mouse.is_button_just_down():
				dealer.carta2.file = dealer.carta2.nome + " of " + carta2.naipe + ".png"
				dealer_score.atualiza(dealer.carta2.valor)
				while dealer.total < 17 or dealer.total < jogador1.total:
					carta = baralho.pega_carta_do_topo()
					dealer.pegar_outra_carta(carta)
					dealer_score.atualiza(carta.valor)
				print(dealer.total)
				if dealer.total > 21:
					toast("Jogador Ganhou", )
				elif jogador1.total > 21:
					toast("Dealer Ganhou",)
				elif jogador1.total > dealer.total:
					toast("Jogador Ganhou",)
				elif jogador1.total < dealer.total:
					toast("Dealer Ganhou",)
				else:
					toast("Empate",)

fundo = Fundo()
botão = button()
stand = stand()
baralho = Baralho()
baralho.embaralha()
carta1 = baralho.pega_carta_do_topo()
carta2 = baralho.pega_carta_do_topo()
jogador1 = jogador(carta1,carta2)
jogador_score = Score(100,320)
jogador_score.atualiza(jogador1.total)
carta3 = baralho.pega_carta_do_topo()
carta4 = baralho.pega_carta_do_topo()
dealer = Dealer(carta3,carta4)
dealer_score = Score(100,60)
dealer_score.atualiza(dealer.total - carta4.valor)





run(globals())
