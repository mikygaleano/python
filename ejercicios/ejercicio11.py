## cargando datos de un objeto a un archivo bin ##

# r: lectura
# a: append/adjuntar
# w: escritura
# x: create

# t: texto
# b: binary

# +

import pickle


class vehiculo:
    marca = 'BMW'
    modelo = 'Sport'

    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
coche = vehiculo('Ferrari', 'Deportivo')
f = open('vehiculos.bin', 'wb')
pickle.dump(coche, f)
f.close

f = open('vehiculos.bin', 'rb')
coche = pickle.load(f)
f.close()

print(type(coche))
print(f'el vehiculo es {coche.marca} modelo {coche.modelo} ')