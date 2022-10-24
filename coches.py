'''
Clases para manejo de coches de combustión y eléctricos.
Ejemplo para uso de clase y herencia.
'''

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
    if os.path.exists(ruta):
        f = open(ruta) # opcional 'r'
        texto = f.read()
        f.close()
        return texto
    else:
        print(f'No existe el archivo {ruta}')
        return None
'''



class ElectricCar(Car):
'''
def escribir(ruta, texto):
    '''
    Escribe el texto en el archivo de la ruta.
    Si existe el archivo, aÃ±ade el contenido al final
    del mismo.
    No devuelve nada
    '''
    if os.path.exists(ruta):
        f = open(ruta, 'a')  # f -> objeto file
    else:
        f = open(ruta, 'w')
    f.write(texto)
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
    for car in x:    
        print(car.name, car.model, car.year, car.type)
        e=f'{car.name} {car.model} {car.year} {car.type}'
        escribir('coches.txt', e)
        leer
        print(leer('coches.txt'))
