import sys
sys.path.append("..")
from ptpulse import ledmatrix

class Button(object):
    def __init__ (self, boardnum):
        self.is_pressed = False
        ledmatrix.button = self

    def wait_for_press(self):
        while True:
            if self.is_pressed:
                break
