from Modelo.funcionario_model import Funcionario
#from Vista.funcionario_view import View
from Util.util import Util


class ControladorFuncionario():
    """Clase Controlador de los Funcionarios"""

    def __init__(self):
        self.fun = Funcionario('', '', 0, '', '', '', '', '')
        #self.view = View()
        self.util = Util()


#    def mostrar_formulario_funcionario(self):
#        self.view.cargar_funcionario()

    def cargar_func(self, funcionario):
        try:
            self.fun = funcionario
            codigo = self.util.genera_codigo(self.fun.nombre, self.fun.apellido, self.fun.cedula)
            existe = self.fun.buscar_persona(codigo)
            if existe != None and len(existe) != 0:
                msg = 'El funcionario {} ya existe en la base'.format(codigo)
                self.view.mostrar_msg(msg)
            else:
                self.fun.carga_datos(codigo)
                msg = self.fun.cargar_persona(self.fun, codigo)
                #self.view.mostrar_msg(msg)
        except KeyboardInterrupt as e:
            raise Exception('Carga interrumpida.')
        except Exception as ex:
            raise Exception(ex)

    def listar_funcionarios(self):
        return self.fun.listar_persona()
        #self.view.listar_funcionarios(ob)

    def buscar_funcionarios(self):
        codigo = self.view.solicitar_codigo()
        return self.fun.buscar_persona(codigo)
        #self.view.mostrar_resultado(funcionario)
