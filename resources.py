import pygame

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

BACKGROUND = 'imagens\mesa.jpg'
BARALHO = 'imagens\sprite_baralho.png'
sprite = pygame.image.load('imagens\sprite_baralho.png')

frames = [0] * 24  # Lista para armazenar as sprites do baralho.


def spritesBaralho():
    x = 0
    for i in range(24):
        frames[i] = sprite.subsurface(pygame.Rect(x, 0, 100, 150))
        x += 100

    return frames



