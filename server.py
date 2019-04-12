from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from aulas import Aulas
from horario import Horario
from cl_reserva import Reserva
from correo import Correo
from datetime import datetime, date, time, timedelta


app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    aulas = Aulas()
    lista_aulas = aulas.leer_registros()
    horario = Horario()
    lista_horario = horario.leer_registros()
    return render_template('index.html', lista_aulas = lista_aulas, lista_horario = lista_horario)

@app.route('/nueva_reserva', methods=['POST'])
def nueva_reserva():
    if request.method == 'POST':
        localiza_reserva = Reserva(0, request.form['aula'], request.form['fecha'], request.form['actividad'], request.form['horario'], request.form['profesional'], request.form['observaciones'], request.form['email'])
        lista_localiza_reserva = localiza_reserva.busca_reserva_aula_fecha_horario(request.form['aula'], request.form['fecha'], request.form['horario'])
        if len(lista_localiza_reserva)>0:
            flash('Ya existe una reserva con esos parametros')
        else:
            reserva = Reserva(0, request.form['aula'], request.form['fecha'], request.form['actividad'], request.form['horario'], request.form['profesional'], request.form['observaciones'], request.form['email'])
            reserva.nueva_reserva()
            flash('Reserva Realizada')
        return redirect(url_for('index'))

@app.route('/buscar_reservar')
def buscar_reservas():
    aulas = Aulas()
    lista_aulas = aulas.leer_registros()
    return render_template('buscar_reservas.html', lista_aulas = lista_aulas)
    
@app.route('/listado_reservas', methods=['POST'])
def listado_reservar():
    if request.method == 'POST':
        aulas = Aulas()
        lista_aulas = aulas.leer_registros()
        reservas = Reserva(0,0,0,0,0,0,0,0)
        codigo_aula = int(request.form['aula'])  
        desde = request.form['desde']
        hasta = request.form['hasta']
       
        if codigo_aula < 1:
            lista_reservas = reservas.buscar_reservas_fecha(request.form['desde'], request.form['hasta'])
        else :
            lista_reservas = reservas.buscar_reservas_aula(codigo_aula, request.form['desde'], request.form['hasta'])
        
        return render_template('buscar_reservas.html',desde = desde, hasta = hasta, lista_aulas = lista_aulas, lista_reservas = lista_reservas, )

#Modificar Reserva
@app.route('/modifica_reserva/<id>')
def obtener_reserva(id):
    aulas = Aulas()
    lista_aulas = aulas.leer_registros()
    horario = Horario()
    lista_horario = horario.leer_registros()
    reserva = Reserva(id,0,0,0,0,0,0,0)
    datos_reserva = reserva.seleciona_reserva()
    fecha = datetime.strftime(datos_reserva[0][2], "%d/%m/%Y")
    return render_template('edita_reserva.html', fecha = fecha, reserva = datos_reserva[0], lista_aulas = lista_aulas, lista_horario = lista_horario)


#Actualizar reserva
@app.route('/update/<id>', methods = ['POST'])
def modifica_reserva(id):
    aulas = Aulas()
    lista_aulas = aulas.leer_registros()
    horario = Horario()
    lista_horario = horario.leer_registros()
    if request.method == 'POST':
        aula = request.form['aula']
        print (aula)
        reserva = Reserva(id, request.form['aula'], request.form['fecha'], request.form['actividad'], request.form['horario'], request.form['profesional'], request.form['observaciones'], request.form['email'])
        reserva.modifica_reserva()
        del reserva
        flash('Reserva Actualizada')
        reserva = Reserva(id,0,0,0,0,0,0,0)
        datos_reserva = reserva.seleciona_reserva()
        fecha = datetime.strftime(datos_reserva[0][2], "%d/%m/%Y")
        return render_template('edita_reserva.html', fecha = fecha, reserva = datos_reserva[0], lista_aulas = lista_aulas, lista_horario = lista_horario)

@app.route('/delete', methods = ['GET'])
def delete():
    codigo = request.args.get('valor')
    print(codigo)
    #print ("Dentro del Delete")
    #checkin_resp = request.data
    #codigo_reserva  = checkin_resp.get('cod_reserva')
    reserva = Reserva(4,0,0,0,0,0,0,0)
    reserva.borrar_reserva()


def validateDateEs(date):
    #Funcion para validar una fecha en formato:
    #dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s

    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False


if __name__ == '__main__':
    app.run(port=5000, debug = True)

