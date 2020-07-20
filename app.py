from flask import Flask, render_template, request, redirect, url_for, flash, session, request, logging
from flask_mysqldb import MySQL
import MySQLdb.cursors
from wtforms import form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt



app = Flask(__name__)
app.debug=True
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin1234'
app.config['MYSQL_DB'] = 'empresas'
mysql = MySQL(app)
# settings
app.secret_key = "mysecretkey"


@app.route('/')
def index():
    return render_template('home.html')
# login--------------------------------------------


#----------------------login----------------------------------------------
 
@app.route('/empresas')
def empresas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('empresas.html', contacts = data)
def empresas():
 return render_template('empresas.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('empresas'))
    #editar datos


@app.route('/servicios')
def servicios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios')
    data = cur.fetchall()
    cur.close()
    return render_template('servicios.html', servicios = data)

@app.route('/add_servicio', methods=['POST'])
def add_servicio():
    if request.method == 'POST':
        servicio = request.form['servicio']
        precio = request.form['precio']
        tipo_uso = request.form['tipo_uso']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO servicios (servicio, precio, tipo_uso) VALUES (%s,%s,%s)", (servicio, precio, tipo_uso))
        mysql.connection.commit()
        flash('servicios Added successfully')
        return redirect(url_for('servicios'))
    
# eliminar empresa
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('empresas'))

@app.route('/servicios')
def nombre_servicios():
 return render_template('servicios.html')

# eliminar servicio
@app.route('/deleteserv/<string:idservicios>', methods = ['POST','GET'])
def delete_servicio(idservicios):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM servicios WHERE idservicios = {0}'.format(idservicios))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('servicios'))


 #modulo servicios--------------------------------------------
# editat datos coductor
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])
# subir datos editados conductor
@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('empresas'))
# vehiculo edit
@app.route('/edits/<idservicios>', methods = ['POST', 'GET'])
def get_servicios(idservicios):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios WHERE idservicios = %s', (idservicios))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-servicios.html', servicio = data[0])
# subir datos editados 
@app.route('/updateserv/<idservicios>', methods=['POST'])
def update_servicio(idservicios):
    if request.method == 'POST':
        servicio = request.form['servicio']
        precio = request.form['precio']
        tipo_uso = request.form['tipo_uso']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE servicios
            SET servicio = %s,
                precio = %s,
                tipo_uso = %s
            WHERE idservicios = %s
        """, (servicio, precio, tipo_uso, idservicios))
        flash('servicios Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('servicios'))
#fin modulo vehiculo------------------------------------------------------
@app.route('/asignaciones')
def asignaciones():
 return render_template('asignaciones.html')

if __name__ =='__main__':
    app.run()

