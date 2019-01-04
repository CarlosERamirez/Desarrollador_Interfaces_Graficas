class Planetas:
    def __init__(self, nombre, diametro, distanciasol):
        self.nombre = nombre
        self.diametro = diametro
        self.distancia = distanciasol
    
    def getDiametro(self):
        return str(self.diametro) +  ' km de diámetro'
    
    def getDistanciaSol(self):
        return str(self.distancia) + ' millones de km'
    
    def __str__(self):
        return 'Planeta ' + self.nombre

class PlanetasconSatelites(Planetas):
    def __init__(self, nombre, diametro, distanciasol, satelites):
        Planetas.__init__(self, nombre, diametro, distanciasol)
        self.satelites = satelites
    
    def getDiametro(self):
        return str(self.diametro) +  ' km de diámetro'
    
    def getDistanciaSol(self):
        return str(self.distancia) + ' millones de km'
    
    def getSatelites(self):
        return str(self.satelites) + ' satélites'
    
    def __str__(self):
        return 'Planeta ' + self.nombre

tierra = PlanetasconSatelites('Tierra', 12756, 149.6, 1)
print(tierra.getSatelites())