def saludo():
    '''
    Entrada: no requiere parámetros
    Salida: imprime el saludo Hola Mundo
    '''
    print('Hola Mundo')

def multiplica(a, b):
    '''
    Entrada: dos valores a y b
    Salida: el producto de los valores
    '''
    return a*b

def calculo_primo(nume):
    if nume < 2:
        print('El número ', nume, ' NO es primo')
    elif nume == 2:
        print('El número ', nume, ' SÍ es primo')
    else:
        for i in range(2, nume):
            if nume %i == 0:
                print('El número ', nume, ' NO es primo')
                break
        else:
            print('El número ', nume, ' SÍ es primo')
            
def es_primo():
    numero = int(input('Ingresa un número entero positivo\ny te diré si es primo o no: '))
    return numero