Lplatillo = [["pollo    ", 20], ["pescado  ", 30]]
Lbebida = [["agua     ", 5], ["jugo     ", 10]]

def imprimirMenu():
    print("             Concepto  Costo")    
    print("Platillo: ")
    for elemento in Lplatillo:
        print("            ", elemento[0], str(elemento[1]))
    
    
    print("Bebida: ")
    for elemento in Lbebida:
        print("            ", elemento[0], str(elemento[1]))
    
    print()

def generarCombinaciones():
    combinaciones = {}
    contador = 1
    for plat in Lplatillo:
        for beb in Lbebida:
            combinaciones["Opción " + str(contador)] = [plat[0], beb[0]] 
            contador += 1
    return(combinaciones)

def generarOpcion(platillo, bebida):
    combinaciones = generarCombinaciones()
        
    for lista in Lplatillo:
        if platillo in lista:
            Platillo = platillo
            
    for lista in Lbebida:
        if bebida in lista:
            Bebida = bebida
    
    Lopcion = [Platillo, Bebida]
    
    for elemento in combinaciones:
        if Lopcion == combinaciones[elemento]:
            return (elemento, Lopcion)     

def imprimirCosto(platillo, bebida):
    """
    Recibe la cadena con la opción elegida por el cliente
    Entrega, en una cadena, el costo de su comida
    """ 
    Opcion = generarOpcion(platillo, bebida)
    costos = {}
    contador = 1
    for plat in Lplatillo:
        for beb in Lbebida:
            costos["Opción " + str(contador)] = plat[1] + beb[1]
            contador += 1

    print(Opcion[1], "    $" + str(costos[Opcion[0]]))



#imprimirMenu()
#print(generarCombinaciones())
#print(generarOpcion('pollo    ', 'jugo     '))
imprimirCosto("pescado  ", "agua     ")