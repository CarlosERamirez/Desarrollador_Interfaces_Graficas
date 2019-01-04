class Menu:
    def __init__(self, cliente):
        self.Lplatillo = [["pollo    ", 20], ["pescado  ", 30]]
        self.Lbebida = [["agua     ", 5], ["jugo     ", 10], ["refresco ", 10]]
        self.cliente = cliente
        print('Bienvenido, ' + self.cliente)
        
    def imprimirMenu(self):
        print("             Concepto  Costo")    
        print("Platillo: ")
        for elemento in self.Lplatillo:
            print("            ", elemento[0], str(elemento[1]))
    
        print("Bebida: ")
        for elemento in self.Lbebida:
            print("            ", elemento[0], str(elemento[1]))
    
        print()
    
    def generarCombinaciones(self):
        """
        Retorna las posibles combinaciones del menú
        Se usa dentro de generarOpcion()
        """
        combinaciones = {}
        contador = 1
        for plat in self.Lplatillo:
            for beb in self.Lbebida:
                combinaciones["Opción " + str(contador)] = [plat[0], beb[0]] 
                contador += 1
        return(combinaciones)
    
    def generarOpcion(self, platillo, bebida):
        """
        Se usa dentro de imprimirCosto()
        Toma los parámetros de imprimirCosto()
        Retorna una tupla con:
           una clave del diccionario 'combinaciones'
           el valor correspondiente a esa clave del diccionario
        """
    
        combinaciones = self.generarCombinaciones()
        
        for lista in self.Lplatillo:
            if platillo in lista:
                Platillo = platillo
            
        for lista in self.Lbebida:
            if bebida in lista:
                Bebida = bebida
    
        Lopcion = [Platillo, Bebida]
    
        for elemento in combinaciones:
            if Lopcion == combinaciones[elemento]:
                return (elemento, Lopcion)        
    
    def imprimirCosto(self, platillo, bebida):
        """
        Recibe dos cadenas con las opciones elegidas por el cliente
        Imprime, en una cadena, el costo de su comida
        """ 
        Opcion = self.generarOpcion(platillo, bebida)
        costos = {}
        contador = 1
        for plat in self.Lplatillo:
            for beb in self.Lbebida:
                costos["Opción " + str(contador)] = plat[1] + beb[1]
                contador += 1

        print(self.cliente, Opcion[1], "$" + str(costos[Opcion[0]]))

menuComida = Menu("Carlos")
menuComida.imprimirMenu()
menuComida.imprimirCosto("pescado  ", "agua     ")