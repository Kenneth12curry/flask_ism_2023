from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, FloatField, SelectField, IntegerField

from wtforms.validators import InputRequired, Length


class RegisterFormRegister(FlaskForm):
    password = PasswordField(
        "Mot de Passe",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        ],
    )


