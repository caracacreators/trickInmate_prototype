import pygame, sys, spritesheetClass

#Events
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

#SURFACE
SCREEN_W,SCREEN_H = 800, 600
SCREEN_CENTERW, SCREEN_CENTERH = SCREEN_W/2, SCREEN_H/2
AREA = SCREEN_W*SCREEN_H


#iNICIALIZAÇÃO DA PYGAME
pygame.init()
CLOCK = pygame.time.Clock()
DISP_Screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Caraca Creators TM")
FPS = 30
ON_SCENE = True

#Cores base
BLACK = (0,0,0,255)
WHITE = (255,255,255,255)

#Logo Spritesheet
sLogo = spritesheetClass.Spritesheet("assets\logoAnimation\LogoSpritesheet.png", 1, 24)

CENTER_HANDLER=4

index = 0


#LOOP PRINCIPAL
while ON_SCENE:
    events()

    if index < 23:
        sLogo.draw(DISP_Screen, index % sLogo.totalCellCount, SCREEN_CENTERW, SCREEN_CENTERH, CENTER_HANDLER)
        index += 1
    elif index == 23:
        sLogo.draw(DISP_Screen, 11, SCREEN_CENTERW, SCREEN_CENTERH, CENTER_HANDLER)

    pygame.display.update()
    CLOCK.tick(12)
    DISP_Screen.fill(WHITE)


