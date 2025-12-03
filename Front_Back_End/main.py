def ticket_avion():
    destinos = ['Japon', 'Peru', 'China', 'EEUU']
    precios = [300000, 180000, 220000, 200000]
    step = 1

    print('-' * 40)
    print('Samurai Boleto de Avion')
    print('-' * 40)

    while True:
        #Primer Paso el cual consiste en que el usuario elija el destino al que ira
        if step == 1:

            print('\n!! PASO 1 !!')
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
                    print('-' * 40)
                    print('POR FAVOR DIGITE UN VALOR VALIDO')
                    print('-' * 40)
                #Continuacion al siguiente paso
                else:
                    destino  = destinos[num_destino - 1]
                    step = 2
                    print('-' * 40)
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
            except:
                print('-' * 40)
                print('POR FAVOR DIGITE UN NUMERO ENTERO')
                print('-' * 40)

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
                    print(str(a + 1) + '.' + aerolinea + 'Precio de Aerolinea -> $' + str(precio_aero[aerolineas.index(aerolinea)]))
                    a += 1
                num_aerolinea = int(input('\nPor favor Elija una Aerolinea para Viajar (Para elegir escriba el numero) -> '))
                #Validacion de que el numero no sea ni negativo ni 0 y que tampoco sea un numero que no tenga opcion
                if num_aerolinea > len(aerolineas) or num_aerolinea <= 0:
                    step = 2
                    print('-' * 40)
                    print('POR FAVOR DIGITE UN VALOR VALIDO')
                    print('-' * 40)
                #Continuacion al siguiente paso
                else:
                    aerolinea = aerolineas[num_aerolinea - 1]
                    step = 3
                    print('\n')
            #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
            except:
                print('-' * 40)
                print('POR FAVOR DIGITE UN NUMERO ENTERO')
                print('-' * 40)

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
                        #Sigue la secuencia sin ningun problema
                        elif volver_paso.lower() == 'no':
                            #Validacion de que el numero no sea ni negativo ni 0 y que tampoco sea un numero que no tenga opcion
                            if num_aerolinea > len(aerolineas) or num_aerolinea <= 0:
                                step = 2
                            #Continuacion al siguiente paso
                            else:
                                step = 3
                                print('\n')
                                print('-' * 40)
                                break
                            print('-' * 40)
                        #Validacion de que el dato introducido sea valido
                        else:
                            print('-' * 40)
                            print('Digite un Valor Valido')
                            print('-' * 40)
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo STR
                except:
                    print('-' * 40)
                    print('Por favor Digite un Valor Valido')
                    print('-' * 40)

        #Tercer Paso pide que el usuario digite la cantidad de personas adultas y menores que viajan
        if step == 3:

            print('\n!! PASO 3 !!\n')

            #El usuario tiene que digitar la cantidad de personas ADULTAS que viajan
            while True:
                try:
                    cant_personas_adultas = int(input('Por favor ingrese la cantidad de personas ADULTAS que van a viajar (Mayores o iguales  18 Años) -> '))
                    #Validacion de que el dato introducido no sea NEGATIVO
                    if cant_personas_adultas < 0 :
                        print('-' * 40)
                        print('Digite un Valor Valido, Que NO SEA NEGATIVO')
                        print('-' * 40)
                    else:
                        break
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 40)
                    print('Por favor Digite un NUMERO ENTERO')
                    print('-' * 40)

            #El usuario tiene que digitar la cantidad de personas MENORES que viajan
            while True:    
                try:
                    cant_personas_menores = int(input('\nPor favor ingrese la cantidad de personas Menores a 18 Años que viajan -> '))
                    #Validacion de que el dato introducido no sea NEGATIVO
                    if cant_personas_menores < 0 :
                        print('-' * 40)
                        print('Digite un Valor Valido, Que NO SEA NEGATIVO')
                        print('-' * 40)
                    else:
                        break
                #Validacion del tipo de dato que introdujo el usuario sea el correcto en este caso tipo INT
                except:
                    print('-' * 40)
                    print('Por favor Digite un NUMERO ENTERO')
                    print('-' * 40)

            if cant_personas_adultas + cant_personas_menores == 0 :
                print('-' * 40)
                print('Por favor Es Necesario que al MENOS HAYA UN PASAJERO')
                print('-' * 40)
            elif cant_personas_adultas + cant_personas_menores >= 50:
                print('-' * 100)
                print('Por favor La Cantidad de Pasajeros No puede superar las 50 PERSONAS (Cap. Max. Avion = 50)')
                print('-' * 100)
            if cant_personas_menores >= 1 and not cant_personas_adultas + cant_personas_menores >= 50:
                print('\nSI EL MENOR ES IGUAL O MAYOR A 13 PAGARA UN TICKET COMO ADULTO Y SE LE CONSIDERARA COMO UNO')


ticket_avion()