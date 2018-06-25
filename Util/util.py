from os import system, name
from time import strptime


class Util:
    def limpiar_pantalla(self):
        system('cls' if name == 'nt' else 'clear')

    def genera_codigo(self, nombre, apellido, cedula):
        try:
            codigo = nombre[0:1].upper() + apellido[0:1].upper() + str(cedula)
        except:
            print('Error al capturar los datos')
        return codigo

    def leer_entero(self, msg, min_value=None, max_value=None, default=None):
        ''' (string, int, int) -> int
        Pide que se ingrese número. Solo se retorna resultado cuando se ingresa
        un valor válido.
        @Parámetros
            msg : mensaje que se muestra al usuario.
            min_value: el valor mínimo que usuario debe ingresar
            max_value: el valor máximo que usuario debe ingresar
        Ej:
            leer_numero('Ingrese un número entre 1 y 9', 1, 9)
        '''
        while (True):
            cualquier_valor = input(msg)
            try:
                # tratamos de convertir en número entero
                number = int(cualquier_valor)

                if min_value and (number < min_value):
                    error_msg = "Número fuera de rango [min_value = {}]".format(str(min_value))
                    raise ValueError(error_msg)

                if max_value and (number > max_value):
                    error_msg = "Número fuera de rango [max_value = {}]".format(str(max_value))
                    raise ValueError(error_msg)

                # se retorna valor válido ingresado por el usuario
                return number
            except ValueError as ve:
                # print (ve)
                print("Se esperaba número!")
            except TypeError as te:
                print("Se esperaba número!")
            except Exception as e:
                print(e)

    def leer_cadena(self, msg, obligatorio, default=None):
        while (True):
            if default:
                msg = msg + default + chr(8) * len(default)

            data = input(msg)
            data = data or default
            try:
                if obligatorio and data == None:
                    raise Exception("Debe ingresar valor!")
                elif (len(data.strip()) == 0):
                    raise Exception("Debe ingresar valor!")
                # se retorna valor válido ingresado por el usuario
                return data
            except Exception as e:
                print('Debe ingresar valor!')

    def leer_fecha(self, msg):
        while (True):
            data = input(msg)
            try:
                strptime(data, '%d/%m/%Y')
                return data
            except Exception as e:
                print('El formato no corresponde')

    def pause(self):
        key = input("\nPresione enter para continuar...\n\n")


    def verificar_espacios(self,valor):
        resultado = ''
        if valor!= None and len(valor)!=0:
            temporal = []
            for char in valor:
                if char!=" ":
                    temporal += char
            resultado = ''.join(temporal)
        return resultado

    def validar_fecha(self, fecha):
        try:
            strptime(fecha, '%d/%m/%Y')
            return fecha
        except Exception as e:
            raise Exception('El formato no corresponde')

    def validar_entero(self, valor, min_value=None, max_value=None, default=None):
        ''' (string, int, int) -> int
        Pide que se ingrese número. Solo se retorna resultado cuando se ingresa
        un valor válido.
        @Parámetros
            msg : mensaje que se muestra al usuario.
            min_value: el valor mínimo que usuario debe ingresar
            max_value: el valor máximo que usuario debe ingresar
        Ej:
            leer_numero('Ingrese un número entre 1 y 9', 1, 9)
        '''
        while (True):
            cualquier_valor = valor
            try:
                # tratamos de convertir en número entero
                number = int(cualquier_valor)

                if min_value and (number < min_value):
                    error_msg = "Número fuera de rango [min_value = {}]".format(str(min_value))
                    raise ValueError(error_msg)

                if max_value and (number > max_value):
                    error_msg = "Número fuera de rango [max_value = {}]".format(str(max_value))
                    raise ValueError(error_msg)

                # se retorna valor válido ingresado por el usuario
                return number
            except ValueError as ve:
                # print (ve)
                raise Exception("Se esperaba número!")
            except TypeError as te:
                raise Exception("Se esperaba número!")
            except Exception as e:
                raise Exception(e)

    def validar_cadena(self, valor, obligatorio, default=None):
        while (True):
            if default:
                msg = msg + default + chr(8) * len(default)

            data = valor
            data = data or default
            try:
                if obligatorio and data == None:
                    raise Exception("Debe ingresar valor!")
                elif (len(data.strip()) == 0):
                    raise Exception("Debe ingresar valor!")
                # se retorna valor válido ingresado por el usuario
                return data
            except Exception as e:
                raise Exception('Debe ingresar valor!')