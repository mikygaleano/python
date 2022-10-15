
def escribirFichero (archivo, datos):
    f = open(archivo, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
            f.write(linea)

    f.close()

caracteres = [
    'Hola mundo!!',
    'Mi nombres Michael',
    'Alias Maikii'
]

escribirFichero('archivo.txt', caracteres)

