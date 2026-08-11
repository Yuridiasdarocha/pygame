import pygame
from pygame.locals import *
from sys import exit

pygame.init ()

largura = 1080
altura = 580

tela = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  
            exit()
    pygame.draw.rect(tela, (255 , 0, 0), (200, 426, 40, 90))

    pygame.draw.circle(tela, (0, 255, 0), (350, 496), 20)

    pygame.draw.line(tela, (255, 255, 0), (1, 550), (1080, 550), 70)

    pygame.display.update()