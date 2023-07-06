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
		self.quantidade_de_cartas = 2
		self.carta1.x = 350
		self.carta1.y = 400
		self.carta2.x = 475
		self.carta2.y = 400

	def pegar_outra_carta(self, cartax) -> None:
		self.total += cartax.valor
		self.quantidade_de_cartas += 1
		cartax.x = 350 + 125 * (self.quantidade_de_cartas - 1)
		cartax.y = 400
		
		
		
class Dealer():
	def __init__(self,carta1,carta2) -> None:
		self.carta1 = carta1
		self.carta2 = carta2
		self.total = carta1.valor + carta2.valor
		self.quantidade_de_cartas = 2
		self.carta1.x = 350
		self.carta1.y = 25
		self.carta2.x = 475
		self.carta2.y = 25
		self.carta2.file = 'back.png'
		
	def pegar_outra_carta(self,carta) -> None:
		self.total += carta.valor
		self.quantidade_de_cartas += 1
		carta.x = 350 + 125 * (self.quantidade_de_cartas - 1)
		carta.y = 25
		return
	
	

