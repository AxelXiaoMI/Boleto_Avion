import psycopg2

try:
    connection = psycopg2.connect(
        host = '127.0.0.1',
        port = 5432,
        user = 'prueba',
        password = '1234',
        database = 'ticket_avion'
    )
    print('Conexion Exitosa')

except Exception as ex:
    print(ex)



def ticket_avion():
    cant_personas_adultas = 2
    cant_personas_menores = 2
    # num_destino = 4
    # aerolineas = ['Aerolineas Argentinas', 'LATAM', 'Austral', 'American Aerlines']
    # num_aerolinea= 1
    # nombres = ['axel','Antonella']
    # apellidos = ['Xiao','Herrera']
    # nacionalidades = ['Argentina','Argentina']
    # tipo_documento = ['pasaporte','dni']
    # num_documentos = [12345678,87654321]
    # fecha_nacimiento = ['2005-2-27','2004-6-23']
    # generos = ['masculino','femenino']
    # asientos_elegidos = ['a4', 'a5']
    # #borrar todo esto luego

    step = 1

    destinos = ['Japon', 'Peru', 'China', 'EEUU']
    precios = [300000, 180000, 220000, 200000]

    print('-' * 100)
    print('Samurai Boleto de Avion')
    print('-' * 100)
    while True:
        #Primer Paso el cual consiste en que el usuario elija el destino al que ira
        if step == 1:

            print('\n!! PASO 1 !!\n')
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
                    step = 1
                    print('-' * 100)
                    print('POR FAVOR DIGITE UN VALOR VALIDO')
                    print('-' * 100)
                #Continuacion al siguiente paso
                else:
                    destino  = destinos[num_destino - 1]
                    step = 2
                    print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
            except:
                print('-' * 100)
                print('POR FAVOR DIGITE UN NUMERO ENTERO')
                print('-' * 100)

        #Segundo Paso Aca el usuario tiene que elegir la Aerolinea que usara
        if step == 2:
            
            aerolineas = ['Aerolineas Argentinas', 'LATAM', 'Austral', 'American Aerlines']
            precio_boleto = precios[destinos.index(destino)]
            #Precio de cada Aerolinea
            precio_aero = [precio_boleto * 1, precio_boleto * 1.25, precio_boleto * 1.50, precio_boleto * 1.75]
            print('\n!! PASO 2 !!')
            print('\nLas Aeronlineas disponibles son las siguientes:\n')
            a = 0

            try:
                #Print de cada Aerolinea disponible
                for aerolinea in aerolineas:
                    print(str(a + 1) + '.' + aerolinea + ' Precio de Aerolinea -> $' + str(precio_aero[aerolineas.index(aerolinea)]))
                    a += 1
                num_aerolinea = int(input('\nPor favor Elija una Aerolinea para Viajar (Para elegir escriba el numero) -> '))
                #Validacion de que el numero no sea ni negativo ni 0 y que tampoco sea un numero que no tenga opcion
                if num_aerolinea > len(aerolineas) or num_aerolinea <= 0:
                    step = 2
                    print('-' * 100)
                    print('POR FAVOR DIGITE UN VALOR VALIDO')
                    print('-' * 100)
                #Continuacion al siguiente paso
                else:
                    aerolinea = aerolineas[num_aerolinea - 1]
                    step = 3
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
            except:
                print('-' * 100)
                print('POR FAVOR DIGITE UN NUMERO ENTERO')
                print('-' * 100)

            #Pregunta si quiere volver a algun paso anterior
            finally:
                try:

                    while True:
                        print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                        volver_paso = str(input('En Caso de que quiera SEGUIR con la Compra escriba "No" -> '))
                        #Vuelta al paso 1
                        if volver_paso.lower() == 'p1':
                            step = 1
                            break
                        #Vuelta al paso 2
                        elif volver_paso.lower() == 'p2':
                            step = 2
                            break
                        #Sigue la secuencia sin ningun problema
                        elif volver_paso.lower() == 'no':
                            #Validacion de que el numero no sea ni negativo ni 0 y que tampoco sea un numero que no tenga opcion
                            if num_aerolinea > len(aerolineas) or num_aerolinea <= 0:
                                step = 2
                            #Continuacion al siguiente paso
                            else:
                                step = 3
                                print('-' * 100)
                                break
                            print('-' * 100)
                        #Validacion de que el dato introducido sea valido
                        else:
                            print('-' * 100)
                            print('Digite un Valor Valido')
                            print('-' * 100)
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                except:
                    print('-' * 100)
                    print('Por favor Digite un Valor Valido')
                    print('-' * 100)

        #Tercer Paso pide que el usuario digite la cantidad de personas adultas y menores que viajan
        if step == 3:

            print('\n!! PASO 3 !!\n')

            #El usuario tiene que digitar la cantidad de personas ADULTAS que viajan
            while True:
                try:
                    cant_personas_adultas = int(input('Por favor ingrese la cantidad de personas ADULTAS que van a viajar (Mayores o iguales  18 Años) -> '))
                    #Validacion de que el dato introducido no sea NEGATIVO
                    if cant_personas_adultas < 0 :
                        print('-' * 100)
                        print('Digite un Valor Valido, Que NO SEA NEGATIVO')
                        print('-' * 100)
                    else:
                        break
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 100)
                    print('Por favor Digite un NUMERO ENTERO')
                    print('-' * 100)

            #El usuario tiene que digitar la cantidad de personas MENORES que viajan
            while True:    
                try:
                    cant_personas_menores = int(input('\nPor favor ingrese la cantidad de personas Menores a 18 Años que viajan -> '))
                    #Validacion de que el dato introducido no sea NEGATIVO
                    if cant_personas_menores < 0 :
                        print('-' * 100)
                        print('Digite un Valor Valido, Que NO SEA NEGATIVO')
                        print('-' * 100)
                    else:
                        break
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 100)
                    print('Por favor Digite un NUMERO ENTERO')
                    print('-' * 100)

            #Validacion de que haya al menos un pasajero y se evite que se ponga 0 en ambos inputs 
            if cant_personas_adultas + cant_personas_menores == 0 :
                print('-' * 100)
                print('Por favor Es Necesario que al MENOS HAYA UN PASAJERO')
                print('-' * 100)
            #Validacion de que la cantidad introducida de personas no supere la capacidad del avion 
            elif cant_personas_adultas + cant_personas_menores >= 50:
                print('-' * 100)
                print('Por favor La Cantidad de Pasajeros No puede superar las 50 PERSONAS (Cap. Max. Avion = 50)')
                print('-' * 100)
            #Ingresar la edad de los menores EN CASO DE QUE HAYA
            elif cant_personas_menores >= 1 and not cant_personas_adultas + cant_personas_menores >= 50:
                print('-' * 100)
                print('\nSI EL MENOR ES IGUAL O MAYOR A 13 PAGARA UN TICKET COMO ADULTO Y SE LE CONSIDERARA COMO UNO\n')
                print('-' * 100)
                print('Por Favor la EDAD tiene que estar entre 0 y 17 años')
                print('-' * 100)
                edad_menores = []
                for menores in range (cant_personas_menores):
                    while True:
                        try:
                            edad = int(input(f'Digite la Edad del Niño {menores + 1} -> '))
                            #Validacion de que el dato introducido no sea NEGATIVO
                            if edad <= -1:
                                print('-' * 100)
                                print('Digite un Valor Valido, Que NO SEA NEGATIVO')
                                print('-' * 100)
                            #Validacion de que el dato introducido no sea mayor a 17
                            elif edad > 17:
                                print('-' * 100)
                                print('Digite un Valor Menor o Igual a 17')
                                print('-' * 100)
                            #Append a la lista de edad de menores
                            else: 
                                edad_menores.append(edad)
                                break
                        #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                        except:
                            print('-' * 100)
                            print('Por favor Digite un NUMERO ENTERO')
                            print('-' * 100)
                #Si el niño supera o es igual a los 13 años se suma un adulto y se resta un menor
                for edad_menor in edad_menores:
                    if edad_menor >= 13:
                        cant_personas_adultas += 1
                        cant_personas_menores -= 1

            #Pregunta si quiere volver a algun paso anterior
            try:
                while True:
                    print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                    volver_paso = str(input('En Caso de que quiera SEGUIR con la Compra escriba "No" -> '))
                    #Vuelta al paso 1
                    if volver_paso.lower() == 'p1':
                        step = 1
                        break
                    #Vuelta al paso 2
                    elif volver_paso.lower() == 'p2':
                        step = 2
                        break
                    #Vuelta al paso 3
                    elif volver_paso.lower() == 'p3':
                        step = 3
                        break
                    #Sigue la secuencia sin ningun problema
                    elif volver_paso.lower() == 'no':
                        print('-' * 100)
                        step = 4
                        break
                    #Validacion de que el dato introducido sea valido
                    else:
                        print('-' * 100)
                        print('Digite un Valor Valido')
                        print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)

        #Cuarto paso rellenado de datos de cada pasajero que vuela
        if step == 4:

            print('\n!! PASO 4 !!\n')

            #Listas en las que almaceno los datos y luego los envio a la BD
            nombres = []
            apellidos = []
            nacionalidades = []
            tipo_documento = []
            num_documentos = []
            fecha_nacimiento = []
            generos = []

            #Formularios de datos para cada Adulto
            for adulto in range (cant_personas_adultas):
                print(f'Por favor Ingrese los siguientes datos del Adulto {adulto + 1}:')
                #Formulario Nombre
                while True:
                    try:
                        nombre = str(input('Digite el Nombre/s de la persona (Solo el NOMBRE) -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nombre) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba un nombre de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nombre) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
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
                #Formulario Apellido
                while True:
                    try:
                        apellido = str(input('Digite el Apellido/S de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(apellido) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba un apellido de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(apellido) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
                            print('-' * 100)
                        #Todo correcto, pasamos al siguiente formulario
                        else:
                            apellidos.append(apellido.lower())
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)
                #Formulario Nacionalidad
                while True:
                    try:
                        nacionalidad = str(input('Digite la Nacionalidad de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nacionalidad) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba una palabra de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nacionalidad) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
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
                #Formulario Tipo de Documento
                while True:
                    try:
                        documento = str(input('Que tipo de Documento Tiene: Pasaporte (P) o DNI (D) -> '))
                        #Validacion de si es 'p' sea pasaporte
                        if documento.lower() == 'p':
                            tipo_documento.append('pasaporte')
                            break
                        #Validacion de si es 'd' sea dni
                        elif documento.lower() == 'd':
                            tipo_documento.append('dni')
                            break
                        #Validacion de que sea una opcion disponible
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (P o D)')
                            print('-' * 100)
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
                            print('Por favor Digite un Valor Valido (Min. 8 Dig., Max. 8 Dig.)')
                            print('-' * 100)
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Formulario Fecha de Nacimiento (AÑO)
                while True:
                    try:
                        año_nacimiento = int(input('Digite el AÑO en el que Nacio -> '))
                        #Validacion de que el dato introducido que es el año no sea mayor a este año
                        if año_nacimiento >= 2026:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (No puede Venir del Futuro)')
                            print('-' * 100)
                        #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                        elif año_nacimiento < 1900:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (No puede tener mas de 125 años)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Parte del Formulario Fecha de Nacimiento (MES)
                while True:
                    
                    try:
                        mes_nacimiento = int(input('Digite el MES en el que Nacio (Digite el mes de forma Numeral 1-12) -> '))
                        #Validacion de que el dato introducido que es el mes no sea mayor a 12
                        if mes_nacimiento > 12:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-12)')
                            print('-' * 100)
                        #Validacion de que el dato introducido no sea Negativo
                        elif año_nacimiento <= 0:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-12)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Parte del Formulario Fecha de Nacimiento (DIA)
                while True:
                    try:
                        dia_nacimiento = int(input('Digite el DIA en el que Nacio -> '))
                        #Validacion de que el dato introducido que es el mes no sea mayor a 31
                        if dia_nacimiento > 31:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-31)')
                            print('-' * 100)
                        #Validacion de que el dato introducido no sea Negativo
                        elif año_nacimiento <= 0:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-31)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Concatenacion de los datos y agregacion a lista datos
                datos_nacimiento = str(dia_nacimiento) + '-' + str(mes_nacimiento) + '-' + str(año_nacimiento)
                fecha_nacimiento.append(datos_nacimiento)
                #Formulario Generos
                while True:
                    try:
                        genero = str(input('Que Sexo es : Masculino (M) o Femenino (F) -> '))
                        #Validacion de si es 'm' sea masculino
                        if genero.lower() == 'm':
                            generos.append('masculino')
                            break
                        #Validacion de si es 'f' sea femenino
                        elif genero.lower() == 'f':
                            generos.append('femenino')
                            break
                        #Validacion de que sea una opcion disponible
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (M o F)')
                            print('-' * 100)
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido (M o F)')
                        print('-' * 100)
            
            #Formularios de datos para cada Menor            
            for menor in range (cant_personas_menores):
                print(f'Por favor Ingrese los siguientes datos del Menor {menor + 1}:')
                #Formulario Nombre
                while True:
                    try:
                        nombre = str(input('Digite el Nombre/s de la persona (Solo el NOMBRE) -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nombre) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba un nombre de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nombre) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
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
                #Formulario Apellido
                while True:
                    try:
                        apellido = str(input('Digite el Apellido/S de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(apellido) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba un apellido de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(apellido) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
                            print('-' * 100)
                        #Todo correcto, pasamos al siguiente formulario
                        else:
                            apellidos.append(apellido.lower())
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)
                #Formulario Nacionalidad
                while True:
                    try:
                        nacionalidad = str(input('Digite la Nacionalidad de la persona -> '))
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nacionalidad) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba una palabra de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nacionalidad) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
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
                #Formulario Tipo de Documento
                while True:
                    try:
                        documento = str(input('Que tipo de Documento Tiene: Pasaporte (P) o DNI (D) -> '))
                        #Validacion de si es 'p' sea pasaporte
                        if documento.lower() == 'p':
                            tipo_documento.append('pasaporte')
                            break
                        #Validacion de si es 'd' sea dni
                        elif documento.lower() == 'd':
                            tipo_documento.append('dni')
                            break
                        #Validacion de que sea una opcion disponible
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (P o D)')
                            print('-' * 100)
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
                            print('Por favor Digite un Valor Valido (Min. 8 Dig., Max. 8 Dig.)')
                            print('-' * 100)
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Formulario Fecha de Nacimiento (AÑO)
                while True:
                    try:
                        año_nacimiento = int(input('Digite el AÑO en el que Nacio -> '))
                        #Validacion de que el dato introducido que es el año no sea mayor a este año
                        if año_nacimiento >= 2026:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (No puede Venir del Futuro)')
                            print('-' * 100)
                        #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                        elif año_nacimiento < 1900:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (No puede tener mas de 125 años)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Parte del Formulario Fecha de Nacimiento (MES)
                while True:
                    
                    try:
                        mes_nacimiento = int(input('Digite el MES en el que Nacio (Digite el mes de forma Numeral 1-12) -> '))
                        #Validacion de que el dato introducido que es el mes no sea mayor a 12
                        if mes_nacimiento > 12:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-12)')
                            print('-' * 100)
                        #Validacion de que el dato introducido no sea Negativo
                        elif año_nacimiento <= 0:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-12)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Parte del Formulario Fecha de Nacimiento (DIA)
                while True:
                    try:
                        dia_nacimiento = int(input('Digite el DIA en el que Nacio -> '))
                        #Validacion de que el dato introducido que es el mes no sea mayor a 31
                        if dia_nacimiento > 31:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-31)')
                            print('-' * 100)
                        #Validacion de que el dato introducido no sea Negativo
                        elif año_nacimiento <= 0:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (Del 1-31)')
                            print('-' * 100)
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                    except:
                        print('-' * 100)
                        print('Por favor Digite la Cantidad de Caracteres Requeridos')
                        print('-' * 100)
                #Concatenacion de los datos y agregacion a lista datos
                datos_nacimiento = str(dia_nacimiento) + '-' + str(mes_nacimiento) + '-' + str(año_nacimiento)
                fecha_nacimiento.append(datos_nacimiento)
                #Formulario Generos
                while True:
                    try:
                        genero = str(input('Que Sexo es : Masculino (M) o Femenino (F) -> '))
                        #Validacion de si es 'm' sea masculino
                        if genero.lower() == 'm':
                            generos.append('masculino')
                            break
                        #Validacion de si es 'f' sea femenino
                        elif genero.lower() == 'f':
                            generos.append('femenino')
                            break
                        #Validacion de que sea una opcion disponible
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (M o F)')
                            print('-' * 100)
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido (M o F)')
                        print('-' * 100)
            step =5
            #Pregunta si quiere volver a algun paso anterior
            try:
                while True:
                    print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                    volver_paso = str(input('En Caso de que quiera SEGUIR con la Compra escriba "No" -> '))
                    #Vuelta al paso 1
                    if volver_paso.lower() == 'p1':
                        step = 1
                        break
                    #Vuelta al paso 2
                    elif volver_paso.lower() == 'p2':
                        step = 2
                        break
                    #Vuelta al paso 3
                    elif volver_paso.lower() == 'p3':
                        step = 3
                        break
                    #Vuelta al paso 4
                    elif volver_paso.lower() == 'p4':
                        print('-' * 100)
                        step = 4
                        break
                    #Sigue la secuencia sin ningun problema
                    elif volver_paso.lower() == 'no':
                        print('-' * 100)
                        step = 5
                        break
                    #Validacion de que el dato introducido sea valido
                    else:
                        print('-' * 100)
                        print('Digite un Valor Valido')
                        print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)
        #Quinto Paso Seleccion de la columna en la cual quiere viajar
        if step == 5:

            print('\n!! PASO 5 !!\n')
            
            print('Seleccione en que Fila y Columna desea viajar:')
            print('*' * 33)
            print('*' + '      Clase Super Premium      ' + '*')
            print('*' + ' (A1)-(A2)-(A3)-(A4)-(A5)-(A6) ' + '*')
            print('*' + ' (B1)-(B2)-(B3)-(B4)-(B5)-(B6) ' + '*')
            print('*' + ' ----------------------------- ' + '*')
            print('*' + '        Clase Premium          ' + '*')
            print('*' + ' (C1)-(C2)-(C3)-(C4)-(C5)-(C6) ' + '*')
            print('*' + ' (D1)-(D2)-(D3)-(D4)-(D5)-(D6) ' + '*')
            print('*' + ' ----------------------------- ' + '*')
            print('*' + '        Clase Economica        ' + '*')
            print('*' + ' (E1)-(E2)-(E3)-(E4)-(E5)-(E6) ' + '*')
            print('*' + ' (F1)-(F2)-(F3)-(F4)-(F5)-(F6) ' + '*')
            print('*' * 33)
            print('\n-La Clase Super Premium tiene un valor agregado del 150% respecto al Precio Inicial del Boleto')
            print('\n-La Clase Premium tiene un valor agregado del 100% respecto al Precio Inicial del Boleto')
            print('\n-La Clase Economica es igual al costo del boleto ')
            try:
                while True:
                    #El usuario Ingresa una letra para consultar la disponibilidad las filas de la columna
                    columna = str(input('\nDigite una Columna para consultar disponibilidad (A,B,C,D,E,F) -> ')).lower()
                    if columna == 'a' or columna == 'b' or columna == 'c' or columna == 'd' or columna == 'e' or columna == 'f':
                        cursor = connection.cursor()
                        cursor.execute(f"SELECT asiento FROM asientos WHERE asiento LIKE '%{columna}%';")
                        asientos_de_BD = cursor.fetchall()
                        cursor.connection.commit()
                        asientos_de_BD = [fila[0] for fila in asientos_de_BD]
                        asientos_ocupados = []
                        asientos_disponibles = [columna + '1', columna + '2', columna + '3', columna + '4', columna + '5', columna + '6']
                        #Chequeo de si hay algun asiento ocupado en cuyo agrega a la lista de asientos ocupado el asiento
                        for asiento in asientos_de_BD:
                            if asiento in asientos_disponibles:
                                asientos_ocupados.append(asiento)
                        #Borra de la lista asientos_disponible si el asiento esta en la lista asientos ocupados, como tal significa que esta ocupado
                        for asiento in asientos_ocupados:
                            for disponible in asientos_disponibles:
                                if asiento == disponible:
                                    asientos_disponibles.pop(asientos_disponibles.index(asiento))
                        #Avance al siguiente paso
                        step = 6
                        break
                    else:
                        print('-' * 100)
                        print('Digite un una Columna Disponible (A,B,C,D,E,F)')
                        print('-' * 100)
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)            
            #Pregunta si quiere volver a algun paso anterior
            try:
                while True:
                    print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                    volver_paso = str(input('En Caso de que quiera SEGUIR con la Compra escriba "No" -> '))
                    #Vuelta al paso 1
                    if volver_paso.lower() == 'p1':
                        step = 1
                        break
                    #Vuelta al paso 2
                    elif volver_paso.lower() == 'p2':
                        step = 2
                        break
                    #Vuelta al paso 3
                    elif volver_paso.lower() == 'p3':
                        step = 3
                        break
                    #Vuelta al paso 4
                    elif volver_paso.lower() == 'p4':
                        print('-' * 100)
                        step = 4
                        break
                    #Vuelta al paso 5
                    elif volver_paso.lower() == 'p5':
                        print('-' * 100)
                        step = 5
                        break
                    #Sigue la secuencia sin ningun problema
                    elif volver_paso.lower() == 'no':
                        print('-' * 100)
                        step = 6
                        break
                    #Validacion de que el dato introducido sea valido
                    else:
                        print('-' * 100)
                        print('Digite un Valor Valido')
                        print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)
        #Sexto Paso Eleccion de los asientos que cada uno quiera
        if step == 6: 
            print('\n!! PASO 6 !!\n')           
            asientos_elegidos = []
            columnas = ['a','b','c','d','e','f']
            #Adultos
            # try:
            while True:
                    asientos_ocupados = []
                    for i in range(cant_personas_adultas):
                        #En caso de que no haya asientos disponibles imprime un mensaje
                        if len(asientos_disponibles) == 0:
                            print('-' * 100)
                            print(f'Disculpe NO HAY MAS ASIENTOS DISPONIBLES EN ESTA COLUMNA')
                            print('-' * 100)
                            columnas.remove(columna)
                            try:
                                while True:
                                    columna = str(input('Por favor Digite otra columna -> '))
                                    if columna in columnas :
                                        cursor = connection.cursor()
                                        cursor.execute(f"SELECT asiento FROM asientos WHERE asiento LIKE '%{columna}%';")
                                        asientos_de_BD = cursor.fetchall()
                                        cursor.connection.commit()
                                        asientos_de_BD = [fila[0] for fila in asientos_de_BD]
                                        asientos_disponibles = [columna + '1', columna + '2', columna + '3', columna + '4', columna + '5', columna + '6']
                                        #Chequeo de si hay algun asiento ocupado en cuyo agrega a la lista de asientos ocupado el asiento
                                        for asiento in asientos_de_BD:
                                            if asiento in asientos_disponibles:
                                                asientos_ocupados.append(asiento)
                                        #Borra de la lista asientos_disponible si el asiento esta en la lista asientos ocupados, como tal significa que esta ocupado
                                        for asiento in asientos_ocupados:
                                            for disponible in asientos_disponibles:
                                                if asiento == disponible:
                                                    asientos_disponibles.pop(asientos_disponibles.index(asiento))
                                        break
                                    else:
                                        print('-' * 100)
                                        print('Digite un una Columna Disponible (A,B,C,D,E,F)')
                                        print('-' * 100)
                            except:
                                print('-' * 100)
                                print('Digite un una Columna Disponible (A,B,C,D,E,F)')
                                print('-' * 100)
                        #Imprime los asientos disponibles
                        print('Los asientos disponibles son estos:')
                        for asiento in asientos_disponibles:
                            print(f'({asiento.capitalize()})')

                        #Input de en que fila desea viajar el pasajero
                        fila = input(f'\nElija en que fila desea Viajar el PASAJERO ADULTO {i + 1} Ej: "A2" (En caso de que quiera consultar otra Columna Digite "N") -> ').lower()
                        
                        #Esto hace que la fila ELEGIDA se agregue a la lista asientos_elegidos y se elimine de asientos_disponibles
                        if fila in asientos_disponibles:
                            asientos_elegidos.append(fila)
                            asientos_disponibles.pop(asientos_disponibles.index(fila))

                        #Esto hace que rompa el bucle y lo mande al paso 5                           
                        elif fila == 'n':
                            step = 5
                            break

                        #Validacion de que el dato introducido sea uno valido
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (EJ: A2 o "N")')
                            print('-' * 100)
                    #Avance a la siguiente iteracion        
                    if len(asientos_elegidos) == cant_personas_adultas:
                        break
                    elif step == 5:
                        break
                        
            # except:
                # print('-' * 100)
                # print('Por favor Digite un Valor Valido (EJ: A2)')
                # print('-' * 100)

            if step == 5:
                break
                #Menores
            if step != 5:
                try:
                    while True:
                        for i in range(cant_personas_menores):
                            #En caso de que no haya asientos disponibles imprime un mensaje
                            if len(asientos_disponibles) == 0:
                                print('-' * 100)
                                print(f'Disculpe NO HAY MAS ASIENTOS DISPONIBLES EN ESTA COLUMNA')
                                print('-' * 100)
                                columnas.remove(columna)
                                try:
                                    while True:
                                        columna = str(input('Por favor Digite otra columna -> '))
                                        if columna in columnas :
                                            cursor = connection.cursor()
                                            cursor.execute(f"SELECT asiento FROM asientos WHERE asiento LIKE '%{columna}%';")
                                            asientos_de_BD = cursor.fetchall()
                                            cursor.connection.commit()
                                            asientos_de_BD = [fila[0] for fila in asientos_de_BD]
                                            asientos_disponibles = [columna + '1', columna + '2', columna + '3', columna + '4', columna + '5', columna + '6']
                                            #Chequeo de si hay algun asiento ocupado en cuyo agrega a la lista de asientos ocupado el asiento
                                            for asiento in asientos_de_BD:
                                                if asiento in asientos_disponibles:
                                                    asientos_ocupados.append(asiento)
                                            #Borra de la lista asientos_disponible si el asiento esta en la lista asientos ocupados, como tal significa que esta ocupado
                                            for asiento in asientos_ocupados:
                                                for disponible in asientos_disponibles:
                                                    if asiento == disponible:
                                                        asientos_disponibles.pop(asientos_disponibles.index(asiento))
                                            break
                                        else:
                                            print('-' * 100)
                                            print('Digite un una Columna Disponible (A,B,C,D,E,F)')
                                            print('-' * 100)
                                except:
                                    print('-' * 100)
                                    print('Digite un una Columna Disponible (A,B,C,D,E,F)')
                                    print('-' * 100)
                                #Imprime los asientos disponibles
                                print('Los asientos disponibles son estos:')
                                for asiento in asientos_disponibles:
                                    print(f'({asiento.capitalize()})')

                            #Input de en que fila desea viajar el pasajero
                            print(f'\nElija en que fila desea Viajar el PASAJERO MENOR {i + 1} Ej: "A2"') 
                            fila = input('(En caso de que quiera consultar otra Columna Digite la Letra EJ:"B" O tambien puede Digitar "N" para volver al paso 5) -> ').lower()

                            #Esto hace que la fila ELEGIDA se agregue a la lista asientos_elegidos y se elimine de asientos_disponibles
                            if fila in asientos_disponibles:
                                asientos_elegidos.append(fila)
                                asientos_disponibles.pop(asientos_disponibles.index(fila))

                            #Esto hace que selecione otra columna                     
                            elif fila in columnas:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT asiento FROM asientos WHERE asiento LIKE '%{fila}%';")
                                asientos_de_BD = cursor.fetchall()
                                cursor.connection.commit()
                                asientos_de_BD = [fila[0] for fila in asientos_de_BD]
                                asientos_disponibles = [fila + '1', fila + '2', fila + '3', fila + '4', fila + '5', fila + '6']
                                #Chequeo de si hay algun asiento ocupado en cuyo agrega a la lista de asientos ocupado el asiento
                                for asiento in asientos_de_BD:
                                    if asiento in asientos_disponibles:
                                        asientos_ocupados.append(asiento)
                                #Borra de la lista asientos_disponible si el asiento esta en la lista asientos ocupados, como tal significa que esta ocupado
                                for asiento in asientos_ocupados:
                                    for disponible in asientos_disponibles:
                                        if asiento == disponible:
                                            asientos_disponibles.pop(asientos_disponibles.index(asiento))
                                #Imprime los asientos disponibles
                                print('Los asientos disponibles son estos:')
                                for asiento in asientos_disponibles:
                                    print(f'({asiento.capitalize()})')
                            #Esto es para volver al paso 5
                            elif fila == 'n':
                                step = 5
                                break
                            #Validacion de que el dato introducido sea uno valido
                            else:
                                print('-' * 100)
                                print('Por favor Digite un Valor Valido (EJ: A2 o "B")')
                                print('-' * 100)
                        if len(asientos_elegidos) == cant_personas_adultas + cant_personas_menores:
                            step = 7
                            break
                        elif step == 5:
                            break
                except:
                    print('-' * 100)
                    print('Por favor Digite un Valor Valido (EJ: A2)')
                    print('-' * 100)
                    if step == 5:
                        break
                 #Pregunta si quiere volver a algun paso anterior
            try:
                while True:
                    print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                    volver_paso = str(input('En Caso de que quiera SEGUIR con la Compra escriba "No" -> '))
                    #Vuelta al paso 1
                    if volver_paso.lower() == 'p1':
                        step = 1
                        break
                    #Vuelta al paso 2
                    elif volver_paso.lower() == 'p2':
                        step = 2
                        break
                    #Vuelta al paso 3
                    elif volver_paso.lower() == 'p3':
                        step = 3
                        break
                    #Vuelta al paso 4
                    elif volver_paso.lower() == 'p4':
                        print('-' * 100)
                        step = 4
                        break
                    #Vuelta al paso 5
                    elif volver_paso.lower() == 'p5':
                        print('-' * 100)
                        step = 5
                        break
                    #Vuelta al paso 6
                    elif volver_paso.lower() == 'p6':
                        print('-' * 100)
                        step = 6
                        break
                    #Sigue la secuencia sin ningun problema
                    elif volver_paso.lower() == 'no':
                        print('-' * 100)
                        step = 7
                        break
                    #Validacion de que el dato introducido sea valido
                    else:
                        print('-' * 100)
                        print('Digite un Valor Valido')
                        print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)
        #Septimo paso Datos de la tarjeta
        if step == 7:
            
            print('\n!! PASO 7 !!\n')
            print('Introduzca los datos de la tarjeta\n')
            # Metodo de Pago
            while True:
                    try:
                        metodo_pago = str(input('Digite el Metodo de Pago (Credito (C) o Debito (D)) -> ')).lower()
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        if metodo_pago in ['c','d']:
                            break
                        else:
                            print('-' * 100)
                            print('Por favor Digite un Valor Valido (C o D)')
                            print('-' * 100)

                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)
            #Nombre del titular
            while True:
                    try:
                        nombre_tarjeta = str(input('Digite el Nombre COMPLETO del dueño de la tarjeta (Solo el NOMBRE) -> ')).lower()
                        #Validacion de que el dato introducido al menos tenga 3 caracteres
                        if len(nombre_tarjeta) <= 2:
                            print('-' * 100)
                            print('Por Favor Escriba un nombre de al menos 3 Caracteres')
                            print('-' * 100)
                        #Validacion de que el dato introducido no supere el maximo de caracteres permitidos
                        elif len(nombre_tarjeta) >= 60:
                            print('-' * 100)
                            print('A excedido el limite de Caracteres Permitidos')
                            print('-' * 100)
                        #Todo correcto, pasamos al siguiente formulario
                        else:
                            break
                    #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                    except:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido')
                        print('-' * 100)
            #Formulario Numero de la Tarjeta
            while True:
                try:
                    num_tarjeta = int(input('Digite el Numero de la Tarjeta Por Favor (Min. 14 Dig., Max. 14 Dig.) -> '))
                    #Validacion de que el dato introducido al menos tenga 3 caracteres
                    print(num_tarjeta)
                    if len(str(num_tarjeta)) == 14:
                        break
                    else:
                        print('-' * 100)
                        print('Por favor Digite un Valor Valido (Min. 14 Dig., Max. 14 Dig.)')
                        print('-' * 100)
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 100)
                    print('Por favor Digite la Cantidad de Caracteres Requeridos')
                    print('-' * 100)
            print('-' * 100)
            print('\nGracias por comprar su ticket de avion le dejamos los siguientes datos para que confirme: ')
            print(f'\n1.Destino: {destinos[num_destino-1]}')
            print(f'2.Aerolinea: {aerolineas[num_aerolinea]}')
            print(f'3.Cantidad de Personas que Viajan: {cant_personas_adultas + cant_personas_menores} (Adultos: {cant_personas_adultas}, Menores: {cant_personas_menores})')
            print('*' * 60)
            print(f'4.Datos Pasajeros (Adultos):')
            print('*' * 60)
            for i in range(cant_personas_adultas):
                print(f'Pasajero Numero: {i + 1}')
                print(f'Nombre: {nombres[i].capitalize()}')
                print(f'Apellido: {apellidos[i].capitalize()}')
                print(f'Nacionalidad: {nacionalidades[i].capitalize()}')  
                print(f'Tipo de Documento: {tipo_documento[i].capitalize()}')
                print(f'Numero de Documento: {num_documentos[i]}')
                print(f'Fecha de Nacimiento: {fecha_nacimiento[i]}')
                print(f'Sexo: {generos[i].capitalize()}')
            print('*' * 60)
            print(f'4.Datos Pasajeros (Menores):')
            print('*' * 60)
            for i in range(cant_personas_menores):
                i = i + cant_personas_adultas
                print(f'Pasajero Numero: {i + 1}')
                print(f'Nombre: {nombres[i].capitalize()}')
                print(f'Apellido: {apellidos[i].capitalize()}')
                print(f'Nacionalidad: {nacionalidades[i].capitalize()}')  
                print(f'Tipo de Documento: {tipo_documento[i].capitalize()}')
                print(f'Numero de Documento: {num_documentos[i]}')
                print(f'Fecha de Nacimiento: {fecha_nacimiento[i]}')
                print(f'Sexo: {generos[i].capitalize()}')
            print('*' * 60)
            print(f'5.Datos Asientos (Adultos):')
            for i in range(cant_personas_adultas):
                print('*' * 60)
                print(f'Asiento Seleccionado (Adultos): {asientos_elegidos[i].capitalize()}')
                print('*' * 60)
                print(f'5.Datos Asientos (Menores):')
            for i in range(cant_personas_menores):
                print('*' * 60)
                print(f'Asiento Seleccionado (Menores): {asientos_elegidos[i + cant_personas_adultas].capitalize()}')
            print('*' * 60)
            print(f'7.Datos Tarjeta :')
            print('*' * 60)
            print(f'Nombre del Propietario {nombre_tarjeta.capitalize()}')
            if metodo_pago == 'c':
                print(f'Metodo de Pago: Credito')
            elif metodo_pago == 'd':
                print(f'Metodo de Pago: Debito')
            print(f'Numero de Tarjeta: {num_tarjeta}')
            print('*' * 60) 

            #Pregunta si quiere volver a algun paso anterior
            try:
                while True:
                    print('\nDesea Volver a Algun Paso Anterior? Si es Asi digite "P" mas el numero del paso (EJ: "P1")')
                    volver_paso = str(input('En Caso de que quiera TERMINAR con la Compra escriba "No" -> '))
                    #Vuelta al paso 1
                    if volver_paso.lower() == 'p1':
                        step = 1
                        break
                    #Vuelta al paso 2
                    elif volver_paso.lower() == 'p2':
                        step = 2
                        break
                    #Vuelta al paso 3
                    elif volver_paso.lower() == 'p3':
                        step = 3
                        break
                    #Vuelta al paso 4
                    elif volver_paso.lower() == 'p4':
                        print('-' * 100)
                        step = 4
                        break
                    #Vuelta al paso 5
                    elif volver_paso.lower() == 'p5':
                        print('-' * 100)
                        step = 5
                        break
                    #Vuelta al paso 6
                    elif volver_paso.lower() == 'p6':
                        print('-' * 100)
                        step = 6
                        break
                    #Vuelta al paso 7
                    elif volver_paso.lower() == 'p7':
                        print('-' * 100)
                        step = 7
                        break
                    #Sigue la secuencia sin ningun problema
                    elif volver_paso.lower() == 'no':
                        print('-' * 100)
                        step = 8
                        break
                    #Validacion de que el dato introducido sea valido
                    else:
                        print('-' * 100)
                        print('Digite un Valor Valido')
                        print('-' * 100)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
            except:
                print('-' * 100)
                print('Por favor Digite un Valor Valido')
                print('-' * 100)            

        if step == 8:

            #Paso Numero 8
            #Insercion de los datos de cada uno de los pasajeros en la BD
            try:
                for persona in range(int(cant_personas_menores + cant_personas_adultas)):
                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO usuarios (nombre, apellido, nacionalidad, tipo_documento, num_documento, fecha_nacimiento, genero) VALUES (%s, %s, %s, %s, %s, %s, %s);', (nombres[persona], apellidos[persona], nacionalidades[persona], tipo_documento[persona], num_documentos[persona], fecha_nacimiento[persona], generos[persona]))
                    cursor.connection.commit()
                cursor = connection.cursor()
                cursor.execute(f'SELECT id_usuario FROM usuarios WHERE num_documento = {num_documentos[persona]}')
                id_usuario = cursor.fetchall()
                id_usuario = [id_u[0] for id_u in id_usuario]
                cursor.connection.commit()
                for persona in range(int(cant_personas_menores + cant_personas_adultas)):
                    cursor = connection.cursor()
                    cursor.execute(f"INSERT INTO asientos (id_pasajero_asiento, asiento) VALUES ({id_usuario[persona]}, '{str(asientos_elegidos[persona])}');")
                    cursor.connection.commit()
            except:
                print('-' * 100)
                print('Hubo un error a la hora de Insertar los Datos')
                print('-' * 100)
            
            print('Todo Salio Correcto, Gracias Por su Compra (BD)')
ticket_avion()   