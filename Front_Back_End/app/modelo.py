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

@app.route("/comprar_boleto/<vuelos>/<aerolinea>/<precio>")
#ME QUEDE ACA, ESTOY HACIENDO LA CUENTA DE CUANTO DEBERIAN DE PAGAR AUN NO SE BIEN LOS CLACULOS TENGO QUE VER COMO ESTA EN DESPEGAR
def comprar_boleto(vuelos, aerolinea, precio):
    if request.method == "POST":
        adultos = request.form['cantidad_personas_adultas']
        menores = request.form['cantidad_personas_menores']
        total = precio * adultos 
    return render_template("comprar_boleto.html")




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