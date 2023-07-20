from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, FloatField, SelectField, IntegerField

from wtforms.validators import InputRequired, Length


class RegisterFormConnexion(FlaskForm):
    telephone = StringField(
        "Numéro de téléphone",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(min=9, max=9, message="Le numéro de téléphone doit au moins avoir 9 caractères"),
        ],
    )

   
