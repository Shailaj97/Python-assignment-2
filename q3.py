class Car:                   #parent class
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):
    def audi_desc(self):
        return "This is the description of class Audi."

class Mustang(Car):
    print("Mustang is a great car")