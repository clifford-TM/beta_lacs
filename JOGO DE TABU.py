import pygame
from pygame.locals import *
from typing import list
from typing import Union

pygame.init()

# CORES 
Branco = (255, 255, 255)
Preto = (0, 0, 0)
Vermelho = (255, 0, 0)
Verde = (0, 255, 0)
Azul = (0, 0, 255)

# PROPORÇÕES
largura = 900
altura = 640
tela = pygame.display.set_mode((largura, altura))  # configura a janela do jogo

# ELEMENTOS DO JOGO
colunas = 30
quadrados_por_coluna = 12
largura_quadrado = 20
espaco_entre_quadrados = 5
fonte = pygame.font.SysFont(None, 20)



    


nomes_para_linhas = {
    "aries": 0,
    "touro": 1,
    "gemeos": 2,
    "cancer": 3,
    "leao": 4,
    "virgem": 5,
    "libra": 6,
    "escorpiao": 7,
    "sagitario": 8,
    "capricornio": 9,
    "aquario": 10,
    "peixes": 11
    }


class Casa:
    Tipos = ["claros", "extalcao", "fortuna", "fumosos", "femininos", "masculinos", "tenebrosos", "queda", "mutilacao", "masmorra"]

    def __init__(self, posicao, cor, tipo):
        self.posicao = posicao
        self.cor = cor
        self.tipo = tipo

    def coordenada_para_posicao(coordenada):
        nome, numero = coordenada[0], int(coordenada[1:])
        linha = nomes_para_linhas[nome]
        coluna = numero - 1
        return linha, coluna

    def desenhar(self, tela):
        for casa in self.casas:
            x, y = casa.posicao
            pygame.draw.rect(tela, casa.cor, (x, y, largura_quadrado, largura_quadrado))


     # definição das posições das casas
    posicoes_casas = [(20 + coluna * (largura_quadrado + espaco_entre_quadrados), 
                       50 + quadrado * (largura_quadrado + espaco_entre_quadrados)) 
                       for coluna in range(colunas) 
                       for quadrado in range(quadrados_por_coluna)]
    
    for posicao, tipo in zip(posicoes_casas, Tipos):
            casas.append(Casas(posicao, Preto, tipo))


class Tabuleiro:
    def __init__(self):
        self.casas = []
        self.posicoes_casas = [(20 + coluna * (largura_quadrado + espaco_entre_quadrados), 
                       50 + quadrado * (largura_quadrado + espaco_entre_quadrados)) 
                       for coluna in range(colunas) 
                       for quadrado in range(quadrados_por_coluna)]
        
        self.casas = {

            "claros": [(4,0), (5,0), (6,0), (7,0), (8,0), (17,0), (18,0), (19,0), (20,0), (25,0), (26,0), (27,0), (28,0), (29,0), (4,1), (5,1), (6,1), (7,1), (13,1), (14,1), (15,1), (21,1), (22,1), (23,1), (24,1), (25,1), (26,1), (27,1), (28,1),
                       (1,2), (2,2), (3,2), (4,2), (8,2), (9,2), (10,2), (11,2), (12,2), (17,2), (18,2), (19,2), (20,2), (21,2), (22,2), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (9,3), (10,3), (11,3), (12,3), (21,3), (22,3),  (23,3), (24,3), (25,3),
                       (26,3), (27,3), (28,3) ,(26,4), (27,4), (28,4), (29,4), (30,4), (6,5), (7,5), (8,5), (11,5), (12,5), (13,5), (14,5), (15,5), (16,5), (1,6), (2,6), (3,6), (4,6), (5,6), (11,6), (12,6), (13,6), (14,6), (15,6), (16,6), (17,6), (18,6), (22,6), (23,6),
                       (24,6), (25,6), (26,6), (27,6),(4,7), (5,7), (6,7), (7,7), (8,7), (15,7), (16,7), (17,7), (18,7), (19,7), (20,7), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8), (8,8), (9,8) (13,8), (14,8) (15,8), (16,8), (17,8), (18,8), (19,8), (24,8), (25,8), (26,8),
                       (27,8), (28,8), (29,8), (30,8), (8,9), (9,9), (10,9), (16,9), (17,9), (18,9), (19,9), (5,10), (6,10), (7,10), (8,10), (9,10), (14,10), (15,10),(16,10), (17,10), (18,10), (19,10), (20,10), (21,10), (26,10), (27,10), (28,10), (29,10), (30,10), (7,11),
                       (8,11), (9,11), (10,11), (11,11), (12,11), (19,11), (20,11), (21,11), (22,11), (26,11), (27,11), (28,11)]


            "extaltacao": [(19,0), (3,1), (21,6), (15,2), (28,9), (27,11), (15,5)]
            

            "fortuna": [(19,0), (3,1), (15,1), (27,1), (11,2), (1,3), (2,3), (3,3), (4,3), (15,3), (2,4), (5,4), (7,4), (19,4),
                        (3,5), (14,5), (20,5), (3,6), (5,6), (21,6), (7,7), (18,7), (20,7), (12,8), (20,8), (12,9), (13,9), (14,9),
                        (20,9), (7,10), (16,10), (17,10), (20,10), (13,11), (20,11)]


            "fumosos": [(19,2), (20,2), (11,4), (12,4), (13,4), (14,4), (15,4), (16,4), (17,4), (18,4), (19,4), (20,4), (17,5), (18,5), (19,5),
                          (20,5), (21,5), (22,5), (21,7), (22,7), (20,8), (21,8), (22,8), (23,8), (11,9), (12,9), (13,9), (14,9), (15,9), (1,10),
                          (2,10), (3,10), (4,10)]


            "femininos": [(9,0), (16,0), (17,0), (18,0), (19,0), (20,0), (21,0), (22,0), (1,1), (2,1), (3,1), (4,1), (5,1), (12,1), (13,1), (14,1),(15,1), (16,1),
                       (17,1), (22,1), (23,1), (24,1), (1,2), (2,2), (3,2), (4,2), (5,2), (17,2), (18,2), (19,2),(20,2), (21,2), (22,2), (27,2), (28,2), (29,2),
                       (30,2), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (11,3), (12,3),(24,3), (25,3), (26,3), (27,3), (6,4), (7,4), (8,4), (16,4), (17,4), (18,4),
                       (19,4), (20,4),(21,4), (22,4), (23,4), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), (8,5),(13,5), (14,5), (15,5), (16,5), (17,5), (18,5),
                       (19,5), (20,5), (6,6), (7,6), (8,6), (9,6), (10,6), (11,6), (12,6), (13,6), (14,6), (15,6), (21,6), (22,6), (23,6), (24,6), (25,6), (26,6),
                       (27,6), (5,7), (6,7), (7,7), (8,7), (9,7), (10,7), (11,7), (12,7), (13,7), (14,7), (18,7), (19,7), (20,7), (21,7), (22,7), (23,7), (24,7),
                       (25,7), (3,8), (4,8), (5,8), (13,8), (14,8), (15,8), (16,8), (17,8), (18,8), (19,8), (20,8), (21,8), (22,8), (23,8), (24,8), (12,9), (13,9),
                       (14,9), (15,9), (16,9), (17,9), (18,9), (19,9), (6,10), (7,10), (8,10), (9,10), (10,10), (11,10), (12,10), (13,10), (14,10), (15,10), (22,10),
                       (23,10), (24,10), (25,10), (28,10), (29,10), (30,10), (11,11), (12,11), (13,11), (14,11), (15,11), (16,11), (17,11), (18,11), (19,11), (20,11),
                       (24,11), (25,11), (26,11), (27,11), (28,11)]




            "masculinos": [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (10,0), (11,0), (12,0), (13,0), (14,0), (15,0), (23,0),
                        (24,0), (25,0), (26,0), (27,0), (28,0), (29,0), (30,0), (6,1), (7,1), (8,1), (9,1), (10,1), (11,1), (18,1), (19,1),
                        (20,1), (21,1), (25,1), (26,1), (27,1), (28,1), (29,1), (30,1), (1,2), (2,2), (9,2), (10,2), (13,2), (14,2), (15,2),
                        (16,2), (23,2), (24,2), (25,2), (26,2), (1,3), (2,3), (9,3), (10,3), (13,3), (14,3), (15,3), (16,3), (17,3), (18,3),
                        (19,3), (20,3), (21,3), (22,3), (23,3), (28,3), (29,3), (30,3), (1,4), (2,4), (3,4), (4,4), (5,4), (9,4), (10,4), (11,4),
                        (12,4), (13,4), (14,4), (15,4), (24,4), (25,4), (26,4), (27,4), (28,4), (29,4), (30,4), (9,5), (10,5), (11,5), (12,5), (21,5),
                        (22,5), (23,5), (24,5), (25,5), (26,5), (27,5), (28,5), (29,5), (30,5), (1,6), (2,6), (3,6), (4,6), (5,6), (16,6), (17,6),
                        (18,6), (19,6), (20,6), (28,6), (29,6), (30,6), (1,7), (2,7), (3,7), (4,7), (15,7), (16,7), (17,7), (26,7), (27,7), (28,7),
                        (29,7), (30,7), (1,8), (2,8), (6,8), (7,8), (8,8), (9,8), (10,8), (11,8), (12,8), (25,8), (26,8), (27,8), (28,8), (29,8), (30,8),
                        (1,9), (2,9), (3,9), (4,9), (5,9), (6,9), (7,9), (8,9), (9,9), (10,9), (11,9), (20,9), (21,9), (22,9), (23,9), (24,9), (25,9),
                        (26,9), (27,9), (28,9), (29,9), (30,9), (1,10), (2,10), (3,10), (4,10), (5,10), (16,10), (17,10), (18,10), (19,10), (20,10), (21,10),
                        (26,10), (27,10), (1,11), (2,11), (3,11), (4,11), (5,11), (6,11), (7,11), (8,11), (9,11), (10,11), (21,11), (22,11), (23,11), (29,11),
                        (30,11)]


            "tenbrosos": [(1,0), (2,0), (3,0), (9,0), (10,0),(11,0), (12,0), (13,0), (14,0), (15,0), (16,0), (1,1), (2,1), (3,1), (29,1), (30,1), (5,2), (6,2), (7,2), (23,2), (24,2),
                       (25,2), (26,2), (27,2), (13,3), (14,3), (1,4), (2,4), (3,4), (4,4), (5,4),(6,4), (7,4), (8,4), (9,4), (10,4), (1,5), (2,5), (3,5), (5,5), (5,5),(28,5), (29,5),
                       (30,5), (6,6), (7,6), (8,6), (9,6), (10,6), (19,6), (20,6), (21,6), (1,7), (2,7), (3,7), (28,7), (29,7), (30,7), (10,8), (11,8), (12,8), (1,9), (2,9), (3,9),
                       (4,9), (5,9), (6,9), (7,9), (20,9), (21,9), (22,9), (26,9), (27,9), (28,9), (29,9), (30,9), (10,10), (11,10), (12,10), (13,10), (1,11), (2,11), (3,11), (4,11),
                       (5,11), (6,11), (13,11), (14,11), (15,11), (16,11), (17,11), (18,11), (29,11), (30,11)]


            "queda": [(19, 6), (3, 7), (21, 0), (15, 9), (28, 2), (27, 5), (15, 11)]


            "mutilacao": [(6,1), (7,1), (8,1), (9,1), (10,1), (9,3), (10,3), (11,3), (12,3), (14,3), (15,3), (18,4), (27,4), (28,4), (19,7), (29,7), (1,8), (7,8), (8,8),
                      (18,8), (19,8), (26,9), (27,9), (28,9), (29,9), (18,10), (19,10)]


            "masmorra": [(6,0), (11,0), (16,0), (23,0), (29,0), (5,1), (12,1), (14,1), (24,1), (25,1), (2,2), (12,2), (17,2), (26,2), (30,2), (12,3), (17,3), (23,3), (26,3),
                     (30,3), (6,4), (13,4), (15,4), (22,4), (23,4), (28,4), (8,5), (13,5), (16,5), (21,5), (25,5), (1,6), (7,6), (20,6), (30,6), (9,7), (10,7), (22,7), (23,7),
                     (27,7), (7,8), (12,8), (15,8), (24,8), (27,8), (30,8), (2,9), (7,9), (17,9), (22,9), (24,9), (28,9),(1,10), (12,10), (17,10), (24,10), (29,10), (4,11), (9,11),
                     (24,11), (27,11), (28,11)]

            }



    def criar_casa(self):
        for posicao in self.posicoes_claros:
    self.casas.append(Casas(posicao, Preto, claros))

        for posicao in self.posicoes_exaltacao:
    self.casas.append(Casas(posicao, Preto, exaltacao))

        for posicao in self.posicoes_fortuna:
    self.casas.append(Casas(posicao, Preto, fortuna))

        for posicao in self.posicoes_fumosos:
    self.casas.append(Casas(posicao, Preto, fumosos))

        for posicao in self.posicoes_femininos:
    self.casas.append(Casas(posicao, Preto, femininos))

        for posicao in self.posicoes_masculinos:
    self.casas.append(Casas(posicao, Preto, masculinos))

        for posicao in self.posicoes_tenebrosos:
    self.casas.append(Casas(posicao, Preto, tenebrosos))

        for posicao in self.posicoes_queda:
    self.casas.append(Casas(posicao, Preto, queda))

        for posicao in self.posicoes_mutilacao:
    self.casas.append(Casas(posicao, Preto, mutilacao))

        for posicao in self.posicoes_masmorra:
    self.casas.append(Casas(posicao, Preto, masmorra))
        


sair = True

while sair:
    tela.fill(Branco)

    for posicao in posicoes_casas:
        pygame.draw.rect(tela, Preto, (*posicao, largura_quadrado, largura_quadrado), 1)

    for nome, linha in nomes_para_linhas.items():
        texto = fonte.render(nome, True, Preto)
        posicao = (10, 50 + linha * (largura_quadrado + espaco_entre_quadrados))
        tela.blit(texto, posicao)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
            pygame.quit()
