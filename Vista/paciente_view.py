'''Vista para la carga de paciente'''
from Util.util import Util
from Modelo.paciente_model import Paciente
from Controlador.paciente_controller import  ControladorPaciente
import tkinter
import tkinter.ttk as ttk

class View:
    def __init__(self):
        self.util=Util()
        self.controller = ControladorPaciente()



    def cargar_paciente(self):
        pacientes = tkinter.Tk()
        pacientes.title("CARGAR PACIENTE")
        pacientes.geometry("800x500")

        def volver():
            pacientes.destroy()

        def cargar():
            def cerrar_exp():
                pacientes.destroy()
                #pacientes.eval('::ttk::CancelRepeat')
                self.cargar_paciente()

            try:

                nombre_pac = self.util.validar_cadena(str(nombre.get()), True)
                apellido_pac = self.util.validar_cadena(str(apellido.get()), True)
                cedula_pac = self.util.validar_entero(str(documento_identidad.get()), 1)
                telefono_pac = self.util.validar_cadena(str(telefono.get()), False)
                email_pac = self.util.validar_cadena(str(email.get()), False)
                fecha_pac = self.util.validar_fecha(str(fecha_nacimiento.get()))

                #contenedor = Medico(nombre, apellido, cedula, telefono, email, fecha, cargo, '')

                contenedor = Paciente(nombre_pac, apellido_pac, cedula_pac, telefono_pac, email_pac, fecha_pac, '')

                self.controller.cargar_paciente(contenedor)

            except Exception as e:
                alerta = tkinter.Message(pacientes, relief='raised',
                                         text='NO SE PUDO CARGAR EL PACIENTE\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
            else:
                alerta = tkinter.Message(pacientes, relief='raised', text='PACIENTE CARGADO CON EXITO', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(pacientes, font='Arial', text="DATOS DEL NUEVO PACIENTE")
        titulo.place(bordermode='outside', height=20, width=600, x=100)
        # Etiquetas
        lbl_nombre = tkinter.Label(pacientes, font='Arial', text="Nombres", justify='left')
        lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=30)
        lbl_apellido = tkinter.Label(pacientes, font='Arial', text="Apellidos")
        lbl_apellido.place(bordermode='outside', height=20, width=300, x=50, y=55)
        lbl_documento_identidad = tkinter.Label(pacientes, font='Arial', text="Documento de identidad")
        lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=80)
        lbl_telefono = tkinter.Label(pacientes, font='Arial', text="Télefono")
        lbl_telefono.place(bordermode='outside', height=20, width=300, x=50, y=105)
        lbl_email = tkinter.Label(pacientes, font='Arial', text="Email")
        lbl_email.place(bordermode='outside', height=20, width=300, x=50, y=130)
        lbl_fecha_nacimiento = tkinter.Label(pacientes, font='Arial', text="Fecha de Nacimiento")
        lbl_fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=50, y=155)

        # Campos de Texto
        nombre = tkinter.Entry(pacientes, font='times')
        nombre.place(bordermode='outside', height=20, width=300, x=350, y=30)
        apellido = tkinter.Entry(pacientes, font='times')
        apellido.place(bordermode='outside', height=20, width=300, x=350, y=55)
        documento_identidad = tkinter.Entry(pacientes, font='times')
        documento_identidad.place(bordermode='outside', height=20, width=300, x=350, y=80)
        telefono = tkinter.Entry(pacientes, font='times')
        telefono.place(bordermode='outside', height=20, width=300, x=350, y=105)
        email = tkinter.Entry(pacientes, font='times')
        email.place(bordermode='outside', height=20, width=300, x=350, y=130)
        fecha_nacimiento = tkinter.Entry(pacientes, font='times')
        fecha_nacimiento.place(bordermode='outside', height=20, width=300, x=350, y=155)


        cargar = tkinter.Button(pacientes, text="Cargar", command=cargar)
        cargar.place(bordermode='outside', height=40, width=100, x=240, y=210)
        volver = tkinter.Button(pacientes, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=340, y=210)
        pacientes.mainloop()


    def buscar_paciente(self):
        pacientes = tkinter.Tk()
        pacientes.title("BUSCAR PACIENTES")
        pacientes.geometry("800x500")

        def volver():
            pacientes.destroy()

        def buscar():

            def cerrar_exp():
                pacientes.destroy()
                #pacientes.eval('::ttk::CancelRepeat')
                self.buscar_paciente()

            dato = self.controller.buscar_paciente(self.util.validar_cadena(str(codigo.get()), True))

            if dato != None and len(dato) > 0:

                lbl_codigo = tkinter.Label(pacientes, font='Arial', text="Código", justify='left')
                lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=55)
                lbl_nombre = tkinter.Label(pacientes, font='Arial', text="Nombre Completo", justify='left')
                lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=80)
                lbl_documento_identidad = tkinter.Label(pacientes, font='Arial', text="Documento de identidad", justify='left')
                lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=105)
                lbl_orden = tkinter.Label(pacientes, font='Arial', text="Orden", justify='left')
                lbl_orden.place(bordermode='outside', height=20, width=300, x=50, y=130)

                codigo_result = tkinter.Label(pacientes, font='Arial', text=dato['codigo'], justify='left')
                codigo_result.place(bordermode='outside', height=20, width=300, x=350, y=55)
                nombre_result = tkinter.Label(pacientes, font='Arial', text=dato['nombrecompleto'], justify='left')
                nombre_result.place(bordermode='outside', height=20, width=300, x=350, y=80)
                documento_identidad_result = tkinter.Label(pacientes, font='Arial', text=dato['cedula'], justify='left')
                documento_identidad_result.place(bordermode='outside', height=20, width=300, x=350, y=105)
                orden_result = tkinter.Label(pacientes, font='Arial', text=dato['orden'], justify='left')
                orden_result.place(bordermode='outside', height=20, width=300, x=350, y=130)
            else:

                alerta = tkinter.Message(pacientes, relief='raised', text='Paciente no encontrado', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")



        titulo = tkinter.Label(pacientes, font='Arial', text="DATOS DEL PACIENTE")
        titulo.place(bordermode='outside', height=20, width=300, x=100)

        # Etiquetas
        lbl_codigo = tkinter.Label(pacientes, font='Arial', text="Código del Paciente", justify='left')
        lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=30)

        # Campos de Texto
        codigo = tkinter.Entry(pacientes, font='times')
        codigo.place(bordermode='outside', height=20, width=300, x=350, y=30)

        buscar = tkinter.Button(pacientes, text="Buscar", command=buscar)
        buscar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(pacientes, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        pacientes.mainloop()

    def listar_pacientes(self):
        def cerrar_exp():
            pacientes.destroy()
            #pacientes.eval('::ttk::CancelRepeat')
            self.cargar_paciente()

        pacientes = tkinter.Tk()
        pacientes.title("LISTADO DE PACIENTES")
        pacientes.geometry("1000x500")

        def volver():
            pacientes.destroy()

        mylistbox = tkinter.Listbox(pacientes, height=12, width=100, font=('times', 13))
        mylistbox.place(x=32, y=110)
        paciente = self.controller.listar_paciente()
        if paciente != None and len(paciente) != 0:
            for values in paciente:
                mylistbox.insert('end', '* Codigo: '+ values.codigof+ ', Nombre: '+ values.nombre+' '+values.apellido )
            titulo = tkinter.Label(pacientes, font='Arial', text="LISTADO DE PACIENTES")
            titulo.place(bordermode='outside', height=20, width=600, x=100, y=30)
            volver = tkinter.Button(pacientes, text="Volver", command=volver)
            volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
            pacientes.mainloop()
        else:
            alerta = tkinter.Message(pacientes, relief='raised',
                                     text='NO EXISTEN REGISTROS ' , width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

    def solicitar_datos_pac(self):
        print('-> Datos del nuevo Paciente')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        contenedor = Paciente(nombre,apellido,cedula,telefono,email,fecha,'','')
        return (contenedor)

    def solicitar_codigo_pac(self):
        print('-> Busqueda Paciente')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def busqueda_cedula_pac(self, orden):
        pacientes = tkinter.Tk()
        pacientes.title("BUSCAR PACIENTES")
        pacientes.geometry("800x500")

        def volver():
            pacientes.destroy()

        def buscar():
            def cerrar_exp():
                pacientes.destroy()
                # pacientes.eval('::ttk::CancelRepeat')
                #self.buscar_paciente()

            try:

                codigo = self.util.validar_entero(str(cedula.get()), 1)
                pacientes.destroy()
                orden.gestionar_orden(codigo)
                # return (codigo)

            except Exception as e:
                alerta = tkinter.Message(pacientes, relief='raised',
                                         text='NO SE PUDO REALIZAR LA BUSQUEDA\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(pacientes, font='Arial', text="DATOS DEL PACIENTE")
        titulo.place(bordermode='outside', height=20, width=300, x=100)

        # Etiquetas
        lbl_codigo = tkinter.Label(pacientes, font='Arial', text="Nro. de Cédula", justify='left')
        lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=30)

        # Campos de Texto
        cedula = tkinter.Entry(pacientes, font='times')
        cedula.place(bordermode='outside', height=20, width=300, x=350, y=30)

        buscar = tkinter.Button(pacientes, text="Buscar", command=buscar)
        buscar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(pacientes, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        pacientes.mainloop()


    def listar_pacientes_old(self, lista):
        if lista != None and len(lista) != 0:
            print('\n-> Listado de Pacientes: \n')
            for paciente in lista:
                print ('* Codigo: ', paciente.codigof, ', Nombre: ', paciente.nombre+' '+paciente.apellido, ', Cedula: ',paciente.cedula)
        else:
            print('\n-> No existen registros')
        self.util.pause()

    def mostrar_resultado_pac(self,dato):
        if(dato != None and len(dato)!=0):
            print('\n-> Paciente Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* orden: ',dato['orden']+'\n')
        else:
            print('\n-> Paciente no encontrado')
        self.util.pause()

    def mostrar_msg_pac(self,msg):
        print('\n',msg+'\n\n')


    def registrar_paciente_orden(self,orden, cedula):
        pacientes = tkinter.Tk()
        pacientes.title("CARGAR PACIENTE")
        pacientes.geometry("800x500")

        def volver():
            pacientes.destroy()

        def cargar():
            def cerrar_exp():
                pacientes.destroy()
                #pacientes.eval('::ttk::CancelRepeat')
                self.cargar_paciente()
            def ok_exp():
                pacientes.destroy()
                #pacientes.eval('::ttk::CancelRepeat')
                orden.gestionar_orden(cedula)

            try:

                nombre_pac = self.util.validar_cadena(str(nombre.get()), True)
                apellido_pac = self.util.validar_cadena(str(apellido.get()), True)
                cedula_pac = self.util.validar_entero(cedula, 1)
                telefono_pac = self.util.validar_cadena(str(telefono.get()), False)
                email_pac = self.util.validar_cadena(str(email.get()), False)
                fecha_pac = self.util.validar_fecha(str(fecha_nacimiento.get()))

                #contenedor = Medico(nombre, apellido, cedula, telefono, email, fecha, cargo, '')

                contenedor = Paciente(nombre_pac, apellido_pac, cedula_pac, telefono_pac, email_pac, fecha_pac, '')

                self.controller.cargar_paciente(contenedor)

            except Exception as e:
                alerta = tkinter.Message(pacientes, relief='raised',
                                         text='NO SE PUDO CARGAR EL PACIENTE\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
            else:
                alerta = tkinter.Message(pacientes, relief='raised', text='PACIENTE CARGADO CON EXITO', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=ok_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(pacientes, font='Arial', text="DATOS DEL NUEVO PACIENTE")
        titulo.place(bordermode='outside', height=20, width=600, x=100)
        # Etiquetas
        lbl_nombre = tkinter.Label(pacientes, font='Arial', text="Nombres", justify='left')
        lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=30)
        lbl_apellido = tkinter.Label(pacientes, font='Arial', text="Apellidos")
        lbl_apellido.place(bordermode='outside', height=20, width=300, x=50, y=55)
        lbl_documento_identidad = tkinter.Label(pacientes, font='Arial', text="Documento de identidad")
        lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=80)
        lbl_telefono = tkinter.Label(pacientes, font='Arial', text="Télefono")
        lbl_telefono.place(bordermode='outside', height=20, width=300, x=50, y=105)
        lbl_email = tkinter.Label(pacientes, font='Arial', text="Email")
        lbl_email.place(bordermode='outside', height=20, width=300, x=50, y=130)
        lbl_fecha_nacimiento = tkinter.Label(pacientes, font='Arial', text="Fecha de Nacimiento")
        lbl_fecha_nacimiento.place(bordermode='outside', height=20, width=300, x=50, y=155)

        # Campos de Texto
        nombre = tkinter.Entry(pacientes, font='times')
        nombre.place(bordermode='outside', height=20, width=300, x=350, y=30)
        apellido = tkinter.Entry(pacientes, font='times')
        apellido.place(bordermode='outside', height=20, width=300, x=350, y=55)

        documento_identidad_result = tkinter.Label(pacientes, font='Arial', text=cedula)
        documento_identidad_result.place(bordermode='outside', height=20, width=300, x=350, y=80)
        #documento_identidad = tkinter.Entry(pacientes, font='times')
        #documento_identidad.place(bordermode='outside', height=20, width=300, x=350, y=80)

        telefono = tkinter.Entry(pacientes, font='times')
        telefono.place(bordermode='outside', height=20, width=300, x=350, y=105)
        email = tkinter.Entry(pacientes, font='times')
        email.place(bordermode='outside', height=20, width=300, x=350, y=130)
        fecha_nacimiento = tkinter.Entry(pacientes, font='times')
        fecha_nacimiento.place(bordermode='outside', height=20, width=300, x=350, y=155)


        cargar = tkinter.Button(pacientes, text="Cargar", command=cargar)
        cargar.place(bordermode='outside', height=40, width=100, x=240, y=210)
        volver = tkinter.Button(pacientes, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=340, y=210)
        pacientes.mainloop()





