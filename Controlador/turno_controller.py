import datetime as fecha
from Modelo.turno_model import TurnoModel

class TurnoController():
    turnos = {'T1': ['06:00:00', '13:00:00'], 'T2': ['13:00:00', '23:59:00']}
    def __init__(self,orden=''):
        self.orden = orden
        self.hora_actual = None
        self.tr = self.periodo()
        self.turno = TurnoModel()


    def turno_actual(self):
        '''capturamos la hora actual en una cadena de caracteres'''
        self.hora_actual = fecha.datetime.now().strftime('%H:%M:%S')
        return self.hora_actual

    def periodo(self):
        '''verificamos que el horario este dentro de cada turno 1 er turno , 2 do turno y 0 fuera de turno'''
        hora = self.turno_actual()
        t1 = self.horario_laboral('T1')
        t2 = self.horario_laboral('T2')
        if(hora >= t1[0] and hora < t1[1]):
            return 1
        elif(hora >= t2[0] and hora <= t2[1]):
            return 2
        else:
            return 0


    def horario_laboral(self, valor):
        '''devuelve lo asignado como rango de fecha T1 y T2'''
        return self.turnos[valor]

    def disponibilidad_x_turno(self):
        valor = self.turno.ordenes_disponibles()
        return valor