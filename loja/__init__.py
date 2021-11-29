from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES,UploadSet, configure_uploads, patch_request_class
from flask_bcrypt import Bcrypt
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] = 'dggfgdfgdfg4545'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos  =  UploadSet ( 'photos')
configure_uploads( app, photos)
patch_request_class (app)


from loja.admin import rotas
from loja.produtos import rotas