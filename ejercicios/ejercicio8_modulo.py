# modulo calculadora
import time
def suma (a, b):
    print(a + b)

def resta (a, b):
    print(a - b)

def multiplicar (a, b):
    print(a * b)

def divicion (a, b):
    print(a / b)

def calculadora():
    while True:
        print('******** Bienvenido a su calculadora *********')
        elegir = input('pulse "espacio" para apagar o "a" para seguir: ')
        
        if elegir == ' ':
            print('Chau!!')
            break
        if elegir == 'a':
            print('Ingrese los dos numeros que desea calcular')
            num1 = int(input('Numero 1: '))
            num2 = int(input('Numero 2: '))
            print('Por favor ingrese la operación que desea realizar')
            print('******* Menu *******')
            print('opcion "1" suma')
            print('opcion "2" resta')
            print('opcion "3" multiplicar')
            print('opcion "4" dividir')
            print('opcion "5" finalizar calculadora')
            opcion = int(input('ingrese su opcion a continuación: '))

            if opcion == 5:
                print('Adios!!')
                break
            elif opcion == 1:
                print(suma(num1, num2))
            elif opcion == 2:
                print(resta(num1, num2))
            elif opcion == 3:
                print(multiplicar(num1, num2))
            elif opcion == 4:
                print(divicion(num1, num2))
            else:
                print('Opción invalida')
        else:
            print('Opción invalida')
        
        time.sleep(2)    

    
