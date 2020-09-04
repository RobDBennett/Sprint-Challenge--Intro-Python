# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:  
    #Parent(base) Class
    pass

class FlightVehicle(Vehicle): 
    #Child class, inherits from Vehicle
    pass

class Airplane(FlightVehicle):
    #Child class, inherits from FlightVehicle
    pass

class Starship(FlightVehicle):
    #Child class, inherits from FlightVehicle
    pass

class GroundVehicle(Vehicle):
    #Child class, inherits from Vehicle
    pass

class Car(GroundVehicle):
    #Child class, inherits from GroundVehicle.
    pass

class Motorcycle(GroundVehicle):
    #Child class, inherits from GroundVehicle.
    pass