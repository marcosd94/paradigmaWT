'''Vista para la carga de paciente'''
from Util.util import Util
from Modelo.paciente_model import Paciente

class View:
    def __init__(self):
        self.util=Util()

    def solicitar_datos_pac(self):
        print('-> Datos del nuevo Paciente')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        contenedor = Paciente(nombre,apellido,cedula,telefono,email,fecha,'','')
        return (contenedor)

    def solicitar_codigo_pac(self):
        print('-> Busqueda Paciente')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def busqueda_cedula_pac(self):
        print('\n')
        print('-> Busqueda de Paciente')
        codigo = self.util.leer_entero('Nro. Cedula: ',1)
        return (codigo)

    def listar_pacientes(self, lista):
        if lista != None and len(lista) != 0:
            print('\n-> Listado de Pacientes: \n')
            for paciente in lista:
                print ('* Codigo: ', paciente.codigof, ', Nombre: ', paciente.nombre+' '+paciente.apellido, ', Cedula: ',paciente.cedula)
        else:
            print('\n-> No existen registros')
        self.util.pause()

    def mostrar_resultado_pac(self,dato):
        if(dato != None and len(dato)!=0):
            print('\n-> Paciente Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* orden: ',dato['orden']+'\n')
        else:
            print('\n-> Paciente no encontrado')
        self.util.pause()

    def mostrar_msg_pac(self,msg):
        print('\n',msg+'\n\n')




