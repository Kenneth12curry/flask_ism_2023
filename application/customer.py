# fichier qui contient l'ensemble des routes conçernant le client #

from flask import Flask, render_template, redirect, url_for, request, flash, session
from sqlalchemy import null
# from flask_paginate import Pagination, get_page_parameter

# importation de la méthode getAllArticles#
from .fake_data import getAllArticles, getAllShops

from .forms_article import RegisterFormArticle

app = Flask(__name__)


# Montrer à flask là où se trouve notre fichier de config
app.config.from_object("config")

from .models import \
    (
    saveArticle,
    Article,
    findArticleById,
    findImageArticleById,
    findUserByTelephoneAndPassword,
    saveUser,
    User,
    Shop,
    getAllShop,
    searchArticle
)

from .form_connexion import RegisterFormConnexion
from .form_register import RegisterFormRegister


@app.route("/compte/login", methods=["GET", "POST"])
def compte():
    if request.method == 'POST':
        # Récupération du tel dans une session
        session['input_value'] = request.form['tel']
        return redirect(url_for('register'))
    return render_template('connexion/compte.html')


@app.route("/compte/register", methods=["GET", "POST"])
def register():
    register_form = RegisterFormRegister()
    if register_form.validate_on_submit():
        # Récupération du tel de l'utilisateur qui se trouve dans la session
        input_value = session.get('input_value')
        # Récupérer le password de l'utilisateur
        password = register_form.password.data
        # user = User.query.filter_by(username=username, password=password).first()
        user = User.query.filter_by(telephone=input_value, password=password).first()

        if user:
            # flash(f"Bienvenue sur Expat-Dakar !!")
            # Stockage de l'utilisateur dans la session
            session['user'] = user.id
            return redirect(url_for('user_area'))
        # si l'utilisateur n'existe pas
        else:
            # Enregistrer l'utilisateur
            #new_user = User(
                #telephone=input_value,
                #password=password
            #)
            #if new_user != null:
                #saveUser(new_user)
            flash('Mot de passe invalide')
            # flash(f"L'utilisateur est ajouté avec succès!!!")

    return render_template("connexion/register.html", form=register_form)



# méthode pour l'inscription"
@app.route("/compte/inscription", methods=["GET", "POST"])
def inscription():
    register_form = RegisterFormRegister()
    # Vérifier si la requête est une requête POST
    if request.method == 'POST':
        tel = request.form['tel']
        if register_form.validate_on_submit():
            # Récupérer le password de l'utilisateur
            password = register_form.password.data
            # Enregistrer l'utilisateur
            new_user = User(
                telephone=tel,
                password=password
            )
            saveUser(new_user)
            # Stockage de l'utilisateur dans la session
            session['user'] = new_user.id
            if new_user != null:
                flash("Bienvenue sur Expat Dakar!")
                return redirect(url_for('user_area'))

    return render_template("connexion/inscription.html", form=register_form)




# page home #
@app.route("/")
def index():
    product = Shop.query.all()
    posts = Article.query.all()
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    if user:
        return render_template('customer/Home.html', posts=posts, product=product, user=user)
    else:
        return render_template("customer/Home.html", posts=posts, product=product)


# Déconnexion de l'utilisateur
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


# page article #
@app.route('/article', methods=["GET", "POST"])
def index2():
    page = request.args.get('page', default=1, type=int)
    per_page = 10
    # per_page = request.args.get('max_per_page', default=10, type=int)
    filter_value = request.args.get('a', default=None, type=str)

    # Obtention des données filtrées
    if filter_value:
        data = Article.query.filter_by(category=filter_value).paginate(page=page, per_page=per_page)
    else:
        data = Article.query.paginate(page=page, per_page=per_page)

    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()

    # Affichage de la page
    return render_template('customer/article.html', data=data, user=user)
    # return render_template('customer/article.html', articles=articles, pagination=pagination, filter_value=filter_value)
    # return render_template('customer/article.html', articles=articles)
    # return render_template('customer/article.html', posts=posts)


@app.route("/expat/article/<int:id_article>")
def article(id_article):
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    article = findArticleById(id_article)
    image_article = findImageArticleById(id_article)
    if not article:
        return redirect(url_for("index"))
    return render_template("customer/details_article.html", article=article, image_article=image_article, user=user)


# Pages véhicules
@app.route("/expat/article/vehicules")
def vehicules():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    articles = Article.query.filter_by(category="Véhicules")
    return render_template("customer/vehicules.html", user=user, article=articles)

@app.route("/expat/article/voitures")
def voitures():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    articles = Article.query.filter_by(category="Véhicules")
    return render_template("customer/vehicules.html", user=user, article=articles)


@app.route("/expat/article/motos&scooters")
def motos():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    articles = Article.query.filter_by(category="Véhicules")
    return render_template("customer/vehicules.html", user=user, article=articles)


@app.route("/expat/article/location&voiture")
def location():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    articles = Article.query.filter_by(category="Véhicules")
    return render_template("customer/vehicules.html", user=user, article=articles)


@app.route("/expat/article/equipements&pieces")
def pieces():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    articles = Article.query.filter_by(category="Véhicules")
    return render_template("customer/vehicules.html", user=user, article=articles)

#
# Méthode pour rechercher un ou des articles
@app.route("/expat/annonces")
def findArticle():
    # Récupérer l'utilisateur qui est connecté
    search = request.args.get('recherche')
    user = User.query.filter_by(id=session.get('user')).first()
    articles = searchArticle(search)
    if articles:
        data = articles
        return render_template("customer/article.html", data=data, user=user)
#

@app.route("/expat/annoncesVehicules", methods=["GET", "POST"])
def annonceVehicule():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    category = request.args.get('value')
    vehicule = Article.query.filter_by(category=category)
    if vehicule:
        data = vehicule
        return render_template("customer/article.html", data=data, user=user)

# Partie connexion utilisateur
@app.route("/espace/user")
def user_area():
    user = User.query.filter_by(id=session.get('user')).first()
    if user:
        return render_template("layouts/base_user_area.html", user=user)


@app.route("/espace/user/message")
def message():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/message.html", user=user)


@app.route("/espace/user/discussion")
def discussion():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/discussion.html", user=user)


@app.route("/espace/user/cv")
def profil():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/profil_cv.html", user=user)


@app.route("/espace/user/annonces")
def annonce():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/annonces.html", user=user)

@app.route("/espace/user/achat")
def achat():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/achats.html", user=user)


@app.route("/espace/user/publier", methods=["GET", "POST"])
def publier():
    register_form = RegisterFormArticle()
    if request.method == "POST":
        title = register_form.title.data
        category = register_form.category.data
        img_url = register_form.img_url.data
        description = register_form.content.data
        price = register_form.price.data
        adresse = register_form.adresse.data
        # title = request.args.get('title')
        characteristic = register_form.characteristic.data
        # Enregistrer l'article
        new_article = Article(
            title=title,
            price=price,
            img_url=img_url,
            adresse=adresse,
            category=category,
            characteristic=characteristic,
            # details=details,
            # offre=offre,
            content=description
        )
        if new_article != null:
            saveArticle(new_article)
            flash(f"Annonce publié avec succès!!!")

    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    #
    listeCategory = ["Véhicules", "Sports", "Multimédia", "Mode&beauté",
                     "Agroalimentaire", "Services", "Immobilier", "Animaux", "Offres d'emploi"]
    etat = ["Neuf", "venant", "d'occassion"]
    return render_template("user_area/publier.html", listeCategory=listeCategory, etat=etat, user=user, form=register_form)


@app.route("/espace/user/credits")
def credit():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/achat_credits.html", user=user)


@app.route("/espace/user/favoris")
def favoris():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/favoris.html", user=user)


@app.route("/espace/user/alertes")
def alertes():
    # Récupérer l'utilisateur qui est connecté
    user = User.query.filter_by(id=session.get('user')).first()
    return render_template("user_area/alertes.html", user=user)
