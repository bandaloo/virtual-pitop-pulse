import colorsys
import math
import time
from ptpulse import ledmatrix
from random import randint

s_width, s_height = ledmatrix.get_shape()

counter = 0

lgrid = []
tgrid = []
bgrid = []

def numtohue(num):
    return (math.cos(num) + 1) / 2


def makegrid(grid):
    for i in range(0, s_width):
        grid.append([])
        for j in range(0, s_height):
            grid[i].append(0)


makegrid(lgrid)
makegrid(tgrid)
makegrid(bgrid)

while True:
    counter += 0.02
    rotationx = math.cos(counter / 8)
    rotationy = math.sin(counter / 8)
    for i in range(0, s_width):
        for j in range(0, s_height):
            color = colorsys.hsv_to_rgb(numtohue(counter + i * rotationx + j * rotationy) * 0.7, 1, 1)
            color = (0, color[1] * 255, color[2] * 255)
            bgrid[i][j] = (color[0], color[1], color[2])
    for i in range(0, s_width):
        for j in range(0, s_height):
            ledmatrix.set_pixel(i, j, tgrid[i][j], bgrid[i][j][1], bgrid[i][j][2])
            tgrid[i][j] -= 10
            if tgrid[i][j] < 0:
                tgrid[i][j] = 0
            if lgrid[i][j] == 1:
                lgrid[i][j] = 0
                tgrid[i][j] = 255
                ledmatrix.set_pixel(i, j, 255, 255, 255)
                if j > 0:
                    lgrid[i][j - 1] = 1

    makelaser = randint(0, 9)
    if makelaser == 9:
        randpos = randint(0, s_width - 1)
        lgrid[randpos][s_height - 1] = 1
    ledmatrix.show()
