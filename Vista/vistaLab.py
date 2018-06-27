from Util.util import Util
from Controlador.funcionario_controller import ControladorFuncionario
from Controlador.paciente_controller import  ControladorPaciente
from Controlador.medico_controller import  ControladorMedico
from Controlador.orden_controller import OrdenController
from Controlador.jornada_controller import JornadaController
from Vista.funcionario_view import View as FuncionarioView
from Vista.medico_view import View as MedicoView
from Vista.paciente_view import View as PacienteView
from Vista.orden_view import OrdenPaciente
import tkinter
class VistaLab:
    def __init__(self):
        self.util = Util()
        self.x = ControladorFuncionario()
        self.p = ControladorPaciente()
        self.m = ControladorMedico()
        self.con = OrdenController()
        self.jornada = JornadaController()
        self.promtp = '~golab >>> '
        self.funcionario_view = FuncionarioView()
        self.medico_view = MedicoView()
        self.paciente_view = PacienteView()
        self.orden_view = OrdenPaciente()


    def main_loop(self):
        '''Menu principal de la aplicacion'''

        bucle = True
        valor = ''
        tur = self.jornada.periodo
        ver = ''
        if(tur ==1):
            ver = 'Primer Turno'
        elif(tur == 2):
            ver = 'Segundo Turno'
        else:
            ver = 'Cerrado'


        #BOTONES DE LA VISTA
        def salir():
            ventana.destroy()

        def CurSelet(evt):
            value = str(mylistbox.get(mylistbox.curselection()))
            if (value == 'Agregar'):
                ventana.destroy()
                self.agregar_vista()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Listar'):
                ventana.destroy()
                self.listar_vista()
                #view_funcionarios.listar_funcionarios(usu)
            elif (value == 'Buscar'):
                ventana.destroy()
                self.buscar_vista()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Atender'):
                #ventana.destroy()
                self.atender_vista()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Salir'):
                ventana.destroy()
                bucle = False
                #view_articulos.cargar_articulos(usu)

        if ( tur != 0):
        #if ( False ):

            ventana = tkinter.Tk()
            ventana.title("GOLAB - Laboratorio de Analisis Clinicos")
            ventana.geometry("700x700")
            L1 = tkinter.Label(ventana, font='Arial', text="GOLAB - Laboratorio de Analisis Clinicos")
            L1.place(bordermode='outside', height=30, x=50, y=10)

            #print('-> Jornada:', self.jornada.numero, '\t ->', ver, '\t-> Ultima conexion: ', self.jornada.ultima_fecha)
            dato = '* Jornada: '+ str(self.jornada.numero) + '\t*' + ver + '\t* Ultima conexion: '+ self.jornada.ultima_fecha
            datos = tkinter.Label(ventana, font='Arial', text=dato)
            datos.place(bordermode='outside', height=20, x=50, y=40)

            L2 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
            L2.place(bordermode='outside', height=30, x=50, y=80)

            itemsforlistbox = ['Agregar',
                               'Listar',
                               'Buscar',
                               'Atender']


            mylistbox = tkinter.Listbox(ventana, height=12, font=('times', 13))
            mylistbox.bind('<<ListboxSelect>>', CurSelet)
            mylistbox.place(x=45, y=110)

            for items in itemsforlistbox:
                mylistbox.insert('end', items)

            #cerrar = tkinter.Button(ventana, text="Cerrar Sesión", command=cerrar)
            #cerrar.place(bordermode='outside', height=40, width=100, x=40, y=400)
            salir = tkinter.Button(ventana, text="Salir", command=salir)
            salir.place(bordermode='outside', height=40, width=100, x=140, y=400)

            ventana.mainloop()
        else:

            def cerrar_exp():
                ordenes.destroy()
                #funcionarios.eval('::ttk::CancelRepeat')

            ordenes = tkinter.Tk()
            ordenes.title("GOLAB - Laboratorio de Analisis Clinicos")
            ordenes.geometry("500x300")
            alerta = tkinter.Message(ordenes, relief='raised', text="GOLAB se encuentra cerrado", width=200)
            alerta.place(bordermode='outside', height=250, width=400, y=30, x=50)
            ok = tkinter.Button(alerta, text="Ok", command=cerrar_exp)
            ok.pack(side="bottom")

            ordenes.mainloop()



    def agregar_vista(self):
        valor = ''
        loop = True

        def salir():
            agregar.destroy()

        def volver():
            agregar.destroy()
            self.main_loop()

        def CurSelet(evt):
            value = str(mylistbox.get(mylistbox.curselection()))
            if (value == 'Funcionario'):
                #agregar.destroy()
                self.funcionario_view.cargar_funcionario()
                #self.x.mostrar_formulario_funcionario()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                #agregar.destroy()
                self.medico_view.cargar_medico()
                #view_funcionarios.listar_funcionarios(usu)
            elif (value == 'Paciente'):
                #agregar.destroy()
                self.paciente_view.cargar_paciente()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis'):
                #agregar.destroy()
                self.orden_view.registrar_orden()
                #self.con.cargar_orden()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                agregar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        agregar = tkinter.Tk()
        agregar.title("Agregar")
        agregar.geometry("700x700")
        L1 = tkinter.Label(agregar, font='Arial', text="ELIJA EL ITEM PARA AGREGAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis']

        mylistbox = tkinter.Listbox(agregar, height=12, width=50, font=('times', 13))
        mylistbox.bind('<<ListboxSelect>>', CurSelet)
        mylistbox.place(x=45, y=110)

        for items in itemsforlistbox:
            mylistbox.insert('end', items)

        volver = tkinter.Button(agregar, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
        salir = tkinter.Button(agregar, text="Salir", command=salir)
        salir.place(bordermode='outside', height=40, width=100, x=140, y=400)

        agregar.mainloop()




    def listar_vista(self):
        valor = ''
        loop = True

        def salir():
            listar.destroy()

        def volver():
            listar.destroy()
            self.main_loop()

        def CurSelet(evt):
            value = str(mylistbox.get(mylistbox.curselection()))
            if (value == 'Funcionario'):
                #listar.destroy()
                self.funcionario_view.listar_funcionarios()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                #listar.destroy()
                self.medico_view.listar_medicos()
                #view_funcionarios.listar_funcionarios(usu)
            elif (value == 'Paciente'):
                #listar.destroy()
                self.paciente_view.listar_pacientes()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis Pendientes'):
                #listar.destroy()
                self.orden_view.listar_ordenes_pendientes()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Orden de Analisis Finalizados'):
                #listar.destroy()
                self.orden_view.listar_ordenes_finalizadas()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                listar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        listar = tkinter.Tk()
        listar.title("Listar")
        listar.geometry("700x700")
        L1 = tkinter.Label(listar, font='Arial', text="ELIJA EL ITEM A LISTAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis Pendientes',
                           'Orden de Analisis Finalizados']

        mylistbox = tkinter.Listbox(listar, height=12, width=50, font=('times', 13))
        mylistbox.bind('<<ListboxSelect>>', CurSelet)
        mylistbox.place(x=45, y=110)

        for items in itemsforlistbox:
            mylistbox.insert('end', items)

        volver = tkinter.Button(listar, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
        salir = tkinter.Button(listar, text="Salir", command=salir)
        salir.place(bordermode='outside', height=40, width=100, x=140, y=400)

        listar.mainloop()

    def buscar_vista(self):
        valor = ''
        loop = True


        def salir():
            buscar.destroy()

        def volver():
            buscar.destroy()
            self.main_loop()

        def CurSelet(evt):
            value = str(mylistbox.get(mylistbox.curselection()))
            if (value == 'Funcionario'):
                #buscar.destroy()
                self.funcionario_view.solicitar_codigo()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                #buscar.destroy()
                self.medico_view.buscar_medico()
                #self.m.buscar_medico()
                #view_funcionarios.buscar_funcionarios(usu)
            elif (value == 'Paciente'):
                #buscar.destroy()
                self.paciente_view.buscar_paciente()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis'):
                #buscar.destroy()
                self.orden_view.buscar_orden()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                buscar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        buscar = tkinter.Tk()
        buscar.title("Buscar")
        buscar.geometry("700x700")
        L1 = tkinter.Label(buscar, font='Arial', text="ELIJA EL ITEM A BUSCAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis']

        mylistbox = tkinter.Listbox(buscar, height=12, width=50, font=('times', 13))
        mylistbox.bind('<<ListboxSelect>>', CurSelet)
        mylistbox.place(x=45, y=110)

        for items in itemsforlistbox:
            mylistbox.insert('end', items)

        volver = tkinter.Button(buscar, text="Volver", command=volver)
        volver.place(bordermode='outside', height=40, width=100, x=40, y=400)
        salir = tkinter.Button(buscar, text="Salir", command=salir)
        salir.place(bordermode='outside', height=40, width=100, x=140, y=400)

        buscar.mainloop()

    def atender_vista(self):
        self.orden_view.atender_orden()

