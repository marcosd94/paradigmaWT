# clase que guarda datos basicos de persona
from abc import ABCMeta, abstractmethod
from persistent import Persistent

class Persona(metaclass=ABCMeta):

    __metaclass__ = ABCMeta

    def __init__(self, nombre, apellido, cedula, telefono, email, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.email = email
        self.fecha_nac = fecha_nac

    def carga_datos(self, codigo):
        pass

    def cargar_persona(self, obj, clave):
        pass

    def listar_persona(self):
        pass

    def buscar_persona(self, codigo):
        pass
