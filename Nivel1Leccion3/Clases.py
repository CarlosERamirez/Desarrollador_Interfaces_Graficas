class Coches:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "negro"
        
    def elColor(self):
        return self.color
    
    def __str__(self):
        #return "{" + self.marca + " " + self.modelo + " " + self.color + "}"
        return "!mi coche!"



miCoche = Coches('Mustang Shelby', '2017')

#print(miCoche.elColor())

#print(type(miCoche))

print(miCoche)





























"""
class CocheDeportivo(Coches):
    def __init__(self, marca, modelo, velMax):
        Coches.__init__(self, marca, modelo)
        self.velMax = velMax
       

    def __str__(self):
        return "{" + self.marca + " " + self.modelo + " " + self.color + " " + self.velMax + "}"



miCoche = CocheDeportivo("Corvette", "2017", "250 kph")

print(miCoche)
print(isinstance(miCoche, CocheDeportivo))
print(isinstance(miCoche, Coches))
"""






















"""from datetime import *
class Person(object):
    def __init__(self, name):
        self.name = name
        self.bithday = None
        self.lastName = name.split(" ")[-1]
    
    def getLastName(self):
        return self.lastName
    
    def __str__(self):
        return self.name
    
    def setBirth(self, month, day, year):
        self.birthday = date(year, month, day)
    
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (date.today() - self.birthday).days
    
carlos = Person('Carlos Ramírez')
print(carlos.getLastName())
carlos.setBirth(3, 3, 1993)
print(carlos.getAge())"""