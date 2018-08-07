from ptpulse import ledmatrix
from random import randint
import tty, sys

grid = []

s_width, s_height = ledmatrix.get_shape()

R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

W = (255, 255, 255)
X = (0, 0, 0)

L = (255, 84, 101)

lightgrid = [[X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, B, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
             [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X]]

gridlen = len(lightgrid[0])

def paintgrid(position):
    for i in range(0, s_height):
        for j in range(0, s_width):
            xp = (position + i) % gridlen
            ledmatrix.set_pixel(i, j, lightgrid[j][xp][0], lightgrid[j][xp][1], lightgrid[j][xp][2])

counter = 0
position = 0
while True:
    tty.setraw(sys.stdin.fileno())
    while 1:
        ch = sys.stdin.read(1)
        if ch == 'a':
            print("Wohoo")
    counter += 1
    if counter % 6 == 0:
        position += 1

    paintgrid(position)
    ledmatrix.show()
