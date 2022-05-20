class Conta:

    def __init__(self, numero, titular, saldo, limite):   # função construtora do objeto, inicialização
        print("Construindo objeto...{}".format(self))  # self é a referência que sabe onde encontrar o nosso objeto.
        self.__numero = numero  # deixar o atributo privado __,usar esse atributo dentro da classe com os métodos
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):  #metodo
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))  # pegar os valores do objeto

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <=(valor_disponivel_a_sacar)

    def saca(self, valor):  # criei o método para facilitar a legibilidade
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)  # a partir do self eu posso chamar outro método
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular   # get sempre tem um retorno, só criar quando necessário

    @property   # propriedade de melhoria na sintaxe (por baixo dos panos executa p get)
    def limite(self):
        return self.__limite

    @limite.setter   # propriedade de melhoria na sintaxe (por baixo dos panos executa p set)
    def limite(self, limite):   # set não tem retorno, só criar quando necessário
        self.__limite = limite

    # criação do método para acessar o cód do banco
    @staticmethod       # método estático, não precisa do objeto.
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return  {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}



"""
Encapsulamento de acesso aos atributos, devem acontecer pelos métodos.
conta = Conta(123,"Daniela",55.5, 1000.0)
Construindo objeto...<conta.Conta object at 0x000002347DE52B90>
conta._Conta__limite  # aqui o python está te avisando que esse atributo deve ser acessado pela classe.
1000.0
conta._Conta__saldo
55.5

# Método estático
from conta import Conta
Conta.codigo_banco() # (com os parenteses)
'001'

# CUIDADO ! O uso somente de métodos estáticos fogem do mundo OO e mais próximo do mundo procedural.

"""