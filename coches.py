'''
Clases para manejo de coches de combustión y eléctricos.
Ejemplo para uso de clase y herencia.
'''

class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level en litros.
        self.fuel_capacity = 100
        self.fuel_level = 0
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")


if __name__ == '__main__':
    car1 = Car('audi', 'a4', 2019)
