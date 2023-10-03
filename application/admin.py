# fichier qui contient l'ensemble des routes conçernant l'admin #

from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import null

from .customer import app

from .models import (
    Article,
    saveArticle,
    getAllArticles,
    saveImageArticle,
    # un_published,
    findArticleById,
    # editArticle,
    un_delete,
    saveUser,
    getAllUsers,
    User,
    Image
    # de_activate,
)

# from application.forms import RegisterForm
from .forms import RegisterForm
from .forms_article import RegisterFormArticle
from .forms_image_article import RegisterFormImage


@app.route("/admin/users")
def users():
    users = getAllUsers()
    return render_template("admin/users.html", users=users)


# @app.route("/admin/users/<int:id_user>/activate")
# def de_active_user(id_user):
# de_activate(id_user)
# return redirect(url_for("users"))


@app.route("/admin/users/new", methods=["GET", "POST"])
def add_user():
    # if request.method == "POST":
    #     print("=======================POST")
    # else:
    #     print("=======================GET")
    #
    register_form = RegisterForm()

    # Si on arrive par POST et que le formulaire est validée
    if register_form.validate_on_submit():
        nomComplet = register_form.nomComplet.data
        telephone = register_form.telephone.data
        email = register_form.email.data
        password = register_form.password.data
        confirmation = register_form.confirmation.data
        #
        if password == confirmation:
            # Enregistrer l'utilisateur
            new_user = User(
                nomComplet=nomComplet,
                email=email,
                password=password,
                telephone=telephone
            )
            #
            saveUser(new_user)
            flash(f"L'utilisateur '{nomComplet}' est ajouté avec succès!!!")
        else:
            flash("Les deux mots de passe ne sont pas conformes!!!")
    return render_template("admin/new_user.html", form=register_form)


@app.route("/admin/articles/new", methods=["GET", "POST"])
def add_articles():
    register_form = RegisterFormArticle()
    # Si on arrive par POST et que le formulaire est validée
    if register_form.validate_on_submit():
        title = register_form.title.data
        price = register_form.price.data
        content = register_form.content.data
        img_url = register_form.img_url.data
        adresse = register_form.adresse.data
        category = register_form.category.data
        characteristic = register_form.characteristic.data
        details = register_form.details.data
        offre = register_form.offre.data
        #
        # Enregistrer l'article
        new_article = Article(
            title=title,
            price=price,
            img_url=img_url,
            adresse=adresse,
            category=category,
            characteristic=characteristic,
            details=details,
            offre=offre,
            content=content
        )
        #
        if new_article != null:
            saveArticle(new_article)
            flash(f"L'article ,'{title}',est ajouté avec succès!!!")
        else:
            flash("Désolé l'article n'a pas pu être crée!")
        #
    return render_template("admin/new_article.html", form=register_form)



@app.route("/admin/articles/image", methods=["GET", "POST"])
def add_images_articles():
    register_form = RegisterFormImage()
    # Si on arrive par POST et que le formulaire est validée
    if register_form.validate_on_submit():
        img_url = register_form.img_url.data
        article_id = register_form.article_id.data
        # Enregistrer l'image
        new_image = Image(
            img_url=img_url,
            article_id=article_id,
        )
        #
        if new_image != null:
            saveImageArticle(new_image)
            flash(f"L'image de l'article est ajouté avec succès!!!")
        else:
            flash("Désolé L'image de l'article  n'a pas pu être crée!!")
        #
    return render_template("admin/new_image_article.html", form=register_form)
