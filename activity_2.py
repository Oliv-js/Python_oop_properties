class Vehicle:
    """Base class for all vehicles"""
    def move(self):
        pass  # Intentionally empty to be overridden by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

class Rocket(Vehicle):
    def move(self):
        print("Blasting off! 🚀")

# Demonstration of polymorphism
if __name__ == "__main__":
    vehicles = [
        Car(),
        Plane(),
        Boat(),
        Bicycle(),
        Rocket()
    ]

    print("Let's see how different vehicles move:")
    for vehicle in vehicles:
        vehicle.move()  # Same method name, different implementations
