import time
def añoBisiesto ():
    añoIngresado = int(input(f'ingrese un año por favor: '))
    if (añoIngresado % 4 == 0 and añoIngresado % 100 != 0) or añoIngresado % 400 == 0:
        print(f'el año: {añoIngresado} ingresado es bisiesto')
    else:
        print(f'el año: {añoIngresado} ingresado no es bisiesto')

añoBisiesto()
time.sleep(5)