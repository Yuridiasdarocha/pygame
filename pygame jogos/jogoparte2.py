import pygame
from pygame.locals import *
from sys import exit

# Começa o Pygame
pygame.init ()

# Tamanho da janela
largura = 640
altura = 480

# Onde o objeto começa
x = largura / 2
y = altura / 2

# Nome que aparece na janela
pygame.display.set_caption("Primeiro jogo com Pygame")

# Cria o relógio para o jogo rodar na mesma velocidade
relogio = pygame.time.Clock()

# Abre a janela do jogo
tela = pygame.display.set_mode((largura, altura))

while True:
    # Faz o jogo rodar com 60 fps
    relogio.tick(60)

    # Pinta a tela de preto
    tela.fill((0, 0, 0))

    # Olha o que o jogador fez no teclado ou se fechou a janela
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                x = x - 5
            elif event.key == K_d or event.key == K_RIGHT:
                x = x + 5
            elif event.key == K_w or event.key == K_UP:
                y = y - 5
            elif event.key == K_s or event.key == K_DOWN:
                y = y + 5
        if event.type == QUIT:
            exit()

    # Muda a posição do objeto enquanto a tecla está sendo pressionada
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + 5

    # Desenha um retângulo vermelho na tela
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()

    # Se o jogador fechar a janela, encerra o jogo
    if event.type == QUIT:
        pygame.quit()
        exit()
