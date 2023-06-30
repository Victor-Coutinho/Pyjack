from tupy import *
from random import shuffle
from baralho import *


class Fundo(Image):
	def __init__(self) -> None:
		self.file = 'Fundo.jpg'
		self.x = 550
		self.y = 400



class jogador():
	def __init__(self,carta1,carta2) -> None:
		self.carta1 = carta1
		self.carta2 = carta2
		self.total = carta1.valor + carta2.valor
		self.carta1.x = 425
		self.carta1.y = 400
		self.carta2.x = 550
		self.carta2.y = 400

	def pegar_outra_carta(self) -> None:
		return
		
class Mesa:
	def __init__(self,carta1,carta2) -> None:
		self.carta1 = carta1
		self.carta2 = carta2
		
		
        

fundo = Fundo()
baralho = Baralho()
baralho.embaralha()
carta1 = baralho.pega_carta_do_topo()
carta2 = baralho.pega_carta_do_topo()
jogador1 = jogador(carta1,carta2)


run(globals())
