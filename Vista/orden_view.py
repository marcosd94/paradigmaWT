#vista orden de analisis
from Util.util import Util
from Vista.paciente_view import View

class OrdenPaciente:
    def __init__(self):
        self.util = Util()
        self.view = View()

    def solicitar_datos(self):
        cedula = self.view.busqueda_cedula_pac()
        return (cedula)

    def cargar_orden(self,cliente,ahora,nro,tipo):
        print('\n-> Fecha:', ahora)
        print('-> Orden de Analisis Nro: ',nro)
        print('-> Paciente: ',cliente['nombrecompleto'],' codigo: ',cliente['codigo'])
        print('-> Tipo de analisis a realizar')
        for i,tp in enumerate(tipo):
            print('\t',i+1,'- ',tp)
        etipo = self.util.leer_entero('',1)
        validacion = self.util.leer_cadena('Confirmar "S" :: Cancelar "N" ',True)
        print('\n')
        return (validacion,etipo)


    def solicitar_codigo(self):
        print('-> Busqueda Orden de Analisis')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def listar_ordeness(self, lista):
        if lista!=None and len(lista)!=0:
            print('\n-> Ordenes de Analisis Pendientes : \n')
            for ord in lista:
                print ('* Cod. Orden: ', ord.cod_orden, ', Cod. Paciente: ', ord.codigo_paciente, ', Estado: ',ord.estado, ', Fecha: ',ord.fecha,', Tipo: ',ord.tipo,)
            self.util.pause()
        else:
            print('\n-> No existen registros')
            self.util.pause()

    def listar_ordeness_finalizadas(self, lista):
        if lista!=None and len(lista)!=0:
            print('\n-> Ordenes de Analisis Finalizadas : \n')
            for ord in lista:
                print ('* Cod. Orden: ', ord.cod_orden, ', Cod. Paciente: ', ord.codigo_paciente, ', Estado: ',ord.estado, ', Fecha: ',ord.fecha,', Tipo: ',ord.tipo,)
            self.util.pause()
        else:
            print('\n-> No existen registros')
            self.util.pause()

    def mostrar_resultado(self,dato):
        if dato != None and len(dato)>0:
            print('\n-> Orden Buscada Cod: ',dato['codigo'])
            print('* Codigo Paciente: ',dato['cod_paciente'])
            print('* Tipo de Analisis: ',dato['tipo'])
            print('* Estado: ',dato['estado']+'\n')

        else:
            print('\n-> Orden no encontrada')
        self.util.pause()

    def reg_cliente(self):
        print('\n')
        print('-> Desea registrar al paciente ?')
        consulta = self.util.leer_cadena('Confirmar "S" :: Cancelar "N" ',True)
        print('\n')
        return consulta

    def cargar_otro(self):
        print('\n')
        print('-> Desea cargar otra Orden?')
        consulta = self.util.leer_cadena('Confirmar "S" :: Cancelar "N" ', True)
        print('\n')
        return consulta

    def mostrar_msg(self,msg):
        print('\n', msg[0], msg[1],'\n')
        self.util.pause()

    def mostrar_msg2(self,msg):
        print('\n',msg+'\n')
        self.util.pause()
