"""alumnos = ('Ana', 'Beto', 'Claudia')
notas = [6.7, 8.2, 9.9]
calificaciones = {}
#for index in range(len(alumnos)):
index = 0
while index < len(alumnos):
    calificaciones[alumnos[index]] = notas[index]
    index += 1
print(calificaciones)"""

entrada = ["sopa", "crema", "spaguetti"]
platillo = ["res", "pollo", "pescado"]
postre = ["pastel", "gelatina", "flan"]

combinaciones = {}
contador = 1
for ent in entrada:
    for plat in platillo:
        for pos in postre:
            combinaciones["Opción " + str(contador)] = ent + '-' + plat + '-' + pos
            contador += 1
print(combinaciones)
for claves in combinaciones:
    print(combinaciones[claves])
