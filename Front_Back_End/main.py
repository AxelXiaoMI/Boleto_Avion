def ticket_avion():
    destinos = ['Japon', 'Peru', 'China', 'EEUU']
    precio = [300000, 180000, 300000, 200000]
    step = 1

    print('-' * 30)
    print('Samurai Boleto de Avion')
    print('-' * 30)
    # for i in range (1):
    while True:
        if step == 1:

            print('!! PASO 1 !!')
            print('Los lugares a viajar disponibles son los siguientes:\n')
            a = 0
            for destino in destinos:
                print(str(a + 1) + '.' + destino + ' Precio del Boleto por persona -> $' + str(precio[destinos.index(destino)]))
                a += 1
            num_destino = int(input('\nPor favor Elija un Destino para empezar (Para elegir escriba el numero) -> \n'))
            if num_destino > len(destinos) or num_destino <= 0:
                step = 1
                print('-' * 30)
                print('POR FAVOR DIGITE UN VALOR VALIDO')
                print('-' * 30)
            else:
                destino  = destinos[num_destino - 1]
                step = 2
                print('-' * 30)

        if step == 2:

            aerolineas = ['Aerolineas Argentinas', 'LATAM', 'Austral', 'American Aerlines']
            print('!! PASO 2 !!')
            print('\nLas Aeronlineas disponibles son las siguientes:\n')
            a = 0
            for aerolinea in aerolineas:
                print(str(a + 1) + '.' + aerolinea)
                a += 1
            num_aerolinea = int(input('\nPor favor Elija una Aerolinea para Viajar (Para elegir escriba el numero) -> \n'))
            print('SI DESEA VOLVER A ALGUN PASO ANTERIOR ESCRIBA EN "P" + EL NUMERO DEL PASO AL QUE QUIERA IR EN EL INPUT EJ: "P1"')
            if num_aerolinea > len(aerolineas) or num_aerolinea <= 0:
                #ME QUEDE ACA ESTABA HACIENDO LA LOGICA PARA QUE PUEDA VOLVER AL PASO ANTERIOR ESCRIBIENDO P1 Y LUEGO TENDRIA QUE AGREGARLE
                #UN PRECIO DISTINTO DEPENDIENDO DE LA AEROLINEA QUE ELIJAN Y EL SIGUIENTE PASO SERIA HACER INPUTS DE LOS DATOS DE LAS PERSONAS QUE VIAJAN
                step = 2
                print('-' * 30)
                print('POR FAVOR DIGITE UN VALOR VALIDO')
                print('-' * 30)
            else:
                aerolinea = aerolineas[num_aerolinea - 1]
                step = 3
                print('llego al final')
        

ticket_avion()