from ptpulse import ledmatrix
from random import randint

def paintbackground(red, green, blue):
    for i in range(0, 7):
        for j in range(0, 7):
            ledmatrix.set_pixel(i, j, red, green, blue)

position = 0
while True:
    ledmatrix.clear()
    paintbackground(0, 0, 255)
    # parameters, are x position, y position, red, green and blue
    position += 1
    if position == 7:
        position = 0
    ledmatrix.set_pixel(2, position, 255, 0, 0)
    ledmatrix.set_pixel(2, 3, randint(0, 255), randint(0, 255), randint(0, 255))
    ledmatrix.set_pixel(5, 5, 42, 226, 79)
    ledmatrix.set_pixel(1, 2, 126, 100, 200)
    ledmatrix.set_pixel(3, 2, 125, 90, 61)
    ledmatrix.show()
