from Modelo.persona import Persona, Persistent
from Util.base import MiZODB, transaction


class Medico(Persona, Persistent):
    def __init__(self, nombre, apellido, cedula, telefono, email, fecha_nac, cargo, codigof):
        Persona.__init__(self, nombre, apellido, cedula, telefono, email, fecha_nac)
        self.codigof = codigof
        self.cargo = cargo

    def carga_datos(self, codigo):
        self.codigof = codigo

    def cargar_persona(self, obj, clave):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            dbroot[clave] = obj
            transaction.commit()
            db.close()
            return ('Medico creado!: ' + clave)
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
                if isinstance(obj, Medico):
                    medico = Medico(obj.nombre, obj.apellido, obj.cedula, obj.telefono,
                                              obj.email, obj.fecha_nac, obj.cargo, obj.codigof)
                    result.append(medico)
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
                if isinstance(obj, Medico):
                    if obj.codigof == codigo:
                        persona = {'nombrecompleto': obj.nombre +
                                                   ' ' + obj.apellido, 'codigo': obj.codigof,'cedula':obj.cedula,'cargo':obj.cargo}
            db.close()
            return persona
        except Exception as e:
            db.close()
            raise ('Error', e)
