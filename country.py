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


def main():
    # Test the Country-class with some names
    print(Country('The Netherlands'))
    print(Country('Belgium'))
    print(Country('Germany'))


if __name__ == "__main__":
    main()
        

    
