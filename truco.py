import pygame
import config as cf
import resources as rc
import random

maoPlayer1 = [0] * 3
cartasPlayer1 = [None, None, None]
virou = 0
baralho = [0, 1, 2, 3,
           4, 5, 6, 7,
           8, 9, 10, 11,
           12, 13, 14, 15,
           16, 17, 18, 19,
           20, 21, 22, 23]
turno = 1
cartasJogadas = [None, None, None]
spritesBaralho = rc.spritesBaralho()
posCartasJogadas = (273, 232)


def inverterPosCartas(cartasInverter=[]):
    temp = [0] * 4
    for i in range(4):
        temp[i] = spritesBaralho[cartasInverter[i]]

    while i <= 0:
        spritesBaralho.remove(spritesBaralho[cartasInverter[i]])
        i -= 1

    for i in range(4):
        spritesBaralho.append(temp[i])


def virarCarta():
    virou = random.randint(0, len(baralho) - 1)
    baralho[virou] = None
    print('Virou', virou)

    if 0 <= virou <= 3:
        inverterPosCartas([4, 5, 6, 7])
    elif 4 <= virou <= 7:
        inverterPosCartas([8, 9, 10, 11])
    elif 8 <= virou <= 11:
        inverterPosCartas([12, 13, 14, 15])
    elif 12 <= virou <= 15:
        inverterPosCartas([16, 17, 18, 19])
    elif 16 <= virou <= 19:
        inverterPosCartas([20, 21, 22, 23])
    elif 20 <= virou <= 23:
        inverterPosCartas([0, 1, 2, 3])
        return virou - 4
    return virou


def entregarCartas():
    cartasPlayerX = [None, None, None]

    for i in range(3):
        while True:
            cartasPlayerX[i] = random.randint(0, len(baralho) - 1)
            if baralho[cartasPlayerX[i]] is not None:
                break
        baralho[cartasPlayerX[i]] = None

    for i in range(24):
        if i % 4 == 0:
            print('')
        print(baralho[i], end=' ')
    print('\n\n', cartasPlayerX)
    return cartasPlayerX


def verificarAnim(mouse):

    if maoPlayer1[0].collidepoint(mouse) and cartasJogadas[0] is None:
        if maoPlayer1[0].top > 400:
            maoPlayer1[0] = maoPlayer1[0].move(0, -10)
    else:
        maoPlayer1[0].top = 460

    if maoPlayer1[1].collidepoint(mouse) and cartasJogadas[1] is None:
        if maoPlayer1[1].top > 400:
            maoPlayer1[1] = maoPlayer1[1].move(0, -10)
    else:
        maoPlayer1[1].top = 460

    if maoPlayer1[2].collidepoint(mouse) and cartasJogadas[2] is None:
        if maoPlayer1[2].top > 400:
            maoPlayer1[2] = maoPlayer1[2].move(0, -10)
    else:
        maoPlayer1[2].top = 460


# def clickObjects(mouse, cartaClicada=[]):
#     if maoPlayer1[0].collidepoint(mouse):
#         cartasJogadas[0] = cartaClicada[0]
#         maoPlayer1[0].left = 373
#         maoPlayer1[0].top = 232
#     elif maoPlayer1[1].collidepoint(mouse):
#         cartasJogadas[1] = cartaClicada[1]
#         maoPlayer1[1].left = 373
#         maoPlayer1[1].top = 232
#     elif maoPlayer1[2].collidepoint(mouse):
#         cartasJogadas[2] = cartaClicada[2]
#         maoPlayer1[2].left = 373
#         maoPlayer1[2].top = 232


def main():
    pygame.init()
    screen = pygame.display.set_mode(cf.TAMANHO_TELA)
    pygame.display.set_caption(cf.TITULO)
    clock = pygame.time.Clock()
    background = pygame.image.load(rc.BACKGROUND)

    maoPlayer1[0] = pygame.Rect((264, 460, 100, 150))
    maoPlayer1[1] = pygame.Rect((357, 460, 100, 150))
    maoPlayer1[2] = pygame.Rect((450, 460, 100, 150))

    manilhaCarta = pygame.Rect((100, 100, 100, 150))
    virou = virarCarta()
    cartasPlayer1 = entregarCartas()

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    maoPlayer1[0] = maoPlayer1[0].move(-10, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!!')
                #clickObjects(mouse)

        verificarAnim(mouse)

        screen.blit(background, (0, 0))
        screen.blit(spritesBaralho[cartasPlayer1[0]], (maoPlayer1[0].left, maoPlayer1[0].top))
        screen.blit(spritesBaralho[cartasPlayer1[1]], (maoPlayer1[1].left, maoPlayer1[1].top))
        screen.blit(spritesBaralho[cartasPlayer1[2]], (maoPlayer1[2].left, maoPlayer1[2].top))
        screen.blit(spritesBaralho[virou], (manilhaCarta.left, manilhaCarta.top))

        clock.tick(cf.FPS)
        pygame.display.update()


main()
