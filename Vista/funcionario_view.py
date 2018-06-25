'''Vista para la carga de funcionarios'''
from Util.util import Util
from Modelo.funcionario_model import Funcionario

class View:
    def __init__(self):
        self.util=Util()

    def solicitar_datos(self):
        print('-> Datos del nuevo Funcionario')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        cargo = self.util.leer_cadena('Cargo: ',False)
        contenedor = Funcionario(nombre,apellido,cedula,telefono,email,fecha,cargo,'')
        return (contenedor)

    def solicitar_codigo(self):
        print('-> Busqueda por codigo de Funcionario')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def listar_funcionarios(self, lista):
        if lista!=None and len(lista)!=0:
            print('\n-> Listado de Funcionarios en la base de datos: \n')
            for funcionario in lista:
                print ('* Codigo: ', funcionario.codigof, ', Nombre: ', funcionario.nombre+' '+funcionario.apellido, ', Cargo: ',funcionario.cargo)
            self.util.pause()
        else:
            print('\n-> No existen registros')
            self.util.pause()

    def mostrar_resultado(self,dato):
        if dato != None and len(dato)>0:
            print('\n-> Funcionario Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* Cargo: ',dato['cargo']+'\n')
        else:
            print('\n-> Funcionario no encontrado')
        self.util.pause()

    def mostrar_msg(self,msg):
        print('\n',msg+'\n\n')




