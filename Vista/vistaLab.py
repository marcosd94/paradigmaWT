from Util.util import Util
from Controlador.funcionario_controller import ControladorFuncionario
from Controlador.paciente_controller import  ControladorPaciente
from Controlador.medico_controller import  ControladorMedico
from Controlador.orden_controller import OrdenController
from Controlador.jornada_controller import JornadaController

class VistaLab:
    def __init__(self):
        self.util = Util()
        self.x = ControladorFuncionario()
        self.p = ControladorPaciente()
        self.m = ControladorMedico()
        self.con = OrdenController()
        self.jornada = JornadaController()
        self.promtp = '~golab >>> '




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


        if ( tur != 0):
            print('-> Jornada:', self.jornada.numero, '\t ->', ver, '\t-> Ultima conexion: ', self.jornada.ultima_fecha)
            print('\t\tGOLAB Laboratorio de Analisis Clinicos\n')
            while (bucle):
                print('\t\t*** Elija una opcion ***')
                print('1- Agregar')
                print('2- Listar')
                print('3- Buscar')
                print('4- Atender')
                print('4- Salir')
                valor = self.util.verificar_espacios(input(self.promtp)).strip(',.-_')
                if (valor == '1' or valor == 'Agregar' or valor == 'agregar'):
                    self.agregar_vista()
                elif (valor == '2' or valor == 'Listar' or valor == 'listar'):
                    self.listar_vista()
                elif (valor == '3' or valor == 'Buscar' or valor == 'buscar'):
                    self.buscar_vista()
                elif (valor == '4' or valor == 'Atender' or valor == 'atender'):
                    self.atender_vista()
                elif (valor == '5' or valor == 'Salir' or valor == 'salir'):
                    bucle = False
                elif (valor == ''):
                    continue
                else:
                    print('El comando ingresado no es Valido')
                    valor = ''

            else:
                print('Hasta pronto!')
        else:
            print('\t\tGOLAB se encuentra cerrado\n')

    def agregar_vista(self):
        valor = ''
        loop = True

        while (loop):
            print('\t\t*** Agregar ***')
            print('1- Funcionario')
            print('2- Medico')
            print('3- Paciente')
            print('4- Orden de Analisis')
            print('5- Volver')
            valor = self.util.verificar_espacios(input(self.promtp)).strip(',.-_')
            try:
                if (valor == '1' or valor == 'Funcionario' or valor == 'funcionario'):
                    self.x.cargar_func()
                    pass
                elif (valor == '2' or valor == 'Medico' or valor == 'medico'):
                    self.m.cargar_medico()
                elif (valor == '3' or valor == 'Paciente' or valor == 'paciente'):
                    self.p.cargar_paciente()
                elif (valor == '4' or valor == 'Orden' or valor == 'orden'):
                    self.con.cargar_orden()
                elif (valor == '5' or valor == 'Volver' or valor == 'volver'):
                    loop = False
                elif (valor == ''):
                    continue
                else:
                    print('El comando ingresado no es Valido')
            except Exception as e:
                print('Ocurrio un error con el servicio solicitado\n', e)
            except KeyboardInterrupt as ex:
                print('Te dije nde bobo',ex)

    def listar_vista(self):
        valor = ''
        loop = True
        while (loop):
            print('\t\t*** Listar ***')
            print('1- Funcionario')
            print('2- Medico')
            print('3- Paciente')
            print('4- Ordenes')
            print('5- Volver')
            valor = self.util.verificar_espacios(input(self.promtp)).strip(',.-_')
            try:

                if (valor == '1' or valor == 'Funcionario' or valor == 'funcionario'):
                    self.x.listar_funcionarios()
                elif (valor == '2' or valor == 'Medico' or valor == 'medico'):
                    self.m.listar_medico()
                elif (valor == '3' or valor == 'Paciente' or valor == 'paciente'):
                    self.p.listar_paciente()
                elif (valor == '4' or valor == 'Ordenes' or valor == 'ordenes'):
                    self.con.listar_orden()
                elif (valor == '5' or valor == 'Volver' or valor == 'volver'):
                    loop = False
                elif (valor == ''):
                    continue
                else:
                    print('El comando ingresado no es Valido')
            except Exception as e:
                print('Ocurrio un error con el servicio solicitado\n', e)

    def buscar_vista(self):
        valor = ''
        loop = True

        while (loop):
            print('\t\t*** Buscar ***')
            print('1- Funcionario')
            print('2- Medico')
            print('3- Paciente')
            print('4- Ordenes')
            print('5- Volver')
            valor = self.util.verificar_espacios(input(self.promtp)).strip(',.-_')
            try:
                if (valor == '1' or valor == 'Funcionario' or valor == 'funcionario'):
                    self.x.buscar_funcionarios()
                elif (valor == '2' or valor == 'Medico' or valor == 'medico'):
                    self.m.buscar_medico()
                elif (valor == '3' or valor == 'Paciente' or valor == 'paciente'):
                    self.p.buscar_paciente()
                elif (valor == '4' or valor == 'Ordenes' or valor == 'ordenes'):
                    self.con.buscar_orden()
                elif (valor == '5' or valor == 'Volver' or valor == 'volver'):
                    loop = False
                elif (valor == ''):
                    continue
                else:
                    print('El comando ingresado no es Valido')
            except Exception as e:
                print('Ocurrio un error con el servicio solicitado\n', e)


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
