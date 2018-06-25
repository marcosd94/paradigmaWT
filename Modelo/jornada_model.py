from Util.base import MiZODB, transaction
from persistent import Persistent



class JornadaModel(Persistent):
    def __init__(self):
        aux = self.conteo_jornada()
        self.contador = aux[0]
        self.fecha = aux[1]

    def traer_fecha(self):
        return self.fecha

    def conteo_jornada(self):
        """la funcion conteo devuelve el mayor nro de jornada en la base """
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            nro = 1
            fecha = None
            cont = True
            for key in dbroot.keys():
                obj = dbroot[key]

                if isinstance(obj, JornadaModel):
                    if cont:
                        nro = obj.contador
                        fecha = obj.fecha
                        cont = False

                    if obj.contador > nro:
                        nro = obj.contador
                        fecha = obj.fecha
            db.close()

            return (nro,fecha)
        except Exception as e:
            db.close()
            raise ('Error', e)

    def cargar_jornada(self, obj):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            dbroot[obj.contador] = obj
            transaction.commit()
            db.close()
            return ('Ok')
        except Exception as e:
            db.close()
            raise ('No se ha podido crear \n', e)