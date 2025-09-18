# Import a useful container from the typing module
from typing import Optional

class Computer:

    def __init__(self,
                 description: str,
                 processorType: str,
                 hardDriveCapacity: int,
                 memory: int,
                 os: str,
                 yearMade: int,
                 price: int):
        
        self.desc = description
        self.processor = processorType
        self.hardDrive = hardDriveCapacity
        self.memory = memory
        self.os = os
        self.yearMade = yearMade
        self.price = price

    """
    Returns a nice-looking, readable string representation of a computer's information
    """
    def __str__(self):
        return f"{self.desc}: {self.processor} processor, {self.hardDrive} GB hard drive, {self.memory} GB RAM, runs {self.os}, {self.yearMade} model, ${self.price}"

    def __repr__(self):
        return f"(description: '{self.desc}', processor: '{self.processor}', hardDrive: {self.hardDrive}, memory: {self.memory}, os: '{self.os}', yearMade: {self.yearMade}, price: {self.price})"

    """
    Takes in a new price, updates the computer's price to match
    """
    def updatePrice(self, newPrice: int):
        self.price = newPrice
    
    """
    Updates a computer's price depending on its yearMade,
    updates its os if a new one is given
    """
    def refurbish(self, newOS: Optional[str] = None):
        if self.yearMade < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.yearMade < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.yearMade < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        # Then update the OS if a new one is given!
        if newOS is not None:
            self.os = newOS