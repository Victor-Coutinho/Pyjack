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
		
		
		
class Dealer():
	def __init__(self,carta1,carta2) -> None:
		self.carta1 = carta1
		self.carta2 = carta2
		self.total = carta1.valor + carta2.valor
		self.carta1.x = 425
		self.carta1.y = 25
		self.carta2.x = 550
		self.carta2.y = 25
		self.carta1.file = 'back.png'
		self.carta2.file = 'back.png'
		
	def pegar_outra_carta(self) -> None:
		return

