from Modelo.paciente_model import Paciente
#from Vista.paciente_view import View
from Util.util import Util


class ControladorPaciente():
    """Clase Controlador de los Pacientes"""

    def __init__(self):
        self.var = Paciente('', '', 0, '', '', '', '', '')
        #self.view = View()
        self.util = Util()

    def cargar_paciente(self,paciente):
        self.var = paciente
        codigo = self.util.genera_codigo(self.var.nombre, self.var.apellido, self.var.cedula)
        existe=self.var.buscar_persona(codigo)
        if existe != None and len(existe) !=0:
            raise Exception('El paciente {} ya esta existe en la base'.format(codigo))
            #self.view.mostrar_msg_pac(msg)
        else:
            self.var.carga_datos(codigo)
            msg = self.var.cargar_persona(self.var,codigo)
            ##self.view.mostrar_msg_pac(msg)

    def listar_paciente(self):
        return self.var.listar_persona()
        #self.view.listar_pacientes(ob)

    def buscar_paciente(self, codigo):
        #codigo = self.view.solicitar_codigo_pac()
        return self.var.buscar_persona(codigo)
        #self.view.mostrar_resultado_pac(paciente)

    def solicitar_oa(self):
        '''Se encarga de crear una orden de trabajo nueva'''
