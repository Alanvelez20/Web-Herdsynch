from flask import Flask, render_template
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt


HS=Flask(__name__)


@HS.route('/')
def principal():
    return render_template('index.html')

@HS.route('/planes/')
def planes():
    return  render_template('planes.html')

@HS.route('/informacion/')
def info():
    return  render_template('info.html')

@HS.route('/contacto/')
def contacto():
    return  render_template('contacto.html')

@HS.route('/registro/')
def registro():
    return  render_template('registro.html')

if __name__=='__main__':
    HS.run(debug=True)