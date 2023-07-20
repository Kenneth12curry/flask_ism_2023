from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField

from wtforms.validators import InputRequired, Length, Email


class RegisterForm(FlaskForm):
    # firstname = StringField(
    # "Prénom",
    # validators=[
    # InputRequired("Le champs est requis!!!"),
    # Length(min=3, max=25, message="La taille min est 3 et max est 25"),
    # ],
    # )
    nomComplet = StringField(
        "Nom et Prénom",
        #validators=[
            # InputRequired("Le champs est requis!!!"),
            #Length(
                #min=3,
                #max=25,
                #message="La taille min est 3 et max est 25",
            #),
        #],
    )
    email = EmailField(
        "email",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Email(),
        # ],
    )
    telephone = StringField(
        "telephone",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Email(),
        # ],
    )
    password = PasswordField(
        "Mot de Passe",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        ],
    )
    confirmation = PasswordField(
        "Confirmation",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        ],
    )
