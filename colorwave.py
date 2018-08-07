from ptpulse import ledmatrix
import colorsys
import math

s_width, s_height = ledmatrix.get_shape()

def numtohue(num):
    return (math.cos(num) + 1) / 2

counter = 0
while True:
    counter += 0.02
    rotationx = math.cos(counter / 8)
    rotationy = math.sin(counter / 8)
    for i in range(0, s_width):
        for j in range(0, s_height):
            color = colorsys.hsv_to_rgb(numtohue(counter + i * rotationx + j * rotationy) * 0.7, 1, 1)
            color = (color[0] * 255, color[1] * 255, color[2] * 255)
            ledmatrix.set_pixel(i, j, color[0], color[1], color[2])
    ledmatrix.show()
