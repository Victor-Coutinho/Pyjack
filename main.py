from Jogador import *


fundo = Fundo()
baralho = Baralho()
baralho.embaralha()
carta1 = baralho.pega_carta_do_topo()
carta2 = baralho.pega_carta_do_topo()
jogador1 = jogador(carta1,carta2)
carta3 = baralho.pega_carta_do_topo()
carta4 = baralho.pega_carta_do_topo()
dealer = Dealer(carta3,carta4)



run(globals())
