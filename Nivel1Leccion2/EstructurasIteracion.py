
num = int(input('Ingresa un número par: '))
while num %2 != 0:
    num = int(input('Ingresaste un número impar, ingresa otro: '))
print('Excelente')

miCadena = 'hola mundo'
for letra in miCadena:
    print(letra.upper())
    
for numero in range(len(miCadena)):
    print(numero +  1, miCadena[numero])

for numero in range(1, 10, 2):
    print('El cuadrado de ', numero, 'es: ', numero**2)
    
miLista = list(miCadena)
for elemento in miLista[:]:
    miLista.remove(elemento)
    miLista.append(elemento*2)
print(miLista)
    
miTupla = (1,'pal',3.51)
for elemento in miTupla:
    print(elemento,'es de tipo: ',type(elemento))