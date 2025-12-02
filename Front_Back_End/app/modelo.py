from flask import Flask, render_template, url_for, redirect, jsonify, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Datos para la conexion con la base de datos en este caso es MySQL Workbench
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xiao'
app.config['MYSQL_DB'] = 'ticket_airplane'
conexion = MySQL(app)


@app.route("/inicio")
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
            return redirect(url_for('calculo_total', vuelos = vuelos, aerolinea = aerolinea, cant_menores = cant_menores, adultos= adultos, precio = precio))
        elif act_calculo == 'True':
            if cant_menores != 0:    
                for menor in range (cant_menores):
                    edad_menores.append(int(request.form[f'edad_niños_{menor+1}']))
                for edad in edad_menores:
                    if edad >= 13:
                        adultos += 1
                        cant_menores -= 1
            return redirect(url_for('calculo_total', vuelos = vuelos, aerolinea = aerolinea, cant_menores = cant_menores, adultos= adultos, precio = precio))
    return render_template("comprar_boleto.html", cant_menores = cant_menores, adultos= adultos, boton_especial = boton_especial)

@app.route("/calculo_total/<vuelos>/<aerolinea>/<int:cant_menores>/<int:adultos>/<float:precio>", methods=['GET', 'POST'])
def calculo_total(vuelos, aerolinea, cant_menores, adultos, precio):
    if request.method == 'POST':

        for a in range (adultos):    
            nombre = request.form[f'nombre_{a +1}_a']
            apellido = request.form[f'apellido_{a +1}_a']
            pais_residencia = request.form[f'pais_residencia_{a +1}_a']
            tipo_documento_a = request.form[f'tipo_documento_{a +1}_a']
            num_documento = request.form[f'num_documento_{a +1}_a']
            email = request.form[f'email_{a +1}_a']
            fecha_nacimiento = request.form[f'fecha_nacimiento_{a +1}_a']
            sexo = request.form[f'sexo_{a +1}_a']
            cursor = conexion.connection.cursor()
            cursor.execute('INSERT INTO pasajero (nombre, apellido, pais_residencia, tipo_documento, num_documento, email, fecha_nacimiento, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', (nombre, apellido, pais_residencia, tipo_documento_a, num_documento, email, fecha_nacimiento, sexo))
            cursor.connection.commit()

        for b in range (cant_menores):    
            nombre = request.form[f'nombre_{b +1}_m']
            apellido = request.form[f'apellido_{b +1}_m']
            pais_residencia = request.form[f'pais_residencia_{b +1}_m']
            tipo_documento_m = request.form[f'tipo_documento_{b +1}_m']
            num_documento = request.form[f'num_documento_{b +1}_m']
            email = request.form[f'email_{b +1}_m']
            fecha_nacimiento = request.form[f'fecha_nacimiento_{b +1}_m']
            sexo = request.form[f'sexo_{b +1}_m']
            cursor = conexion.connection.cursor()
            cursor.execute('INSERT INTO pasajero (nombre, apellido, pais_residencia, tipo_documento, num_documento, email, fecha_nacimiento, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', (nombre, apellido, pais_residencia, tipo_documento_m, num_documento, email, fecha_nacimiento, sexo))
            cursor.connection.commit()

        clase = request.form['clase']
        cursor = conexion.connection.cursor()
        cursor.execute('INSERT INTO asientos (clase) VALUES (%s);', (clase,))           
        seguro = request.form['seguro']
        cursor.execute('INSERT INTO boleto (seguro) VALUES (%s);', (seguro,))
        metodo_pago = request.form['metodo_pago']
        numero_tarjeta = request.form['numero_tarjeta']
        titular_tarjeta = request.form['titular_tarjeta']
        vencimiento_tarjeta = request.form['vencimiento_tarjeta']
        cod_seguridad_tarjeta = request.form['cod_seguridad_tarjeta']
        dni_tarjeta = request.form['dni_tarjeta']
        sexo_tarjeta = request.form['sexo_tarjeta']
        cuotas_tarjeta = request.form['cuotas_tarjeta']
        cursor = conexion.connection.cursor()
        cursor.execute('INSERT INTO pagos (metodo_pago, numero_tarjeta, titular_tarjeta, vencimiento_tarjeta, cod_seguridad_tarjeta, dni_tarjeta, sexo_tarjeta, cuotas_tarjeta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', (metodo_pago, numero_tarjeta, titular_tarjeta, vencimiento_tarjeta, cod_seguridad_tarjeta, dni_tarjeta, sexo_tarjeta, cuotas_tarjeta))
        cursor.connection.commit()

        if clase == 'premium' :
            precio *= 1.5
        elif clase == 'super_premium':
            precio *= 2.25

        if seguro == 'completo':
            precio_seguro = precio * 0.4 
        elif seguro == 'basico':
            precio_seguro = precio * 0.25
        else:
            precio_seguro = 0

        if metodo_pago == 'credito':
            cuenta_total = ((precio * adultos) + (precio * cant_menores * 0.6) + precio_seguro) * 0.85
        else:
            cuenta_total = ((precio * adultos) + (precio * cant_menores * 0.6) + precio_seguro)
        
        precio_pagar_cuota = cuenta_total / int(cuotas_tarjeta)
        return render_template("cuenta_total.html",precio_pagar_cuota = precio_pagar_cuota, cuenta_total = cuenta_total, vuelos = vuelos, aerolinea = aerolinea, cant_menores = cant_menores, adultos = adultos, precio = precio, )
            
    return render_template("completar_datos.html", vuelos = vuelos, aerolinea = aerolinea, cant_menores = cant_menores, adultos = adultos, precio = precio)



@app.route("/datos_clases")
def datos_clases():
    return render_template("datos_clases.html")

@app.route("/datos_seguros")
def datos_seguros():
    return render_template("datos_seguros.html")

def error_404(error):
    return render_template('error_404.html'), 404


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
    app.register_error_handler(404, error_404)
    app.run(debug=True)