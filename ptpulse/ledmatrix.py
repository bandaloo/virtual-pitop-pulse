import os, pygame
import _thread
from pygame.locals import *
from math import ceil

S_WIDTH = 7
S_HEIGHT = 7
W_WIDTH = 448
W_HEIGHT = 448
C_WIDTH = ceil(W_WIDTH / S_WIDTH)
C_HEIGHT = ceil(W_HEIGHT / S_HEIGHT)
grid = []
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
button = None


def drawgrid():
    screen.fill((0, 0, 0))
    for i in range(0, S_WIDTH):
        for j in range(0, S_HEIGHT):
            rj = S_HEIGHT - j - 1
            pygame.draw.rect(screen, grid[i][rj], (i * C_WIDTH, j * C_HEIGHT, C_WIDTH, C_HEIGHT))


def get_shape():
    return (S_WIDTH, S_HEIGHT)


def clear():
    for i in range(0, S_WIDTH):
        for j in range(0, S_HEIGHT):
            grid[i][j] = (0, 0, 0)


def set_pixel(x, y, r, g, b):
    grid[x][y] = (r, g, b)


def show():
    drawgrid()
    pygame.display.update()
    doevents()


def doevents():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and event.key == pygame.K_SPACE:
            if button != None:
                button.is_pressed = True
        else:
            button.is_pressed = False


def main():
    for i in range(0, S_WIDTH):
        grid.append([])
        for j in range(0, S_HEIGHT):
            grid[i].append((0, 0, 0))
    pygame.init()
    screen.fill((255, 0, 0))
    pygame.display.update()
    print("starting game")
    doevents()

main()
