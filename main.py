from tupy import *
from random import shuffle


class Fundo(Image):
	def __init__(self) -> None:
		self.file = 'Fundo.jpg'
		self.x = 550
		self.y = 400


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
		self.file = valor +"_de_" + self._naipe
		self.x = 600
		self.y = 600

	@property
	def valor(self):
		return self._valor
	
	@valor.setter
	def velocidade(self,valor):
		self._valor = valor


class Baralho(Image):
	def __init__(self):
		self.cartas = []
		self.x = 800
		self.y = 300
		for naipe in ['espadas', 'paus', 'copas', 'ouros']:
			for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']:
				self.cartas.append(Carta(naipe, valor))
				
	def embaralha(self):
		shuffle(self.cartas)
		
	def pega_carta_do_topo(self) -> Carta:
		#carta_removida = self.cartas[-1].file
		return self.cartas.pop()



class jogador():
	def __init__(self,carta1,carta2) -> None:
		self.carta1 = carta1
		self.carta2 = carta2
		self.total = carta1.valor + carta2.valor
		self.carta1.x = 300
		self.carta1.y = 400
		self.carta2.x = 400
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