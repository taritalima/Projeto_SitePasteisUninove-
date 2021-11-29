from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo:', [validators.Length(min=4, max=25)])
    username = StringField('Usuario:', [validators.Length(min=4, max=25)])
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova senha', [
        validators.DataRequired(),
        validators.EqualTo('confirmar', message='Senha e Confirmacao nao sao iguais')
    ])
    confirmar = PasswordField('Repete a senha')
    

class LoginFormulario(Form):
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova senha', [validators.DataRequired()])
      