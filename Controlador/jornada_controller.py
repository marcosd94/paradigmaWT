from Controlador.turno_controller import TurnoController
from datetime import date
from Modelo.jornada_model import JornadaModel



class JornadaController:
    '''Se ejecuta la app del laboratorio valida que jornada laboral es especifica el turno y la disponibilidad'''
    def __init__(self):
        self.turnos = TurnoController()
        self.fecha_actual = date.today().strftime('%d/%b/%Y')
        self.ultima_fecha = None
        self.model = JornadaModel()
        self.numero = self.nueva_jornada()
        self.periodo = self.turnos.tr




    def nueva_jornada(self):
        '''el metodo verifica si la fecha del ultimo ingreso es menor al actual y actualiza en la base'''
        self.ultima_fecha= self.model.traer_fecha()
        num = self.model.contador

        if str(self.ultima_fecha) < str(self.fecha_actual):
            num += 1
            self.model.fecha = self.fecha_actual
            self.model.contador = num
            self.model.cargar_jornada(self.model)
            return num
        elif(self.ultima_fecha == None):
            self.model.fecha = self.fecha_actual
            self.model.cargar_jornada(self.model)
            return num
        else:
            return num





