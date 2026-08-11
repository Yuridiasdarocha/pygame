# bibliotecas necessárias
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# inicializa o pygame
pygame.init()

# dimensões da janela
largura = 640
altura = 480

# posição inicial do jogador (centro)
x = largura / 2
y = altura / 2

# fontes para texto
fontepontos = pygame.font.Font(None, 25)
fontederrota = pygame.font.Font(None, 50)

# título da janela
pygame.display.set_caption("Primeiro jogo com Pygame")

# relógio para controlar o FPS
relogio = pygame.time.Clock()

# janela do jogo
tela = pygame.display.set_mode((largura, altura))

# posição inicial do alvo (aleatória)
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# pontuação inicial
pontos = int(0)

# cor do texto de pontuação
corbrancopontos = (255,255,255)

# Define tamanho inicial da 'cobra'
tamanhoinicial = 10
# Lista para armazenar as posições do corpo da cobra
listacobra = []

# Loop principal do jogo
while True:
    # Define FPS do jogo em 10 frames por segundo
    relogio.tick(10)
    # Preenche a tela com cor preta (apaga frame anterior)
    tela.fill((0, 0, 0))
    # Cria um retângulo vazio para colisão com a cobra
    ret_vermelho = pygame.Rect(0, 0, 0, 0)
    # Renderiza o texto de pontuação
    textopontos = fontepontos.render (f"Pontuação {pontos}", True,corbrancopontos)
    # Desenha o texto de pontuação na tela
    tela.blit(textopontos, (10, 10))       
    
    # Verifica eventos do pygame
    for event in pygame.event.get():                      
        # Se o evento é QUIT, fecha o jogo
        if event.type == QUIT:
            exit()

    # Flag para verificar se houve movimento
    moveu = False
    # Verifica se tecla 'A' ou ESQUERDA foi pressionada
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        # Move o jogador 20 pixels para a esquerda
        x = x - 20
        # Marca que houve movimento
        moveu = True
    # Verifica se tecla 'D' ou DIREITA foi pressionada
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        # Move o jogador 20 pixels para a direita
        x = x + 20
        # Marca que houve movimento
        moveu = True
    # Verifica se tecla 'W' ou CIMA foi pressionada
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        # Move o jogador 20 pixels para cima
        y = y - 20
        # Marca que houve movimento
        moveu = True
    # Verifica se tecla 'S' ou BAIXO foi pressionada
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        # Move o jogador 20 pixels para baixo
        y = y + 20
        # Marca que houve movimento
        moveu = True

    # Se houve movimento, adiciona à lista da cobra
    if moveu == True:       
        # Cria lista com posição atual
        posicaoatual = [x, y]
        # Adiciona posição atual ao corpo da cobra
        listacobra.append(posicaoatual)
        # Se a cobra ultrapassou o tamanho máximo, remove a primeira posição
        if len(listacobra) > (tamanhoinicial + pontos):
            # Remove o primeiro elemento (cauda da cobra)
            del listacobra [0]
    # Itera por cada coordenada da cobra
    for coordernada in listacobra:
        # Desenha um quadrado vermelho para cada parte da cobra
        ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (coordernada [0], coordernada [1], 30, 30))
    # Desenha o alvo (retângulo verde)
    ret_azul = pygame.draw.rect(tela, (0, 255, 0), (x_azul, y_azul, 50, 50))

    # Verifica colisão entre cobra e alvo
    if ret_vermelho.colliderect(ret_azul):
        # Gera nova posição aleatória para o alvo (X)
        x_azul = randint(40, 600)
        # Gera nova posição aleatória para o alvo (Y)
        y_azul = randint(50, 430)
        # Aumenta a pontuação em 1
        pontos = pontos + 1

    # Verifica se a cobra saiu da tela (colisão com as bordas)
    if x < 0 or x + 10 > largura or y < 0 or y + 10 > altura:
        # Renderiza mensagem de derrota com a pontuação final
        textoderrota = fontederrota.render (f"Você perdeu, sua pontuação: {pontos}", True, corbrancopontos) 
        # Desenha o texto de derrota na tela
        tela.blit(textoderrota, (10, 200))
        # Atualiza a tela para mostrar a mensagem
        pygame.display.update()
        # Registra o tempo atual em milissegundos
        alarmetempo = pygame.time.get_ticks()
        # Aguarda 3 segundos antes de fechar
        while pygame.time.get_ticks() - alarmetempo < 3000:
            # Verifica eventos durante a espera
            for event in pygame.event.get():
                # Se clicou para fechar, sai imediatamente
                if event.type == QUIT:
                    exit()
        # Fecha o jogo após 3 segundos
        exit()
    # Atualiza o display para mostrar as mudanças na tela
    pygame.display.update()