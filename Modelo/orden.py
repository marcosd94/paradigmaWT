# clase que guarda datos como el estado y el resultado de los analisis
from abc import ABCMeta, abstractmethod
from persistent import Persistent

class Orden(metaclass=ABCMeta):

    __metaclass__ = ABCMeta

    contador = -1
    def __init__(self,estado,id_orden ,fecha=None,codigo = None,cod_orden ='', resultado = []):
        self.estado = estado
        self.resultado = resultado
        self.id_orden = id_orden
        self.fecha = fecha
        self.codigo_paciente = codigo
        self.cod_orden = cod_orden
        self.__contabilizador()


    def decorador_pithon(func):
        '''funcion decorador para contabilizar el incremento de las ordenes'''

        def funcion_interna(cls, *args, **kwargs):
            try:
                resultado = func(cls, *args, **kwargs)
                cls.__increment_contador()
                return resultado

            except Exception as e:
                descr = 'Ocurrio un error inesperado{:}'.format(e)
                raise (descr)

        return funcion_interna

    @decorador_pithon
    def __contabilizador(self):
        '''este metodo solo sirve para activar el decorador'''
        pass

    @classmethod
    def __increment_contador(cls):
        '''la funcion interna llama al metodo a nivel de clase para hacer posible
        el conteo a nivel de clase'''
        cls.contador += 1

    def cantidad_ordenes(self):
        '''devuelve la cantidad de ordenes existentes'''
        return (self.contador)



