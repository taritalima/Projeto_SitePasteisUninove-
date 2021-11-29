from flask import render_template, session, request, url_for

from loja import app, db

@app.route('/')

def home():
    return "seja bem vindo ao sistema em flask"

@app.route('/registrar')

def registrar():
    return render_template('admin/registrar.html', title = "Registrar user")