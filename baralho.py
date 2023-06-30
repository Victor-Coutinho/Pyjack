from tupy import *
from random import shuffle

class Carta(Image):
    
	A = 11
	KQJ = 10
	
	def __init__(self,naipe: str,valor) -> None:
		self._naipe = naipe
		try:
			self._valor = int(valor)
		except:
			if valor != "A":
				self._valor = Carta.KQJ
			else:
				self._valor = Carta.A
		self.file = str(self._valor) +" of " + self._naipe + ".png"
		self.x = 600
		self.y = 600

	@property
	def valor(self):
		return self._valor
	
	@valor.setter
	def velocidade(self,valor):
		self._valor = valor


class Baralho():
	def __init__(self):
		self.cartas = []
		for naipe in ['Spades', 'Clubs', 'Hearts', 'Diamonds']:
			for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']:
				self.cartas.append(Carta(naipe, valor))
				
	def embaralha(self):
		shuffle(self.cartas)
		
	def pega_carta_do_topo(self) -> Carta:
		#carta_removida = self.cartas[-1].file
		return self.cartas.pop()
