class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(self.dia, self.mes, self.ano, sep='/')
        #  print("{}/{}/{}".format(self.dia,self.mes,self.ano))


"""

Passo a passo
from data import Data  # data é o nome do arquivo e Datas o nome da classe
d = Data(10,5,2022) # d è uma vaiável e o que stá em () são os parâmetros
d.formatada()  # chamar a função

"""