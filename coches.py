'''
Clases para manejo de coches de combustión y eléctricos.
Ejemplo para uso de clase y herencia.
'''
# Clase base
import os, shelve
class Battery:
    """A battery for an electric car."""
    def __init__(self, size=75):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0
    def get_range(self):
        """Return the battery's range."""
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315
  
class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year, type):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.type = type

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
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'
def leer(ruta):
    '''
    Lee un archivo y devuelve su contenido
    '''
    f = shelve.open(ruta)
    coches = []
    for coche in f:
        coches.append(coches)
    f.close()
    return coches

   
'''



class ElectricCar(Car):
'''
def escribir(ruta, coches):
    '''
    Escribe el texto en el archivo de la ruta.
    Si existe el archivo, aÃ±ade el contenido al final
    del mismo.
    No devuelve nada
    '''
    f = shelve.open(ruta)
    for coche in coches:
        f[str(coche)] = coche
    f.close()

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,"electric")
        self.battery_size = 75


class Combustive(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,"combustive")
        self.battery_size = 75


if __name__ == '__main__':
    x = set()
    car1 =  ElectricCar('audi', 'a4', 2019)
    x.add(car1)
    car2 = ElectricCar('audi', 'electric', 2019)
    x.add(car2)
    car3 = Combustive('audi', 'a4', 2019)
    x.add(car3)
    car4 = Combustive('audi', 'q5', 2020)
    x.add(car4)   
    car5 = Combustive('audi', 'q5', 2020)
    x.add(car5)
    car6 = Combustive('audi', 'q5', 2020)
    ################################write
    x.add(car6)
    
    """"
    escribe el archivo.dat con los coches de la lista coches y lee el archivo"""

    escribir('coches.dat', x)
    coches = leer('coches.dat')
    for coche in coches:
        print(coche)
