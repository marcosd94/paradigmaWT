from Modelo.medico_model import Medico
from Vista.medico_view import View
from Util.util import Util


class ControladorMedico():
    """Clase Controlador de los Medicos"""

    def __init__(self):
        self.var = Medico('', '', 0, '', '', '', '', '')
        self.view = View()
        self.util = Util()

    def cargar_medico(self):
        self.var = self.view.solicitar_datos_med()
        codigo = self.util.genera_codigo(self.var.nombre, self.var.apellido, self.var.cedula)
        existe=self.var.buscar_persona(codigo)
        if existe != None and len(existe) !=0:
            msg = 'El medico {} ya esta existe en la base'.format(codigo)
            self.view.mostrar_msg_med(msg)
        else:
            self.var.carga_datos(codigo)
            msg = self.var.cargar_persona(self.var,codigo)
            self.view.mostrar_msg_med(msg)

    def listar_medico(self):
        ob = self.var.listar_persona()
        self.view.listar_medicos(ob)

    def buscar_medico(self):
        codigo = self.view.solicitar_codigo_med()
        paciente = self.var.buscar_persona(codigo)
        self.view.mostrar_resultado_med(paciente)
