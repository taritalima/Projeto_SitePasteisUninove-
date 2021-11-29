from flask import render_template, session, request, redirect, url_for, flash
from wtforms.validators import Email
from loja import app, db, bcrypt
from .formulario import LoginFormulario, RegistrationForm
from loja.produtos.models import Addproduto, Marca, Categoria
from .models import User



@app.route('/admin')
def admin():
    produtos = Addproduto.query.all()
    return render_template('admin/index.html', title = 'Pagina administrativa',produtos=produtos)


@app.route('/marcas')
def marcas():
    if 'email' not in session:
        flash(f'Por Favor primeiro realizar o Login no sistema','success')
        return redirect(url_for('login'))
    marcas = Marca.query.order_by(Marca.id.desc()).all()
    return render_template('admin/marca.html', title = 'Pagina de Produtos',marcas=marcas)


@app.route('/categoria')
def categoria():
    if 'email' not in session:
        flash(f'Por Favor primeiro realizar o Login no sistema','success')
        return redirect(url_for('login'))
    categorias = Categoria.query.order_by(Categoria.id.desc()).all()
    return render_template('admin/marca.html', title = 'Pagina de Categorias',categorias=categorias)


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data,email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit() 
        flash(f' Obrigada {form.name.data} por registrar','success')
        #retorna para a pagina inicial após registrar o usuario 
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title = "Pagina de Registros")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f' Seja Bem Vindo! {form.email.data}','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('email ou senha incorretas,tente novamente')
    return render_template('admin/login.html',form=form, title = 'Pagina Login')
