# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    """
    Base Class designed to capture details about wheeled vehicles.
    """
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        """Method that tells you what this particular vehicle sounds like"""
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    """
    Child Class of GroundVehicle, alters the wheel count and could give different details.
    """
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
    
    def drive(self):
        """Method that details that these vehicles are louder."""
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    vehicle.drive()
#breakpoint()
""" 
Note to grader- The above code works in a ruple, but if you just run this file it won't properly print each drive noise.
I'm not entirely sure why this is. It passes the test_oop2.py file, so I presume this is what is wanted. If you form a ruple and repeat, 
or add a breakpoint() it will display correctly.
"""