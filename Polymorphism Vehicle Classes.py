class Vehicle:
    def move(self):
        pass  # Base class move method, to be overridden by child classes

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Creating objects of different vehicle classes
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Calling the move method on each object
vehicles = [my_car, my_plane, my_boat]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves differently based on its class
