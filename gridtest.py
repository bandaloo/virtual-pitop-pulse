from ptpulse import ledmatrix
from random import randint

grid = []

s_width, s_height = ledmatrix.get_shape()

R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

W = (255, 255, 255)
X = (0, 0, 0)

L = (255, 84, 101)

lightgrid = [[X, X, X, X, X, X, X],
             [X, B, X, X, X, B, X],
             [X, X, X, L, X, X, X],
             [X, R, X, X, X, R, X],
             [X, X, R, R, R, X, X],
             [X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X]]

def paintgrid():
    for i in range(0, s_height):
        for j in range(0, s_width):
            ledmatrix.set_pixel(i, j, lightgrid[j][i][0], lightgrid[j][i][1], lightgrid[j][i][2])

while True:
    paintgrid()
    ledmatrix.show()
