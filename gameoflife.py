import pygame, sys
from pygame.locals import *

class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.active = False


cells = {}

for x in range(0, 800, 10):
    for y in range(0, 640, 10):
        cells[x,y] = cell(x, y)

cells[100, 100].active = True
cells[110, 110].active = True
cells[90, 120].active = True
cells[100, 120].active = True
cells[110, 120].active = True
pygame.init()

srf = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Conway's Game of Life")

whiteColor = pygame.Color(255, 255, 255)
grayColor = pygame.Color(220, 220, 220)
blackColor = pygame.Color(0, 0, 0)

clock = pygame.time.Clock()

def getCount(x, y):
    if (x,y) in cells:
        if cells[x, y].active:
            return 1
    
    return 0

def update():
    newcells = {}
    for key, value in cells.items():
        newcells[key] = cell(key[0], key[1])
        count = 0
        count += getCount(key[0] - 10, key[1])
        count += getCount(key[0] - 10, key[1] - 10)
        count += getCount(key[0], key[1] - 10)
        count += getCount(key[0] + 10, key[1] - 10)
        count += getCount(key[0] + 10, key[1])
        count += getCount(key[0] + 10, key[1] + 10)
        count += getCount(key[0], key[1] + 10)
        count += getCount(key[0] - 10, key[1] + 10)


        if count == 0 or count == 1:
            newcells[key].active = False
        if count >= 4:
            newcells[key].active = False

        if count == 3:
            newcells[key].active = True
        if cells[key].active and count == 2:
            newcells[key].active = True

        if key not in newcells:
            newcells[key].active = False

    global cells
    cells = newcells
        

while True:
    clock.tick(2)
    srf.fill(whiteColor)
    for x in range(0, 800, 10):
        pygame.draw.line(srf, grayColor, (x, 0), (x, 600), 1)
    for y in range(0, 640, 10):
        pygame.draw.line(srf, grayColor, (0, y), (800, y), 1)


    for key, value in cells.items():
        if value.active:
            pygame.draw.rect(srf, blackColor, (key[0], key[1], 10, 10), 0)

    pygame.display.update()

    update()
    
