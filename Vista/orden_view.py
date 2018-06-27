#vista orden de analisis
from Util.util import Util
from Vista.paciente_view import View
from Controlador.orden_controller import OrdenController
from Modelo.orden_model import OrdenModel
import tkinter
import tkinter.ttk as ttk
from datetime import date

class OrdenPaciente:
    def __init__(self):
        self.util = Util()
        self.view = View()
        self.controller = OrdenController()

    def solicitar_datos(self):
        self.view.busqueda_cedula_pac(self)
        #return (cedula)

    def cargar_orden(self,cliente,ahora,nro,tipo):

        ordenes_registrar = tkinter.Tk()
        ordenes_registrar.title("CARGAR ORDEN")
        ordenes_registrar.geometry("800x500")



        def volver():
            ordenes_registrar.destroy()
            ordenes_registrar.eval('::ttk::CancelRepeat')

        def guardar():
            def cerrar_exp():
                ordenes_registrar.destroy()
                ordenes_registrar.eval('::ttk::CancelRepeat')
                #pacientes.eval('::ttk::CancelRepeat')
                #self.cargar_paciente()

            try:
                #ACA VA A IR TODA LA LÓGICA DE CARGA

                cod_o = 'OT_' + str(nro)
                new_paciente = OrdenModel(ahora, nro, cliente['codigo'], str(tipo.get()), cod_o)
                exit = self.controller.model.cargar_orden(new_paciente, cod_o)


            except Exception as e:
                alerta = tkinter.Message(ordenes_registrar, relief='raised',
                                         text='NO SE PUDO CARGAR LA ORDEN\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
            else:
                alerta = tkinter.Message(ordenes_registrar, relief='raised', text='ORDEN CARGADA CON EXITO', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(ordenes_registrar, font='Arial', text="DATOS DE LA ORDEN")
        titulo.place(bordermode='outside', height=20, width=300, x=100)


        # Etiquetas
        lbl_fecha = tkinter.Label(ordenes_registrar, font='Arial', text="Fecha", justify='left')
        lbl_fecha.place(bordermode='outside', height=20, width=300, x=50, y=55)
        lbl_nro_orden = tkinter.Label(ordenes_registrar, font='Arial', text="Orden de Analisis Nro", justify='left')
        lbl_nro_orden.place(bordermode='outside', height=20, width=300, x=50, y=80)
        lbl_nombre = tkinter.Label(ordenes_registrar, font='Arial', text="Paciente", justify='left')
        lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=105)
        lbl_codigo = tkinter.Label(ordenes_registrar, font='Arial', text="Código", justify='left')
        lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=130)
        lbl_tipo = tkinter.Label(ordenes_registrar, font='Arial',text="Tipo de analisis a realizar")
        lbl_tipo.place(bordermode='outside', height=20, width=300, x=50, y=155)

        # lbl_orden = tkinter.Label(ordenes_registrar, font='Arial', text="Orden", justify='left')
        # lbl_orden.place(bordermode='outside', height=20, width=300, x=50, y=155)

        # Campos de Texto
        fecha_result = tkinter.Label(ordenes_registrar, font='Arial', text=ahora, justify='left')
        fecha_result.place(bordermode='outside', height=20, width=300, x=350, y=55)
        nro_orden_identidad_result = tkinter.Label(ordenes_registrar, font='Arial', text=nro, justify='left')
        nro_orden_identidad_result.place(bordermode='outside', height=20, width=300, x=350, y=80)
        nombre_result = tkinter.Label(ordenes_registrar, font='Arial', text=cliente['nombrecompleto'], justify='left')
        nombre_result.place(bordermode='outside', height=20, width=300, x=350, y=105)
        codigo_result = tkinter.Label(ordenes_registrar, font='Arial', text=cliente['codigo'], justify='left')
        codigo_result.place(bordermode='outside', height=20, width=300, x=350, y=130)
        tipo=ttk.Combobox(ordenes_registrar,value=tipo,state= 'readonly')
        tipo.place(bordermode='outside', height=20, width=300, x=350, y=155)

        # orden_result = tkinter.Label(ordenes_registrar, font='Arial', text=dato['orden'], justify='left')
        # orden_result.place(bordermode='outside', height=20, width=300, x=350, y=155)


        # Campos de Texto
        #codigo = tkinter.Entry(ordenes_registrar, font='times')
        #codigo.place(bordermode='outside', height=20, width=300, x=350, y=30)

        guardar = tkinter.Button(ordenes_registrar, text="Guardar", command=guardar)
        guardar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(ordenes_registrar, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        ordenes_registrar.mainloop()

        #print('\n-> Fecha:', ahora)
        #print('-> Orden de Analisis Nro: ',nro)
        #print('-> Paciente: ',cliente['nombrecompleto'],' codigo: ',cliente['codigo'])
        #print('-> Tipo de analisis a realizar')
        #for i,tp in enumerate(tipo):

    #print('\t',i+1,'- ',tp)
            #etipo = self.util.leer_entero('',1)
        #validacion = self.util.leer_cadena('Confirmar "S" :: Cancelar "N" ',True)
        #print('\n')
        #return (validacion,etipo)


    def solicitar_codigo(self):
        print('-> Busqueda Orden de Analisis')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def listar_ordenes(self):
        def cerrar_exp():
            ordenes.destroy()
            #ordenes.eval('::ttk::CancelRepeat')
            #self.cargar_paciente()

        ordenes = tkinter.Tk()
        ordenes.title("LISTADO DE ORDENES")
        ordenes.geometry("1000x500")

        def volver():
            ordenes.destroy()

        mylistbox = tkinter.Listbox(ordenes, height=12, width=100, font=('times', 13))
        mylistbox.place(x=32, y=110)
        orden = self.controller.listar_orden()
        if orden != None and len(orden) != 0:
            for values in orden:
                mylistbox.insert('end', '* Nro. Orden: ' + str(values.id_orden) +', Cod. Paciente: ' + str(values.codigo_paciente) + ', Estado: ' + str(values.estado) +  ', Fecha: ' + str(values.fecha) + ', Tipo: ' + str(values.tipo) )
            titulo = tkinter.Label(ordenes, font='Arial', text="LISTADO DE PACIENTES")
            titulo.place(bordermode='outside', height=20, width=600, x=100, y=30)
            volver = tkinter.Button(ordenes, text="Volver", command=volver)
            volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
            ordenes.mainloop()
        else:
            alerta = tkinter.Message(ordenes, relief='raised',
                                     text='NO EXISTEN REGISTROS ' , width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")


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


    def registrar_orden(self):

        access = self.controller.verificador_cupos()
        loop = True
        try:
            def cerrar_exp():
                ordenes.destroy()
                # ordenes.eval('::ttk::CancelRepeat')
                #self.cargar_paciente()

            if(access):
                self.solicitar_datos()
                #print (cedula)

            else:
                ordenes = tkinter.Tk()
                ordenes.title("CARGAR PACIENTE")
                ordenes.geometry("500x300")
                alerta = tkinter.Message(ordenes, relief='raised', text='No hay mas cupos disponibles para hoy', width=200)
                alerta.place(bordermode='outside', height=250, width=400, y=30, x=50)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
                #msg = 'No hay mas cupos disponibles para hoy'
                #self.orden.mostrar_msg2(msg)

        except Exception as e:

            ordenes = tkinter.Tk()
            ordenes.title("CARGAR PACIENTE")
            ordenes.geometry("500x300")
            alerta = tkinter.Message(ordenes, relief='raised', text=str(e), width=200)
            alerta.place(bordermode='outside', height=250, width=400, y=30, x=50)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

    def imprimir(self,cedula):
        cliente = self.controller.pac.buscar_persona_cedula(cedula)

        if cliente == '':
            print('Paciente no registrado.')
            #self.mostrar_msg2(msg)
            return ''
            consulta = self.orden.reg_cliente().upper()
            if (consulta == 'S' or consulta == 'SI'):
                self.cpac.cargar_paciente()

        else:
            nro = self.controller.model.buscar_nro_orden()
            if nro == 0:
                nro = 1
            else:
                nro += 1
            ahora = date.today().strftime('%d/%b/%Y')
            tipo = self.controller.model.tipos_analisis()
            retorno = self.cargar_orden(cliente, ahora, nro, tipo)

            #consulta = self.cargar_otro().upper()
            #if (consulta == 'S' or consulta == 'SI'):
            #    self.registrar_orden()