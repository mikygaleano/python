
import time

hora = time.strftime('%H:%M:%S')
horaIngreso = time.strftime('08:00:00')
horaSalida = time.strftime('19:00:00')


def irte ():
    print(horaIngreso - hora)

while True:
    
    if hora == horaSalida:
        print(f'Son las {hora} debes irte a casa!!')
    elif hora < horaSalida:
        print(f'Falta para irte a casa')
        time.sleep(5)
    elif hora > horaSalida or hora < horaIngreso:
        print(f'Aún falta para ir al trabajo')
        time.sleep(5)
    else:
        print('Descansa!!')
        time.sleep(5)