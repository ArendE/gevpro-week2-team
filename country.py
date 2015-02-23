#!/usr/bin/python3

class Country:
    ''' Country class to hold various country names '''
    
    def __init__(self, name):
        self.setName(name)

    def setName(self, name):
        ''' Sets the name of the country '''
        self.name = name

    def getName(self):
        ''' Returns the name of the country '''
        return self.name

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
        

    
