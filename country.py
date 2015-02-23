#!/usr/bin/python3

from flag_color import FlagColor

class Country:
    ''' Country class to hold various country names '''
    
    def __init__(self, name):
        self.setName(name)
        self.setRandomColor()

    def setName(self, name):
        ''' Sets the name of the country '''
        self.name = name

    def getName(self):
        ''' Returns the name of the country '''
        return self.name

    def setRandomColor(self):
        ''' Sets a random color for the country '''
        self.flagColor = FlagColor()

    def getColor(self):
        ''' Returns the color of the country '''
        return self.flagColor

    def __str__(self):
        return 'Hello from ' + self.name

def getCountries():
    countries = open("countries_list.txt","r")
    countryList = []
    for country in countries:
        countryList.append(Country(country.strip()))
    return countryList

def main():
    pass

if __name__ == "__main__":
    main()
        

    
