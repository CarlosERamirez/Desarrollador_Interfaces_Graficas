#REPARTIR BARAJA
cartas  = 40
mesa = {'jugador1': 0, 'jugador2': 0, 'jugador3': 0, 'jugador4': 0, 'jugador5': 0}
while cartas > 0:
    for personas in mesa:
        cartas -= 1
        mesa[personas] += 1
print('Cartas para cada jugador: ', mesa)
print('Cartas restantes', cartas)

#LLENAR VASOS DE BEBIDA
barra = ['cliente1', 'cliente2', 'cliente3']
for clientes in barra:
    print('Agregando líquido a: ', clientes)
    no_lleno = True
    while no_lleno:
        esta_lleno = input('¿Está suficientemente lleno?S o N: ')
        if esta_lleno == 'S':
            no_lleno = False
        else:
            no_lleno = True
print('Gracias a todos por su compra')