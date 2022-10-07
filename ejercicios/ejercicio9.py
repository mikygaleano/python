import time

while True:
    
    horaEntrada = '08:00:00'
    hora = time.strftime('%H:%M:%S')

    if hora == '19:00:00':
        print(f'Son las {hora} debes irte a casa!!')
    elif hora < '19:00:00':
        print(f'Faltan { hora - 19:00:00 } para irte a casa')
        time.sleep(5)
    elif hora > '19:00:00' or hora < '08:00:00':
        print('Aún falta para ir al trabajo')
        time.sleep(5)
    else:
        print('Descansa!!')
        time.sleep(5)