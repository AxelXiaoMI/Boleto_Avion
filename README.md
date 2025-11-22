# Primer Proyecto 

Comparto mi primer proyecto el cual es una pagina de compra de un ticket de avion basica, para el frontend use unicamente HTML5,
para el backend use Python (3.13.7) y para agregarle mas realismo use como base de datos a MySQL Workbench (8.0.43).

Para hacer la comunicacion entre HTML y Python use la libreria de "Flask" que este posee y para la base de datos use una extension "Flask_mysqldb".

# Instalacion
Para hacer la instalacion solamente tenemos que instalar la libreria:
```bash
pip install Flask
```

# Como Funciona el programa
En primer lugar una vez iniciado el codigo y entramos en la url de la pagina (http://127.0.0.1:5000)

Nos encontraremos con esta pagina, la cual aparecera cuando el usuario quiera entrar o por error cargue una url la cual no hemos asignado.

<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/e8da0a69-0b99-4ede-976a-5e24e2d122bd" />

----

El link nos manda a la siguiente pagina web:

<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/39418763-fadf-4a17-a2b0-d5c08b557e2b" />

----

En la cual solo encontraremos un pequeño titulo y otro link en donde nos muestra los "Vuelos Disponibles" el cual
al hacer click nos redirecciona a la pagina donde se puede observar los vuelos disponibles, con sus respectivos destinos e imagenes.

<img width="350" height="700" alt="image" src="https://github.com/user-attachments/assets/6a6b220b-eaf2-4fee-b940-2f71c9cec7fb" />

----

Al hacer click en cualquier link, en este caso elegi "Tokio", nos envia a una pagina en donde se muestran las distintas aerolineas que hacen este vuelo
Muestra: Imagen de la aerolinea, destino, desde que lugar sale, nombre de la aerolinea, el precio por persona y el link.
(Este precio es ilustrativo ya que es el de la clase economica y puede variar segun elija el usuario.)

<img width="400" height="700" alt="image" src="https://github.com/user-attachments/assets/12d18f68-6561-4371-af69-1a26b0bc4b29" />

----

Una vez que ya elegimos y clickeamos el link, nos manda a la pagina "Comprar Boleto" en donde tenemos que indicar la cantidad de personas adultas (+18) y menores (-17)
que viajan una vez que le damos a "Enviar" y nos redirecciona a la siguiente pagina, pero si viajan menores se despliega un formulario el cual es proporcional
a la cantidad de menores que viajan para que ingresen la edad de cada uno de estos. Dato no menor es que si el menor a 13 años este pagara una sexta parte del ticket y en caso contrario
ya contaria como adulto y se le cobrara el monto completo.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/759c7009-7296-4e6b-ba6c-406b5bc9811f" />

----

Una vez que completamos los datos y le damos a "Enviar" esta nos manda a la siguiente pagina:
En donde para empezar tenemos los formularios en donde pedimos los datos de las personas que viajan tanto adultos como menores.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/f2acf1d9-5b82-4847-b831-fefb799e35d3" />

----

Mas abajo luego de los datos de los pasajeros tenemos que escoger que clase preferimos:
En este caso elegi "Premium", como comente antes los precios varian dependiendo de la clase el premium es: precio_ticket * 1.5 y
el "Super Premium" es: precio_ticket * 2.25. 

Y en la parte inferior tenemos un link en donde explica los beneficios de cada clase, pero es solo texto no tiene nada relevante.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/43d411b3-d99d-4331-93d8-456cdf164edd" />

----

Despues esta el formulario del seguro, encontramos el de seguro en donde elegimos que tanta proteccion queremos en caso de un imprevisto.

Elegi "Ninguno" el cual como su nombre indica no es ningun seguro, luego tenemos el "Basico" y "Completo", cada uno con sus respectivos precios
y el calculo es: Basico: precio_ticket * 0.25 y Completo: precio_ticket * 0.4.

Este tambien tiene un link en donde explica los distintos tipos de seguros que hay pero es irrelevante es puro texto tambien.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/4f31a962-4533-4e28-ab8e-4b7972f72bd1" />

----

Prosigue el metodo de pago, en donde es con Tarjeta de Credito o Cebito y para aplicarle un beneficio al pagar con Credito tiene un 15% descuento del total.

<img width="1217" height="244" alt="image" src="https://github.com/user-attachments/assets/242f68e1-6962-44b2-95b6-807fec19a2fb" />

----

Finalmente tenemos formularios con datos de la tarjeta, y abajo un cuadro en donde elige la cantidad de cuotas que desea hacerlo.

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/9e04ada8-3794-4dde-bfb2-4d7a3cc3caff" />

----

Una vez que le clickeamos en "Enviar" nos aparece la pagina final en donde, nos muestra cuanto es en total y cuanto habria que pagar en cada cuota, y un link el cual al clickear
nos manda a la pagina de inicio

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/bcc73f4e-3e20-458d-8a44-a5e50bd59ee4" />

----

Algo a recalcar es que a medida que vamos avanzando con el proceso de la compra cada pagina a la cual entramos su url esta compuesta, por los datos que elegimos.
En este ejemplo: Yo elegi un viaje a "Tokio", con la aerolinea "Latam Aerlines" y el precio del boleto.

<img width="762" height="65" alt="image" src="https://github.com/user-attachments/assets/e19a59b8-9fbe-42b4-b6d1-b3a40c042d00" />

----

Es sencillo si, pero es porque para poder correr tienes que caminar primero.
