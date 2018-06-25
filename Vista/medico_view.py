'''Vista para la carga de medicos'''
from Util.util import Util
from Modelo.medico_model import Medico

class View:
    def __init__(self):
        self.util=Util()

    def solicitar_datos_med(self):
        print('-> Datos del nuevo Medico')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        cargo = self.util.leer_cadena('Cargo: ',False)
        contenedor = Medico(nombre,apellido,cedula,telefono,email,fecha,cargo,'')
        return (contenedor)

    def solicitar_codigo_med(self):
        print('-> Busqueda Medico')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def listar_medicos(self, lista):
        if lista != None and len(lista) != 0:
            print('\n-> Listado de Medicos: \n')
            for medico in lista:
                print ('* Codigo: ', medico.codigof, ', Nombre: ', medico.nombre+' '+medico.apellido, ', cargo: ',medico.cargo)
        else:
            print('\n-> No existen registros')
        self.util.pause()

    def mostrar_resultado_med(self,dato):
        if(dato != None and len(dato)!=0):
            print('\n-> Medico Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* cargo: ',dato['cargo']+'\n')
        else:
            print('\n-> Paciente no encontrado')
        self.util.pause()

    def mostrar_msg_med(self,msg):
        print('\n',msg+'\n\n')




