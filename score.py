from tupy import *

class Score(Label):
    def __init__(self,x,y) -> None:
        super().__init__('Total: 0', x, y, font='Arial 20',color='blue')
        self.__score = 0
    def atualiza(self,valor):
        self.__score += valor
        self.text = 'Total: ' + str(self.__score)

