import colorsys
import math
import time
import sys
from ptpulse import ledmatrix
from random import randint
from gpiozero import Button

s_width, s_height = ledmatrix.get_shape()

# arrays that will store data for the lasers and trails
lgrid = []
tgrid = []

position = 0 # position of player
gamespeed = 6 # how many frames until game steps forward
level = 1 # current difficulty level that increases as game progresses
frequency = 9 # chance of a laser spawning
step = 1 # current game step that increments each frame

button = Button(17) # creating button on the breadboard on pin 17

# makes given empty list a multidimensional array of the led matrix size
def makegrid(grid):
    for i in range(0, s_width):
        grid.append([])
        for j in range(0, s_height):
            grid[i].append(0)


# if num is less than low or greater than high, it will make number within range
def clamp(num, low, high):
    return max(low, min(num, high))

# fill in grids used for lasers and trails
makegrid(lgrid)
makegrid(tgrid)

while True:
    # if the player hits occupies same space as laser, player dies
    if lgrid[position][0] != 0:
        print("score: " + str(step))
        sys.exit()
    # levels up the game, increasing game speed and spawn rate of lasers
    if step % 600 == 0 or step % 1200 == 0 or step % 1800 == 0:
        print(step)
        level += 1
        gamespeed -= 1
        frequency -= 1
    # if game is at the right iterval, step the game forward
    if step % gamespeed == 0:
        # choose direction for player based on whether button is pressed
        if button.is_pressed:
            direction = 1
        else:
            direction = -1
        for i in range(0, s_width):
            for j in range(0, s_height):
                # choose color of trail based on game level
                if level == 1:
                    ledmatrix.set_pixel(i, j, tgrid[i][j], 0, 0)
                elif level == 2:
                    ledmatrix.set_pixel(i, j, 0, tgrid[i][j], 0)
                else:
                    ledmatrix.set_pixel(i, j, 0, 0, tgrid[i][j])
                # make trail fade away
                tgrid[i][j] -= 10
                # make sure color value isn't negative
                if tgrid[i][j] < 0:
                    tgrid[i][j] = 0
                # generate trail behind laser
                if lgrid[i][j] == 1:
                    lgrid[i][j] = 0
                    tgrid[i][j] = 255
                    ledmatrix.set_pixel(i, j, 255, 255, 255)
                    if j > 0:
                        lgrid[i][j - 1] = 1
        # pick random integer for chance of spawning laser
        makelaser = randint(0, frequency)
        if makelaser == frequency:
            # pick random position for the laser
            randpos = randint(0, s_width - 1)
            lgrid[randpos][s_height - 1] = 1
        # move player based on direction
        position += direction
        # make sure player stays on screen
        position = clamp(position, 0, s_width - 1)
        ledmatrix.set_pixel(position, 0, 255, 255, 0)
    ledmatrix.show()
    step += 1
