#!/usr/bin/python3

# Random Country Flag Color v1.0
# Version 23-02-2015
# Made for the course Advanced Programming

import sys
from PyQt4 import QtGui, QtCore
import country

class CountryFlags(QtGui.QWidget):
    ''' GUI to show a country dropdown and show the color of the selected country '''
    
    def __init__(self):
        """ Initializes the PyQt4 gui, instance variables needed for the converter and initializes them """
        super(CountryFlags, self).__init__()
        self.countries = country.getCountries()
        self.initUI()

    def initUI(self):
        # Window
        self.setWindowTitle('Random Country Flag Color v1.0')        
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint) # Disables full-screen (static layout)
        self.setGeometry(8,32,420,155)
        self.show()

        # Font size
        font = QtGui.QFont()
        font.setPointSize(10)

        # Country selection box
        self.cSelect = QtGui.QComboBox(self)
        self.cSelect.setGeometry(10, 10, 400, 30)
        self.defaultCountry = '-- Choose a country to show its color --'
        self.cSelect.addItem(self.defaultCountry)
        for country in self.countries:
            self.cSelect.addItem(country.getName())
        self.cSelect.setFont(font)
        self.cSelect.show()

        # Country Color frame
        self.cColor = QtGui.QFrame(self)
        self.cColor.setGeometry(10, 50, 400, 95)
        self.cColor.show()

        # Setup the signals
        self.cSelect.currentIndexChanged.connect(self.updateUI)

    def updateUI(self):
        if(self.cSelect.currentText() == self.defaultCountry):
            self.cColor.setAutoFillBackground(False);
        else:
            for country in self.countries:
                if(self.cSelect.currentText() == country.getName()):
                    # Idea to use QPallete from http://www.qtforum.org/article/25559/cannot-set-qframe-background-color.html
                    palette = QtGui.QPalette(country.getColor())
                    self.cColor.setPalette(palette);
                    self.cColor.setAutoFillBackground(True);
        
def main():
    app = QtGui.QApplication(sys.argv)
    countryFlags = CountryFlags()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
	main()
