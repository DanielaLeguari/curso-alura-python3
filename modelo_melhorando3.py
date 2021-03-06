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
    def __init__(self, nome, ano, duracao): # __init__ é um inicializador de um objeto
        super().__init__(nome, ano)  # chamando a classe mãe, atributos
        self.duracao = duracao

    def __str__(self):  # objeto programa como texto representação textual para o objeto.
        return f'{self._nome} -{self.ano} - {self._likes} Likes'

#  construtor
class Serie(Programa): #  passei como parametro a classe mãe

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # chamando a classe mãe
        self.temporadas = temporadas

    def __str__(self):  # objeto programa como texto.
        return f'{self._nome} -{self.ano} - {self.temporadas} temporadas {self._likes} Likes'

class Playlist:  #  classe mãe de list
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  #método mágico
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


# objetos: vingadores e atlanta
vingadores = Filme('vingadores - guerra infinita', 2018, 160)   # objeto
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
tmep.dar_like()

# lista
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])
len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:  # polimorfismo.
    print(programa)

