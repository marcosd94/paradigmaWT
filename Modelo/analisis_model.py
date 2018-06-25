
from Modelo.orden import Orden,Persistent
from Util.base import MiZODB, transaction

class Analisis(Orden,Persistent):
    def __init__(self,paciente,id_orden,fecha):
        Orden.__init__(self,id_orden,fecha)
        self.paciente = paciente


    def cargar_analisis(self,):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            dbroot[clave] = obj
            transaction.commit()
            db.close()
            return ('Analisis creado!: ' + clave)
        except Exception as e:
            db.close()
            raise ('No se ha podido crear \n', e)

