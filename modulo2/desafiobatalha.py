import random

class Personagem:

    def __init__(self, nome, vida, ataque, pocoes=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes
        self.defendendo = False

    def atacar(self, alvo):
        dano = self.ataque

        if random.random() < 0.2:  # 20% de chance
            dano *= 2  # acerto crítico (dano dobrado)
            print(f"{self.nome} acertou um ataque critico!")
        print(f'{self.nome} atacou {alvo.nome} causando {dano} de dano.')
        alvo.rteceber_dano(dano)


    def receber_dano(self, dano):
        if self.defendendo:
            dano /= 2 #reduz o dano pela metade
            self.defendendo = False

            self.vida -= dano
            
