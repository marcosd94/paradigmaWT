from Modelo.orden import Orden, Persistent
from Util.base import MiZODB, transaction


class OrdenModel(Orden, Persistent):

    def __init__(self,fecha=None,nro_orden=0,cod_cliente='',tipo=None,cod_orden ='',estado = 'Pendiente',):
        Orden.__init__(self,estado=estado,id_orden=nro_orden,fecha=fecha,codigo=cod_cliente,cod_orden=cod_orden)
        self.tipo = tipo

    def tipos_analisis(self):
        datos = ['Analisis Clinicos y Bacteriologicos','Imagenes']
        return datos

    def cargar_orden(self, obj, nro_orden):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            dbroot[nro_orden] = obj
            transaction.commit()
            db.close()
            return ('Orden de Analisis creado cod.: ',nro_orden)
        except Exception as e:
            db.close()
            raise ('No se ha podido crear \n', e)

    def buscar_nro_orden(self):
        """la funcion buscar devuelve el mayor nro de orden en la base"""
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            nro = 0
            cont = True
            for key in dbroot.keys():
                obj = dbroot[key]

                if isinstance(obj, OrdenModel):
                    if cont:
                        nro = obj.id_orden
                        cont = False

                    if obj.id_orden > nro:
                        nro = obj.id_orden
            db.close()
            return nro
        except Exception as e:
            db.close()
            raise ('Error', e)

    def listar_ordenes(self):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            result = []
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, OrdenModel):
                    orden = OrdenModel(obj.fecha, obj.id_orden,obj.codigo_paciente,obj.tipo,obj.estado)
                    result.append(orden)
            db.close()
            return result
        except Exception as e:
            db.close()
            raise('Error al consultar la base', e)

    def buscar_orden(self,codigo):
        try:
            db = MiZODB('./Data.fs')
            dbroot = db.raiz
            orden = ''
            for key in dbroot.keys():
                obj = dbroot[key]
                if isinstance(obj, OrdenModel):
                    if key == codigo:
                        orden = {'codigo': obj.cod_orden, 'cod_paciente': obj.codigo_paciente,'tipo':obj.tipo,'estado':obj.estado}
            db.close()
            return orden
        except Exception as e:
            db.close()
            raise ('Error', e)


