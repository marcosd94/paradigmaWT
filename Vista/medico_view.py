'''Vista para la carga de medicos'''
from Util.util import Util
from Modelo.medico_model import Medico
from Controlador.medico_controller import  ControladorMedico
import tkinter
import tkinter.ttk as ttk

class View:
    def __init__(self):
        self.util=Util()
        self.controller = ControladorMedico()

    def solicitar_datos_med(self):
        print('-> Datos del nuevo Medico')
        nombre = self.util.leer_cadena('Nombre: ',True)
        apellido = self.util.leer_cadena('Apellido: ',True)
        cedula = self.util.leer_entero('Cedula: ',1)
        telefono = self.util.leer_cadena('Telefono: ',False)
        email = self.util.leer_cadena('Email: ',False)
        fecha = self.util.leer_fecha('Fecha de Nacimiento dd/mm/yyyy: ')
        cargo = self.util.leer_cadena('Cargo: ',False)
        contenedor = Medico(nombre,apellido,cedula,telefono,email,fecha,cargo,'')
        return (contenedor)

    def cargar_medico(self):
        medicos = tkinter.Tk()
        medicos.title("CARGAR MÉDICO")
        medicos.geometry("800x500")

        def volver():
            medicos.destroy()

        def cargar():
            def cerrar_exp():
                medicos.destroy()
                #medicos.eval('::ttk::CancelRepeat')
                self.cargar_medico()

            try:

                nombre_med = self.util.validar_cadena(str(nombre.get()), True)
                apellido_med = self.util.validar_cadena(str(apellido.get()), True)
                cedula_med = self.util.validar_entero(str(documento_identidad.get()), 1)
                telefono_med = self.util.validar_cadena(str(telefono.get()), False)
                email_med = self.util.validar_cadena(str(email.get()), False)
                fecha_med = self.util.validar_fecha(str(fecha_nacimiento.get()))
                cargo_med = self.util.validar_cadena(str(cargo.get()), False)

                #contenedor = Medico(nombre, apellido, cedula, telefono, email, fecha, cargo, '')

                contenedor = Medico(nombre_med, apellido_med, cedula_med, telefono_med, email_med, fecha_med, cargo_med, '')

                self.controller.cargar_medico(contenedor)

            except Exception as e:
                alerta = tkinter.Message(medicos, relief='raised',
                                         text='NO SE PUDO CARGAR AL MÉDICO\nError: ' + str(e), width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")
            else:
                alerta = tkinter.Message(medicos, relief='raised', text='MÉDICO CARGADO CON EXITO', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")

        titulo = tkinter.Label(medicos, font='Arial', text="DATOS DEL NUEVO MÉDICO")
        titulo.place(bordermode='outside', height=20, width=600, x=100)
        # Etiquetas
        lbl_nombre = tkinter.Label(medicos, font='Arial', text="Nombres", justify='left')
        lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=30)
        lbl_apellido = tkinter.Label(medicos, font='Arial', text="Apellidos")
        lbl_apellido.place(bordermode='outside', height=20, width=300, x=50, y=55)
        lbl_documento_identidad = tkinter.Label(medicos, font='Arial', text="Documento de identidad")
        lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=80)
        lbl_telefono = tkinter.Label(medicos, font='Arial', text="Télefono")
        lbl_telefono.place(bordermode='outside', height=20, width=300, x=50, y=105)
        lbl_email = tkinter.Label(medicos, font='Arial', text="Email")
        lbl_email.place(bordermode='outside', height=20, width=300, x=50, y=130)
        lbl_fecha_nacimiento = tkinter.Label(medicos, font='Arial', text="Fecha de Nacimiento")
        lbl_fecha_nacimiento.place(bordermode='outside', height=20, width=200, x=50, y=155)
        lbl_cargo = tkinter.Label(medicos, font='Arial', text="Cargo")
        lbl_cargo.place(bordermode='outside', height=20, width=300, x=50, y=180)

        # Campos de Texto
        nombre = tkinter.Entry(medicos, font='times')
        nombre.place(bordermode='outside', height=20, width=300, x=350, y=30)
        apellido = tkinter.Entry(medicos, font='times')
        apellido.place(bordermode='outside', height=20, width=300, x=350, y=55)
        documento_identidad = tkinter.Entry(medicos, font='times')
        documento_identidad.place(bordermode='outside', height=20, width=300, x=350, y=80)
        telefono = tkinter.Entry(medicos, font='times')
        telefono.place(bordermode='outside', height=20, width=300, x=350, y=105)
        email = tkinter.Entry(medicos, font='times')
        email.place(bordermode='outside', height=20, width=300, x=350, y=130)
        fecha_nacimiento = tkinter.Entry(medicos, font='times')
        fecha_nacimiento.place(bordermode='outside', height=20, width=300, x=350, y=155)
        cargo = tkinter.Entry(medicos, font='times')
        cargo.place(bordermode='outside', height=20, width=300, x=350, y=180)


        cargar = tkinter.Button(medicos, text="Cargar", command=cargar)
        cargar.place(bordermode='outside', height=40, width=100, x=240, y=210)
        volver = tkinter.Button(medicos, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=340, y=210)
        medicos.mainloop()


    def buscar_medico(self):
        medicos = tkinter.Tk()
        medicos.title("BUSCAR MÉDICOS")
        medicos.geometry("800x500")

        def volver():
            medicos.destroy()

        def buscar():

            def cerrar_exp():
                medicos.destroy()
                #medicos.eval('::ttk::CancelRepeat')
                self.buscar_medico()

            dato = self.controller.buscar_medico(self.util.validar_cadena(str(codigo.get()), True))

            if dato != None and len(dato) > 0:

                lbl_codigo = tkinter.Label(medicos, font='Arial', text="Código", justify='left')
                lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=55)
                lbl_nombre = tkinter.Label(medicos, font='Arial', text="Nombre Completo", justify='left')
                lbl_nombre.place(bordermode='outside', height=20, width=300, x=50, y=80)
                lbl_documento_identidad = tkinter.Label(medicos, font='Arial', text="Documento de identidad", justify='left')
                lbl_documento_identidad.place(bordermode='outside', height=20, width=300, x=50, y=105)
                lbl_cargo = tkinter.Label(medicos, font='Arial', text="Cargo", justify='left')
                lbl_cargo.place(bordermode='outside', height=20, width=300, x=50, y=130)

                codigo_result = tkinter.Label(medicos, font='Arial', text=dato['codigo'], justify='left')
                codigo_result.place(bordermode='outside', height=20, width=300, x=350, y=55)
                nombre_result = tkinter.Label(medicos, font='Arial', text=dato['nombrecompleto'], justify='left')
                nombre_result.place(bordermode='outside', height=20, width=300, x=350, y=80)
                documento_identidad_result = tkinter.Label(medicos, font='Arial', text=dato['cedula'], justify='left')
                documento_identidad_result.place(bordermode='outside', height=20, width=300, x=350, y=105)
                cargo_result = tkinter.Label(medicos, font='Arial', text=dato['cargo'], justify='left')
                cargo_result.place(bordermode='outside', height=20, width=300, x=350, y=130)
            else:

                alerta = tkinter.Message(medicos, relief='raised', text='Médico no encontrado', width=200)
                alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
                ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
                ok.pack(side="bottom")



        titulo = tkinter.Label(medicos, font='Arial', text="DATOS DEL MÉDICO")
        titulo.place(bordermode='outside', height=20, width=300, x=100)

        # Etiquetas
        lbl_codigo = tkinter.Label(medicos, font='Arial', text="Código del Médico", justify='left')
        lbl_codigo.place(bordermode='outside', height=20, width=300, x=50, y=30)

        # Campos de Texto
        codigo = tkinter.Entry(medicos, font='times')
        codigo.place(bordermode='outside', height=20, width=300, x=350, y=30)

        buscar = tkinter.Button(medicos, text="Buscar", command=buscar)
        buscar.place(bordermode='outside', height=40, width=100, x=40, y=210)
        volver = tkinter.Button(medicos, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=140, y=210)
        medicos.mainloop()

    def listar_medicos(self):
        def cerrar_exp():
            medicos.destroy()
            #medicos.eval('::ttk::CancelRepeat')
            self.cargar_medico()

        medicos = tkinter.Tk()
        medicos.title("LISTADO DE MÉDICOS")
        medicos.geometry("1000x500")

        def volver():
            medicos.destroy()

        mylistbox = tkinter.Listbox(medicos, height=12, width=100, font=('times', 13))
        mylistbox.place(x=32, y=110)
        medico = self.controller.listar_medico()
        if medico != None and len(medico) != 0:
            for values in medico:
                mylistbox.insert('end', '* Codigo: '+ values.codigof+ ', Nombre: '+ values.nombre+' '+values.apellido+ ', Cargo: '+values.cargo )
            titulo = tkinter.Label(medicos, font='Arial', text="LISTADO DE MÉDICOS")
            titulo.place(bordermode='outside', height=20, width=600, x=100, y=30)
            volver = tkinter.Button(medicos, text="Volver", command=volver)
            volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
            medicos.mainloop()
        else:
            alerta = tkinter.Message(medicos, relief='raised',
                                     text='NO EXISTEN REGISTROS ' , width=200)
            alerta.place(bordermode='outside', height=150, width=200, y=30, x=150)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")


#####METODOS A ELIMINAR


    def solicitar_codigo_med(self):
        print('-> Busqueda Medico')
        codigo = self.util.leer_cadena('Codigo: ',True)
        codigo = codigo.upper()
        return (codigo)

    def mostrar_resultado_med(self,dato):
        if(dato != None and len(dato)!=0):
            print('\n-> Medico Buscado Codigo: ',dato['codigo'])
            print('* Nombre Completo: ',dato['nombrecompleto'])
            print('* Cedula: ',dato['cedula'])
            print('* cargo: ',dato['cargo']+'\n')
        else:
            print('\n-> Paciente no encontrado')
        self.util.pause()

    def mostrar_msg_med(self,msg):
        print('\n',msg+'\n\n')




