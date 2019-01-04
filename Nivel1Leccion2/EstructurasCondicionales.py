"""
seAproxima = ''
seAproxima = input('¿Hay algún coche aproximándose? S=sí, cualquier letra=no: '+ seAproxima)
if seAproxima == 'S' or seAproxima == 's':
    print('Espera en donde estás')
else:
    print('Cruza la calle')
    """

  
estadoTiempo = ''
estadoTiempo = input('Sientes frío, calor o está templado: '+ estadoTiempo)
if estadoTiempo == 'frío':
    print('Usa un abrigo')
elif estadoTiempo == 'calor':
    print('Usa una camiseta y bermuda')
elif estadoTiempo == 'templado':
    print('Usa pantalón de mezclilla y playera')
else:
    print('Decide tú mismo')