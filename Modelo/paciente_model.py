from Modelo.persona import Persona, Persistent
from Util.base import MiZODB, transaction


class Paciente(Persona, Persistent):
    def __init__(self, nombre='', apellido='', cedula=0, telefono='', email='', fecha_nac=None, orden='', codigof=''):
        Persona.__init__(self, nombre, apellido, cedula, telefono, email, fecha_nac)
        self.codigof = codigof
        self.orden = orden


    def __str__(self):
        return '''\
    Nombre:\t\t{}
    Apellido:\t\t{}
    Cedula:\t\t{}
    Telefono:\t\t{}
    Email:\t\t{}
    Fecha_Nacimiento:\t{}
    Codigo:\t\t{}
    Orden:\t\t{}'''.format(self.nombre,self.apellido,self.cedula,self.telefono,self.email,self.fecha_nac,self.codigof,self.orden)


    def carga_datos(self, codigo):
        self.codigof = codigo

    def cargar_persona(self, obj, clave):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            dbroot[clave] = obj
            transaction.commit()
            db.close()
            return ('Paciente creado!: ' + clave)
        except Exception as e:
            db.close()
            raise ('No se ha podido crear \n', e)

    def listar_persona(self):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            result = []
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, Paciente):
                    paciente = Paciente(obj.nombre, obj.apellido, obj.cedula, obj.telefono,
                                              obj.email, obj.fecha_nac, obj.orden, obj.codigof)
                    result.append(paciente)
            db.close()
            return result
        except Exception as e:
            db.close()
            raise('Error al consultar la base', e)

    def buscar_persona(self, codigo):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            persona = ''
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, Paciente):
                    if obj.codigof == codigo:
                        persona = {'nombrecompleto': obj.nombre +
                                                   ' ' + obj.apellido, 'codigo': obj.codigof,'cedula':obj.cedula,'orden':obj.orden}
            db.close()
            return persona
        except Exception as e:
            db.close()
            raise ('Error', e)

    def buscar_persona_cedula(self, cedula):
        '''Realiza la busqueda de la persona por cedula '''
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            persona = ''
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, Paciente):
                    if obj.cedula == cedula:
                        persona = {'nombrecompleto': obj.nombre +
                                                   ' ' + obj.apellido, 'codigo': obj.codigof,'cedula':obj.cedula,'orden':obj.orden}
            db.close()
            return persona
        except Exception as e:
            db.close()
            raise ('Error', e)
