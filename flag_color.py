#!/usr/bin/python3

from PyQt4.QtGui import QColor
from random import randrange

class FlagColor(QColor):

    def __init__(self):
        super(FlagColor, self).__init__()
        self.setRandomColors()
        
    def setRandomColors(self):
        self.setRed(randrange(0,256))
        self.setGreen(randrange(0,256))
        self.setBlue(randrange(0,256))
