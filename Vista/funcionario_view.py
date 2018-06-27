'''Vista para la carga de funcionarios'''
from Util.util import Util
from Modelo.funcionario_model import Funcionario
from Modelo.funcionario_model import Funcionario
from Controlador.funcionario_controller import ControladorFuncionario
import tkinter
import tkinter.ttk as ttk
#from Vista.vistaLab import VistaLab

class View:
    def __init__(self):
        self.util=Util()
        self.controller = ControladorFuncionario()

    def solicitar_datos(self):
        print('-> Datos del nuevo Funcionario')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        cargo = self.util.leer_cadena('Cargo: ',False)


        contenedor = Funcionario(nombre,apellido,cedula,telefono,email,fecha,cargo,'')
        return (contenedor)

    def cargar_funcionario(self):
        funcionarios = tkinter.Tk()
        funcionarios.title("CARGAR FUNCIONARIOS")
        funcionarios.geometry("800x500")

        def volver():
            funcionarios.destroy()

        def cargar():
            def cerrar_exp():
                funcionarios.destroy()
                #funcionarios.eval('::ttk::CancelRepeat')
                self.cargar_funcionario()

            try:

                nombre_fun = self.util.validar_cadena(str(nombre.get()), True)
                apellido_fun = self.util.validar_cadena( str(apellido.get()), True)
                cedula_fun = self.util.validar_entero(str(documento_identidad.get()), 1)
                telefono_fun = self.util.validar_cadena( str(telefono.get()), False)
                email_fun = self.util.validar_cadena( str(email.get()), False)
                fecha_fun = self.util.validar_fecha( str(fecha_nacimiento.get()))
                cargo_fun = self.util.validar_cadena( str(cargo.get()), False)

                contenedor = Funcionario(nombre_fun, apellido_fun, cedula_fun, telefono_fun, email_fun, fecha_fun, cargo_fun, '')

                self.controller.cargar_func(contenedor)

            except Exception as e:
                alerta = tkinter.Message(funcionarios, relief='raised',
                                         text='NO SE PUDO CARGAR AL FUNCIONARIO\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
            else:
                alerta = tkinter.Message(funcionarios, relief='raised', text='FUNCIONARIO CARGADO CON EXITO', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(funcionarios, font='Arial', text="DATOS DEL NUEVO FUNCIONARIO")
        titulo.place(bordermode='outside', height=20, width=300, x=100)
        # Etiquetas
        lbl_nombre = tkinter.Label(funcionarios, font='Arial', text="Nombres", justify='left')
        lbl_nombre.place(bordermode='outside', height=20, width=200, x=50, y=30)
        lbl_apellido = tkinter.Label(funcionarios, font='Arial', text="Apellidos")
        lbl_apellido.place(bordermode='outside', height=20, width=200, x=50, y=55)
        lbl_documento_identidad = tkinter.Label(funcionarios, font='Arial', text="Documento de identidad")
        lbl_documento_identidad.place(bordermode='outside', height=20, width=200, x=50, y=80)
        lbl_telefono = tkinter.Label(funcionarios, font='Arial', text="Télefono")
        lbl_telefono.place(bordermode='outside', height=20, width=200, x=50, y=105)
        lbl_email = tkinter.Label(funcionarios, font='Arial', text="Email")
        lbl_email.place(bordermode='outside', height=20, width=200, x=50, y=130)
        lbl_fecha_nacimiento = tkinter.Label(funcionarios, font='Arial', text="Fecha de Nacimiento")
        lbl_fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=50, y=155)
        lbl_cargo = tkinter.Label(funcionarios, font='Arial', text="Cargo")
        lbl_cargo.place(bordermode='outside', height=20, width=200, x=50, y=180)

        # Campos de Texto
        nombre = tkinter.Entry(funcionarios, font='times')
        nombre.place(bordermode='outside', height=20, width=200, x=250, y=30)
        apellido = tkinter.Entry(funcionarios, font='times')
        apellido.place(bordermode='outside', height=20, width=200, x=250, y=55)
        documento_identidad = tkinter.Entry(funcionarios, font='times')
        documento_identidad.place(bordermode='outside', height=20, width=200, x=250, y=80)
        telefono = tkinter.Entry(funcionarios, font='times')
        telefono.place(bordermode='outside', height=20, width=200, x=250, y=105)
        email = tkinter.Entry(funcionarios, font='times')
        email.place(bordermode='outside', height=20, width=200, x=250, y=130)
        fecha_nacimiento = tkinter.Entry(funcionarios, font='times')
        fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=250, y=155)
        cargo = tkinter.Entry(funcionarios, font='times')
        cargo.place(bordermode='outside', height=20, width=200, x=250, y=180)


        cargar = tkinter.Button(funcionarios, text="Cargar", command=cargar)
        cargar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(funcionarios, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        funcionarios.mainloop()

    def solicitar_codigo(self):

        funcionarios = tkinter.Tk()
        funcionarios.title("BUSCAR FUNCIONARIOS")
        funcionarios.geometry("800x500")

        def volver():
            funcionarios.destroy()

        def buscar():

            def cerrar_exp():
                funcionarios.destroy()
                #funcionarios.eval('::ttk::CancelRepeat')
                self.solicitar_codigo()

            dato = self.controller.buscar_funcionarios(self.util.validar_cadena(str(codigo.get()), True))

            if dato != None and len(dato) > 0:

                lbl_codigo = tkinter.Label(funcionarios, font='Arial', text="Código", justify='left')
                lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=55)
                lbl_nombre = tkinter.Label(funcionarios, font='Arial', text="Nombre Completo", justify='left')
                lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=80)
                lbl_documento_identidad = tkinter.Label(funcionarios, font='Arial', text="Documento de identidad", justify='left')
                lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=105)
                lbl_cargo = tkinter.Label(funcionarios, font='Arial', text="Cargo", justify='left')
                lbl_cargo.place(bordermode='outside', height=20, width=300, x=50, y=130)

                codigo_result = tkinter.Label(funcionarios, font='Arial', text=dato['codigo'], justify='left')
                codigo_result.place(bordermode='outside', height=20, width=300, x=350, y=55)
                nombre_result = tkinter.Label(funcionarios, font='Arial', text=dato['nombrecompleto'], justify='left')
                nombre_result.place(bordermode='outside', height=20, width=300, x=350, y=80)
                documento_identidad_result = tkinter.Label(funcionarios, font='Arial', text=dato['cedula'], justify='left')
                documento_identidad_result.place(bordermode='outside', height=20, width=300, x=350, y=105)
                cargo_result = tkinter.Label(funcionarios, font='Arial', text=dato['cargo'], justify='left')
                cargo_result.place(bordermode='outside', height=20, width=300, x=350, y=130)
            else:

                alerta = tkinter.Message(funcionarios, relief='raised', text='Funcionario no encontrado', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")



        titulo = tkinter.Label(funcionarios, font='Arial', text="DATOS FUNCIONARIO")
        titulo.place(bordermode='outside', height=20, width=300, x=100)

        # Etiquetas
        lbl_codigo = tkinter.Label(funcionarios, font='Arial', text="Código del Funcionario", justify='left')
        lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=30)

        # Campos de Texto
        codigo = tkinter.Entry(funcionarios, font='times')
        codigo.place(bordermode='outside', height=20, width=300, x=350, y=30)

        buscar = tkinter.Button(funcionarios, text="Buscar", command=buscar)
        buscar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(funcionarios, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        funcionarios.mainloop()

    def listar_funcionarios(self):
        def cerrar_exp():
            funcionarios.destroy()
            #funcionarios.eval('::ttk::CancelRepeat')
            self.cargar_funcionario()

        funcionarios = tkinter.Tk()
        funcionarios.title("LISTADO DE FUNCIONARIOS")
        funcionarios.geometry("1000x500")

        def volver():
            funcionarios.destroy()

        mylistbox = tkinter.Listbox(funcionarios, height=12, width=100, font=('times', 13))
        mylistbox.place(x=32, y=110)
        fun = self.controller.listar_funcionarios()
        if fun != None and len(fun) != 0:
            for values in fun:
                mylistbox.insert('end', '* Codigo: '+ values.codigof+ ', Nombre: '+ values.nombre+' '+values.apellido+ ', Cargo: '+values.cargo )
            titulo = tkinter.Label(funcionarios, font='Arial', text="LISTADO DE FUNCIONARIOS")
            titulo.place(bordermode='outside', height=20, width=600, x=100, y=30)
            volver = tkinter.Button(funcionarios, text="Volver", command=volver)
            volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
            funcionarios.mainloop()


            #print('\n-> Listado de Funcionarios en la base de datos: \n')
            #for funcionario in lista:
            #    print ('* Codigo: ', funcionario.codigof, ', Nombre: ', funcionario.nombre+' '+funcionario.apellido, ', Cargo: ',funcionario.cargo)
            #self.util.pause()
        else:
            alerta = tkinter.Message(funcionarios, relief='raised',
                                     text='NO EXISTEN REGISTROS ' , width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

    def mostrar_resultado(self,dato):
        if dato != None and len(dato)>0:
            print('\n-> Funcionario Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* Cargo: ',dato['cargo']+'\n')
        else:
            print('\n-> Funcionario no encontrado')
        self.util.pause()

    def mostrar_msg(self,msg):
        print('\n',msg+'\n\n')




