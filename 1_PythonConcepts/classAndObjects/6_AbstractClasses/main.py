# We must import ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod

# 1. THE ABSTRACT CLASS (The Blueprint)
# Inheriting from ABC tells Python: "This is a template, not a real object."
class Vehicle(ABC):

    # @abstractmethod is a "decorator". 
    # It tells Python: "Any class that inherits from Vehicle MUST have this method."
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# ---------------------------------------------------------
# RULE 1: YOU CANNOT INSTANTIATE AN ABSTRACT CLASS
# ---------------------------------------------------------
# vehicle = Vehicle() 
# ERROR: Python raises TypeError: Can't instantiate abstract class Vehicle 
# with abstract methods go, stop.

# 2. THE CONCRETE CLASS (The Implementation)
class Car(Vehicle):
    # Because we defined go() and stop() here, the "Contract" is fulfilled.
    # This class is now "Concrete" and can be created.
    def go(self):
        print("you drive the car")

    def stop(self):
        print("You stop the car")

# 3. TESTING
car = Car()
car.go()
car.stop()

# ---------------------------------------------------------
# RULE 2: CHILDREN MUST IMPLEMENT ALL ABSTRACT METHODS
# ---------------------------------------------------------
# class Boat(Vehicle):
#     def go(self):
#         print("You sail the boat")
#
# boat = Boat() 
# ERROR: This fails because we forgot to write the stop() method.
# Python protects you from creating incomplete classes.
