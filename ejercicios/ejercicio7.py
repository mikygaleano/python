
class alumno:
    nombre : None
    nota : None

    def cuatrimestre (self):
        if self.nota >= 7 :
            return 'Aprobado'
        else:
            'Desaprobado'

a = alumno()

a.nombre = 'Michael'
a.nota = 8

print(f'El alumno {a.nombre} con nota de {a.nota} esta {a.cuatrimestre()}')