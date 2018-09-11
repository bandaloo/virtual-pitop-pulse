import colorsys
import math
from ptpulse import ledmatrix

s_width, s_height = ledmatrix.get_shape()

grid = []

def makegrid(grid):
    for i in range(0, s_width):
        grid.append([])
        for j in range(0, s_height):
            grid[i].append(0)


def mandelbrot(z, maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return maxiter


makegrid(grid)
for i in range(0, s_width):
    re = i / s_width * 4 - 2
    for j in range(0, s_height):
        im = j / s_height * 4 - 2
        z = complex(re, im)
        iter = mandelbrot(z, 100)
        grid[i][j] = iter


while True:
    for i in range(0, s_width):
        for j in range(0, s_height):
            ledmatrix.set_pixel(i, j, grid[i][j], grid[i][j], grid[i][j])
    ledmatrix.show();
