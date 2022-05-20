#  construtor
class Programa:   # classe mais genérica e as demais classes chamariam ela, criação de uma abstração.
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0  # por convensão deixo um underline.

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

#  construtor, classes filhas
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # chamando a classe mãe, atributos
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):  # método disponível somente para a classe filme. (exemplo)
        pass

#  construtor
class Serie(Programa): #  passei como parametro a classe mãe
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # chamando a classe mãe
        self.temporadas = temporadas

# objetos: vingadores e atlanta
vingadores = Filme('vingadores - guerra infinita', 2018, 160)   # objeto
vingadores.dar_like()
print(f'{vingadores.nome} -{vingadores.ano} - {vingadores.duracao} - {vingadores.likes}')
atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} - {atlanta.likes}')

# lista
filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:  # polimorfismo, consigo percorrer uma lista do mesmo super-tipo, consigo fazer um for.
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas  # if ternário.
    print(f'{programa.nome} -{detalhes} D - {programa.likes}')