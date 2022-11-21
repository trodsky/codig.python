class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

    def exibir(self):
        print(f"O filme {self.nome} tem {self.duracao/60}horas")

class Serie:
    def __init__(self, nome, ano, episodios):
        self.nome = nome 
        self.ano = ano
        self.episodios = episodios

class Teatro:
    def __init__(self, titulo, personagem, figurino, duração):
        self.titulo = titulo
        self.personagem = personagem
        self.figurino = figurino 
        self.duração = duração


f1 = Filme("Gigantes de aço", 2014, 120)
f1.exibir()