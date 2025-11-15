from flask import Flask, render_template, url_for, redirect, jsonify, request, flash
from flask_mysqldb import MySQL

#Esto no se que hace debo buscar y escribir que hace
app = Flask(__name__)

#Datos para la conexion con la base de datos en este caso es MySQL Workbench
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xiao'
app.config['MYSQL_DB'] = 'ticket_airplane'
conexion = MySQL(app)

# app.secret_key = "llave_secreta"

#Para poner una direccion hay que usar el @app.route("/") y luego de la / ponemos la URL que queramos
@app.route("/")
def inicio():
    return render_template("pagina_inicio.html")


@app.route("/vuelos")
def vuelos_disponibles():
    vuelos = {}
    cursor = conexion.connection.cursor()
    cursor.execute('SELECT destino FROM VUELO;')
    vuelos = cursor.fetchall()
    vuelos = [fila[0] for fila in vuelos]
    return render_template("vuelos.html", vuelos = vuelos)

@app.route("/vuelos/<vuelos>")
def vuelos_destino(vuelos):
    aerolinea = {}
    precio = {}
    cursor = conexion.connection.cursor()
    cursor.execute('SELECT aerolinea FROM avion;')
    aerolinea = cursor.fetchall()
    aerolinea = [fila[0] for fila in aerolinea]
    cursor.execute('SELECT precio FROM boleto;')
    precio = cursor.fetchall()
    precio = [fila[0] for fila in precio]
    return render_template("vuelos_destino.html", vuelos= vuelos, aerolinea= aerolinea, precio = precio)

@app.route("/comprar_boleto/<vuelos>/<aerolinea>/<float:precio>", methods=['GET', 'POST'])
def comprar_boleto(vuelos, aerolinea, precio):
    total = None
    cant_menores = None
    adultos = None
    edad_menores = []
    boton_especial = False
    act_calculo = False
    if request.method == "POST":
        #Logica para el HTML para que este pueda repetir el codigo la cantidad de veces indicada en menores
        adultos = request.form['cantidad_personas_adultas']
        adultos = int(adultos)
        cant_menores = request.form['cantidad_personas_menores']
        cant_menores = int(cant_menores)
        act_calculo = request.form['act_calculo']
        boton_especial = True
        if cant_menores == 0:
            total = (precio * adultos) + (precio * 0.6 *cant_menores)
            return redirect(url_for('calculo_total', vuelos = vuelos, aerolinea = aerolinea, total = total, cant_menores = cant_menores, adultos= adultos, precio = precio))
        elif act_calculo == 'True':
            if cant_menores != 0:    
                for menor in range (cant_menores):
                    edad_menores.append(int(request.form[f'edad_niños_{menor+1}']))
                for edad in edad_menores:
                    if edad >= 13:
                        adultos += 1
                        cant_menores -= 1
            total = (precio * adultos) + (precio * 0.6 *cant_menores)
            return redirect(url_for('calculo_total', vuelos = vuelos, aerolinea = aerolinea, total = total, cant_menores = cant_menores, adultos= adultos, precio = precio))
    return render_template("comprar_boleto.html", total = total, cant_menores = cant_menores, adultos= adultos, boton_especial = boton_especial)

@app.route("/calculo_total<vuelos><aerolinea><int:total><int:cant_menores><int:adultos>, <float:precio>")
def calculo_total(vuelos, aerolinea, total, cant_menores, adultos, precio):
    step = 1
    if request.method == 'POST':
        if step == 1:
            cant_menores + adultos
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            pais_residencia = request.form['pais_residencia']
            tipo_documento = request.form['tipo_documento']
            num_documento = request.form['num_documento']
            email = request.form['email']
            fecha_nacimiento = request.form['fecha_nacimiento']
            sexo = request.form['sexo']
            seguro = request.form['seguro']
            metodo_pago = request.form['metodo_pago']
            step = request.form['step']
            

    return render_template("completar_datos.html", vuelos = vuelos, aerolinea = aerolinea, total = total, cant_menores = cant_menores, adultos = adultos, precio = precio, step = step)


@app.route("/datos_seguros")
def datos_seguros():
    return render_template("datos_seguros.html")

@app.route("/registrar_usuario", methods=['GET', 'POST'])
def registrar_usuario():

    if request.method == "POST":

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        sexo = request.form['sexo']
        nacionalidad = request.form['nacionalidad']
        pasaporte = request.form['pasaporte']
        telefono = request.form['telefono']
        email = request.form['email']
        contraseña = request.form['contraseña']

        cursor = conexion.connection.cursor()
        cursor.execute('SELECT email FROM pasajero WHERE email = %s;', (email,))
        check = cursor.fetchone()
        print(email)
        print(check)

        if check is None:  

            print("Adentro del if")
            cursor.execute('INSERT INTO pasajero (nombre, apellido, edad, sexo, nacionalidad, pasaporte, telefono, email, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (nombre, apellido, edad, sexo, nacionalidad, pasaporte, telefono, email, contraseña))
            cursor.connection.commit()
            cursor.close()
            print("antes del return de redireccionamiento")  
            return redirect(url_for('inicio')) 
        
        else:
            
            cursor.connection.commit()
            cursor.close()
            mensaje = 'Este correo ya Existe, pruebe con otro'
            return render_template('registrar_usuario.html', mensaje = mensaje)
            
    return render_template('registrar_usuario.html')
@app.route("/iniciar_sesion")
def iniciar_sesion():
    return render_template("iniciar_sesion.html")


if __name__ == "__main__":
    app.run(debug=True)