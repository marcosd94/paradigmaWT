# from Vista.orden_view import OrdenPaciente
from Modelo.paciente_model import Paciente
from Modelo.orden_model import OrdenModel
from Controlador.paciente_controller import ControladorPaciente
from Controlador.turno_controller import TurnoController
from datetime import date


class OrdenController:

    def __init__(self):
        # self.orden = OrdenPaciente()
        self.pac = Paciente()
        self.model = OrdenModel()
        self.cpac = ControladorPaciente()
        self.turno = TurnoController()

    def verificador_cupos(self):

        cargados = self.model.contador
        datosTope = self.turno.disponibilidad_x_turno()
        if (cargados >= datosTope):
            return False
        else:
            return True

    def cargar_orden(self):
        access = self.verificador_cupos()
        loop = True
        try:

            if (access):
                while (loop):
                    cedula = self.orden.solicitar_datos()
                    cliente = self.pac.buscar_persona_cedula(cedula)
                    if cliente == '':
                        msg = 'Paciente no registrado.'
                        self.orden.mostrar_msg2(msg)
                        consulta = self.orden.reg_cliente().upper()
                        if (consulta == 'S' or consulta == 'SI'):
                            self.cpac.cargar_paciente()

                    else:
                        nro = self.model.buscar_nro_orden()
                        if nro == 0:
                            nro = 1
                        else:
                            nro += 1
                        ahora = date.today().strftime('%d/%b/%Y')
                        tipo = self.model.tipos_analisis()
                        retorno = self.orden.cargar_orden(cliente, ahora, nro, tipo)
                        validacion = retorno[0].upper()
                        etipo = tipo[int(retorno[1]) - 1]
                        if (validacion == 'S' or validacion == 'SI'):
                            cod_o = 'OT_' + str(nro)
                            new_paciente = OrdenModel(ahora, nro, cliente['codigo'], etipo, cod_o)
                            exit = self.model.cargar_orden(new_paciente, cod_o)
                            self.orden.mostrar_msg(exit)
                            consulta = self.orden.cargar_otro().upper()
                            if (consulta == 'S' or consulta == 'SI'):
                                pass
                            else:
                                loop = False
                        else:
                            msg = 'Operacion Cancelada'
                            self.orden.mostrar_msg2(msg)
                            loop = False
            else:
                msg = 'No hay mas cupos disponibles para hoy'
                self.orden.mostrar_msg2(msg)

        except Exception as e:
            raise ('Error Fatal', e)

    def listar_orden(self):
        return self.model.listar_ordenes()
        # self.orden.listar_ordeness(ob)

    def orden_list(self, lang):
        '''funcion de orden superior para controlar las ordenes'''

        def listar_orden_pendiente():
            return self.model.listar_ordenes()

        def listar_orden_finalizada():
            return self.model.listar_ordenes_finalizadas()

        lang_func = {'pen': listar_orden_pendiente,
                     'fin': listar_orden_finalizada
                     }
        return lang_func[lang]()

        # self.orden.listar_ordeness(ob)

        # self.orden.listar_ordeness_finalizadas(ob)

    def buscar_orden(self, codigo):
        # codigo = self.orden.solicitar_codigo()
        return self.model.buscar_orden(codigo)
        # self.orden.mostrar_resultado(orden)

    def atender_orden(self, codigo):
        # codigo = self.orden.solicitar_codigo()
        orden = self.model.buscar_orden_modif(codigo)
        orden.estado = 'Finalizado'
        orden.fecha = date.today().strftime('%d/%b/%Y')
        self.model.cargar_orden(orden, orden.cod_orden)

        # if (orden == None):
        #    msg  = 'No se encuentra la orden de trabajo solicitada'
        #    self.orden.mostrar_msg2(msg)
        # else:
        #    orden.estado = 'Finalizado'
        #    orden.fecha = date.today().strftime('%d/%b/%Y')
        #    self.model.cargar_orden(orden,orden.cod_orden)
        #    msg = 'Orden concluida'
        #    self.orden.mostrar_msg2(msg)