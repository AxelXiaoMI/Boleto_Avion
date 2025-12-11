import subprocess
import sys

#Paso 1 Verificacion de que la libreria psycopg2 este instalada
def ticket_avion():
    step = 1
    if step == 1:
        try:
            import psycopg2
        except ImportError:
            print("Las Librerias Necesarias no estan Instaladas, se instalaran a continuacion")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2"])
            print("Instalación completa.")
            print('\n' * 5)
            import psycopg2
            
        finally:
            print('-' * 100)
            print('Paso Numero 1 Completado (Instalacion de las librearias necesarias)')
            print('-' * 100)
            step = 2
            #Datos para conectarse a la base de datos
            try:
                connection = psycopg2.connect(
                    host = '127.0.0.1',
                    port = 5432,
                    user = 'prueba',
                    password = '1234',
                    database = 'ticket_avion_v1'
                )
            except Exception as ex:
                print(ex)

    while True:
        #Paso 2 Eleccion de Destino
        if step == 2:

            destinos = ['Japon', 'Peru', 'China', 'EEUU']
            precios = [300000, 180000, 220000, 200000]

            print('\n!!! Paso 2 !!!\n')
            print('Los lugares a viajar disponibles son los siguientes:\n')
            a = 0
            try:
                #Print de cada destino disponible
                for destino in destinos:
                    print(str(a + 1) + '.' + destino + ' Precio del Boleto por persona -> $' + str(precios[destinos.index(destino)]))
                    a += 1
                num_destino = int(input('\nPor favor Elija un Destino para empezar (Para elegir escriba el numero) -> '))
                #Validacion de que el numero no sea ni negativo ni 0 y que tampoco sea un numero que no tenga opcion
                if num_destino > len(destinos) or num_destino <= 0:
                    step = 2
                    print('-' * 100)
                    print('Introduzca un Numero Valido')
                    print('-' * 100)
                #Continuacion al siguiente paso
                else:
                    destino  = destinos[num_destino - 1]
                    step = 3
                    print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
            except:
                print('-' * 100)
                print('POR FAVOR INTRODUZCA UN NUMERO ENTERO')
                print('-' * 100)

        #Paso 3 Introducir la cantidad de personas que viajan
        if step == 3:

            print('\n!! PASO 3 !!\n')

            #El usuario tiene que digitar la cantidad de personas que viajan
            while True:
                try:
                    cant_personas = int(input('Por favor ingrese la cantidad de personas  que van a viajar -> '))
                    #Validacion de que el dato introducido sea mayor o igual a 0
                    if cant_personas <= 0 :
                        print('-' * 100)
                        print('Introduzca un Numero Entero Valido (Mayor a 0)')
                        print('-' * 100)
                    #Validacion de que el dato introducido no sea mayor a 10
                    elif cant_personas > 10:
                        print('-' * 100)
                        print('Introduzca un Numero Entero Valido (Menor o igual a 10)')
                        print('-' * 100)
                    else:
                        step = 4
                        print('-' * 100)
                        break
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 100)
                    print('Introduzca un Numero Entero')
                    print('-' * 100)
        
        #Paso 4 Llenado de datos de cada uno de los pasajeros
        if step == 4:

            print('\n!! PASO 4 !!\n')

            #Listas en las que almaceno los datos y luego los envio a la BD
            nombres = []
            num_documentos = []
            nacionalidades = []

            #Formularios de datos para cada pasajero
            for persona in range (cant_personas):
                print(f'Por favor Ingrese los siguientes datos del Pasajero {persona + 1}:')
                
                #Formulario Nombre
                while True:
                    try:
                        nombre = str(input('Digite el Nombre/s de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nombre) <= 2:
                            print('-' * 100)
                            print('Por Favor Digite Un Valor Valido de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nombre) >= 50:
                            print('-' * 100)
                            print('Por Favor digite un valor valido de maximo 50 caracteres')
                            print('-' * 100)
                        #Todo correcto, pasamos al siguiente formulario
                        else:
                            nombres.append(nombre.lower())
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)

                #Formulario Numero de Documento
                while True:
                    try:
                        num_documento = int(input('Digite el Numero de Documento/Pasaporte Por Favor (Min. 8 Dig., Max. 8 Dig.) -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(str(num_documento)) == 8:
                            num_documentos.append(num_documento)
                            break
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Dato de 8 Caracteres de Largo')
                            print('-' * 100)
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite Un Valor Valido Numero Entero')
                        print('-' * 100)
                
                #Formulario Nacionalidad
                while True:
                    try:
                        nacionalidad = str(input('Digite la Nacionalidad de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nacionalidad) <= 2:
                            print('-' * 100)
                            print('Por Favor Digite Un Valor Valido De Al Menos 3 Cacteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nacionalidad) >= 50:
                            print('-' * 100)
                            print('Por Favor Difite Un Valor Valido De Maximo 50 Caracteres')
                            print('-' * 100)
                        #Todo correcto, pasamos al siguiente formulario
                        else:
                            nacionalidades.append(nacionalidad.lower())
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)
            #Insercion de los datos de cada uno de los pasajeros en la BD
            try:
                for persona in range(int(cant_personas)):
                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO usuarios (nombre, nacionalidad, num_documento) VALUES (%s, %s, %s);', (nombres[persona], nacionalidades[persona], num_documentos[persona]))
                    cursor.connection.commit()
                    step = 5
            except:
                print('-' * 100)
                print('Hubo un error a la hora de Insertar los Datos')
                print('-' * 100)
        
        #Paso 5 Impresion de todos los datos
        if step == 5:

            print('\n!! PASO 5 !!\n')

            print('-' * 100)
            print('\nGracias por Comprar su Ticket de Avion Aca estan datos de la Compra: ')
            print(f'\n1.Destino: {destinos[num_destino - 1]}')
            print(f'2.Cantidad de Personas que Viajan: {cant_personas}')
            print(f'3.Datos Pasajeros:')
            print('*' * 60)
            for i in range(cant_personas):
                print(f'Pasajero Numero: {i + 1}')
                print(f'Nombre: {nombres[i].capitalize()}')
                print(f'Nacionalidad: {nacionalidades[i].capitalize()}')  
                print(f'Numero de Documento: {num_documentos[i]}')
            print('*' * 60)
            print(f'4.Total A Pagar: ${precios[num_destino - 1] * cant_personas} (Precio del Boleto ${precios[(num_destino - 1)]})')
            print('*' * 60)
            break
                
            



ticket_avion()