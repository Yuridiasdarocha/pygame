# Importa as bibliotecas necessárias para o jogo
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura = 640
altura = 480

# Define a posição inicial do jogador (retângulo vermelho) no centro da tela
x = largura / 2
y = altura / 2

# Define o título da janela do jogo
pygame.display.set_caption("Primeiro jogo com Pygame")

# Cria um objeto de relógio para controlar o FPS
relogio = pygame.time.Clock()

# Cria a tela do jogo
tela = pygame.display.set_mode((largura, altura))

# Define a posição inicial do alvo (retângulo azul/verde) aleatoriamente
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# Loop principal do jogo
while True:
    # Limita o jogo a 60 FPS
    relogio.tick(60)

    # Preenche a tela com preto
    tela.fill((0, 0, 0))

    # Processa os eventos do jogo
    for event in pygame.event.get():
        # Verifica se uma tecla foi pressionada
        if event.type == KEYDOWN:
            # Movimento para a esquerda (A ou Seta Esquerda)
            if event.key == K_a or event.key == K_LEFT:
                x = x - 5
            # Movimento para a direita (D ou Seta Direita)
            elif event.key == K_d or event.key == K_RIGHT:
                x = x + 5
            # Movimento para cima (W ou Seta Cima)
            elif event.key == K_w or event.key == K_UP:
                y = y - 5
            # Movimento para baixo (S ou Seta Baixo)
            elif event.key == K_s or event.key == K_DOWN:
                y = y + 5
        # Encerra o jogo se a janela for fechada
        if event.type == QUIT:
            exit()

    # Verifica movimento contínuo usando as teclas pressionadas
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + 5

    # Desenha o retângulo vermelho (jogador)
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    # Desenha o retângulo azul/verde (alvo)
    ret_azul = pygame.draw.rect(tela, (0, 255, 0), (x_azul, y_azul, 50, 50))

    # Verifica se o jogador colidiu com o alvo
    if ret_vermelho.colliderect(ret_azul):
        # Gera uma nova posição aleatória para o alvo
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
    
    # Verifica se o jogador saiu dos limites da tela (game over)
    if x < 0 or x + 50 > largura or y < 0 or y + 50 > altura:
        exit()

    # Atualiza a tela do jogo
    pygame.display.update()

