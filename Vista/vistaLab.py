from Util.util import Util
from Controlador.funcionario_controller import ControladorFuncionario
from Controlador.paciente_controller import  ControladorPaciente
from Controlador.medico_controller import  ControladorMedico
from Controlador.orden_controller import OrdenController
from Controlador.jornada_controller import JornadaController
from Vista.funcionario_view import View as FuncionarioView
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

        def cerrar():
            ventana.destroy()
            login.inicio()

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
                ventana.destroy()
                self.atender_vista()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Salir'):
                ventana.destroy()
                bucle = False
                #view_articulos.cargar_articulos(usu)

        if ( tur != 0):

            ventana = tkinter.Tk()
            ventana.title("GOLAB Laboratorio de Analisis Clinicos")
            ventana.geometry("500x500")
            L1 = tkinter.Label(ventana, font='Arial', text="POR FAVOR ELIJA LA TAREA A REALIZAR")
            L1.place(bordermode='outside', height=50, x=100, y=10)

            itemsforlistbox = ['Agregar',
                               'Listar',
                               'Buscar',
                               'Atender',
                               'Salir']


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
            print('\t\tGOLAB se encuentra cerrado\n')





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
                agregar.destroy()
                self.funcionario_view.cargar_funcionario()
                #self.x.mostrar_formulario_funcionario()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                agregar.destroy()
                self.m.cargar_medico()
                #view_funcionarios.listar_funcionarios(usu)
            elif (value == 'Paciente'):
                agregar.destroy()
                self.p.cargar_paciente()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis'):
                agregar.destroy()
                self.con.cargar_orden()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                agregar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        agregar = tkinter.Tk()
        agregar.title("Agregar")
        agregar.geometry("500x500")
        L1 = tkinter.Label(agregar, font='Arial', text="ELIJA EL ITEM PARA AGREGAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis',
                           'Volver']

        mylistbox = tkinter.Listbox(agregar, height=12, font=('times', 13))
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
                listar.destroy()
                self.funcionario_view.listar_funcionarios()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                listar.destroy()
                self.m.listar_medico()
                #view_funcionarios.listar_funcionarios(usu)
            elif (value == 'Paciente'):
                listar.destroy()
                self.p.listar_paciente()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis'):
                listar.destroy()
                self.con.listar_orden()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                listar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        listar = tkinter.Tk()
        listar.title("Listar")
        listar.geometry("500x500")
        L1 = tkinter.Label(listar, font='Arial', text="ELIJA EL ITEM PARA AGREGAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis',
                           'Volver']

        mylistbox = tkinter.Listbox(listar, height=12, font=('times', 13))
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
                buscar.destroy()
                self.funcionario_view.solicitar_codigo()
                #view_funcionarios.cargar_funcionario(usu)
            elif (value == 'Medico'):
                buscar.destroy()
                self.m.buscar_medico()
                #view_funcionarios.buscar_funcionarios(usu)
            elif (value == 'Paciente'):
                buscar.destroy()
                self.p.buscar_paciente()
                #view_funcionarios.eliminar_funcionario(usu)
            elif (value == 'Orden de Analisis'):
                buscar.destroy()
                self.con.buscar_orden()
                #view_articulos.cargar_articulos(usu)
            elif (value == 'Volver'):
                buscar.destroy()
                self.main_loop()
                #bucle = False
                #view_articulos.cargar_articulos(usu)

        buscar = tkinter.Tk()
        buscar.title("Listar")
        buscar.geometry("500x500")
        L1 = tkinter.Label(buscar, font='Arial', text="ELIJA EL ITEM PARA AGREGAR")
        L1.place(bordermode='outside', height=50, x=100, y=10)

        itemsforlistbox = ['Funcionario',
                           'Medico',
                           'Paciente',
                           'Orden de Analisis',
                           'Volver']

        mylistbox = tkinter.Listbox(buscar, height=12, font=('times', 13))
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
        valor = ''
        loop = True
        while(loop):
            print('\t\t*** Atencion Ordenes ***')
            print('1- Cargar Resultados')
            print('2- Volver')
            valor = self.util.verificar_espacios(input(self.promtp)).strip(',.-_')
            try:
                if(valor == '1' or valor == 'Cargar' or valor == 'cargar'):
                    self.con.atender_orden()
                elif(valor == '2' or valor == 'Volver' or valor == 'volver'):
                    loop = False
                elif(valor == ''):
                    continue
                else:
                    print('El comando ingresado no es Valido')
            except Exception as e:
                print('Ocurrio un error con el servicio solicitado\n',e)