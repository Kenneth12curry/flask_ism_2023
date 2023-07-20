from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, FloatField, SelectField, TextAreaField

from wtforms.validators import InputRequired, Length


class RegisterFormArticle(FlaskForm):
    # firstname = StringField(
    # "Prénom",
    # validators=[
    # InputRequired("Le champs est requis!!!"),
    # Length(min=3, max=25, message="La taille min est 3 et max est 25"),
    # ],
    # )
    title = StringField(
        "Titre de l'article",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(
                min=3,
                max=255,
                message="La taille min est 3 et max est 255",
            ),
        ],
    )

    price = FloatField(
        "prix",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(
        # min=3,
        # max=25,
        # message="La taille min est 3 et max est 25",
        # ),
        # ],
    )

    adresse = StringField(
        "Région/ville",
        validators=[
            Length(
                min=3,
                max=25,
                message="La taille min est 3 et max est 25",
            ),
        ],
    )

    img_url = StringField(
        "image_url",
        validators=[
            # InputRequired("Le champs est requis!!!"),
            Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        ],
    )

    category = SelectField(
        "Choisissez une catégorie",
        choices=[("Véhicules"), ("Sports"), ("Multimédia"), ("Mode&beauté"),
                 ("Agroalimentaire"), ("Services"), ("Immobilier"), ("Animaux"), ("Offres d'emploi")]
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        # ],
    )

    content = TextAreaField(
        "description",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        # ],
    )
    characteristic = SelectField(
        "Etat du produit",
        choices=[('neuf'), ('Venant'), ('d occassion')]
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        # ],
    )

    details = TextAreaField(
        "details",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        # ],
    )

    offre = StringField(
        "ofrre",
        # validators=[
        # InputRequired("Le champs est requis!!!"),
        # Length(min=6, message="Le mot de passe doit au moins avoit 6 carateres!"),
        # ],
    )
