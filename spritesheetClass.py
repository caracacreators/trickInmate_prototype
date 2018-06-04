import pygame

class Spritesheet():
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols*rows

        self.rect = self.sheet.get_rect()
        cellW = self.cellWidth = self.rect.width/cols
        cellH = self.cellHeight = self.rect.height/rows
        centerCellW, centerCellH = self.centerCell = (cellW/2, cellH/2)

        #Lista de retângulos das imagens da spritesheet
        self.cells = list([(index % cols*cellW, index/cols*cellH, cellW, cellH) for index in range(self.totalCellCount)])
        #offset (pontos de posicionamento da imagem handle[0] equivale ao ponto superior esquerdo
        self.handle = list([(0, 0), (-centerCellW, 0), (-cellW, 0),
                           (0,-centerCellH),(-centerCellW,-centerCellH),(-cellW,-centerCellH),
                            (0,-cellH),(-centerCellW, -cellH),(-cellW, -cellH)])

    def draw(self, surface, cellIndex, x, y, handle=0):
        surface.blit(self.sheet, (x+self.handle[handle][0], y+self.handle[handle][0]),self.cells[cellIndex])
