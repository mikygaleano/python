# indice de masa corporal

peso = int(input('Ingrese su peso, por favor: '))
talla = float(input('Ingrese su altura en metros, por favor: '))

def imc ():
    calculo = round(peso / pow(talla, 2), 2)
    print(f'Su indice de masa corporal es: {str(calculo)}')

imc()