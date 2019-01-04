def calculo_primo(nume):
    """
    Casos base:
    primer prueba deliberadamente errónea
    >>> calculo_primo(0)
    El número 0 SÍ es primo
    >>> calculo_primo(1)
    El número 1 NO es primo
    >>> calculo_primo(2)
    El número 2 SÍ es primo
    
    Primo:
    >>> calculo_primo(97)
    El número 97 SÍ es primo
    
    No primo: 
    >>> calculo_primo(95)
    El número 95 NO es primo
    """
    if nume < 2:
        print('El número ' + str(nume) + ' NO es primo')
    elif nume == 2:
        print('El número ' + str(nume) + ' SÍ es primo')
    else:
        for i in range(2, nume):
            if nume %i == 0:
                print('El número ' + str(nume) + ' NO es primo')
                break
        else:
            print('El número ' + str(nume) + ' SÍ es primo')
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()
