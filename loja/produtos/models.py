from loja import db

from datetime import datetime


class Addproduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'),nullable=False)
    marca = db.relationship('Marca',backref=db.backref('marcas', lazy=True))
    
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'),nullable=False)
    categoria = db.relationship('Categoria',backref=db.backref('categorias', lazy=True))
 
    image_1 = db.Column(db.String(150), nullable=False, default ='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default ='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default ='image.jpg')
 

    def __repr__(self):
        return '<Addproduto %r>' % self.name



class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable= False, unique=True)
    
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable= False, unique=True)
    
    
db.create_all()