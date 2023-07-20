from flask_sqlalchemy import SQLAlchemy,session

from math import ceil

from .customer import app

import logging as log

from sqlalchemy import desc
import datetime

# # Créer une instance de la base de donnees
# db = SQLAlchemy()
# # Relier la base de donnee avec l'application
# db.init_app(app)
# OU BIEN
db = SQLAlchemy(app)


# Creation des Models
class Article(db.Model):
    __tablename__ = "article"  # Au cas où on change le nom de la table
    #
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    price = db.Column(db.Double, nullable=False)
    adresse = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(255))
    #
    content = db.Column(db.String(200), nullable=True)
    characteristic = db.Column(db.String(200), nullable=True)
    details = db.Column(db.String(200), nullable=True)
    offre = db.Column(db.String(200), nullable=True)
    published_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)


# Création du model Image
class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(255))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = db.relationship('Article', backref='images')


# Création du model Category
class Shop(db.Model):
    __tablename__ = "shop"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True, unique=True)
    img_url = db.Column(db.String(255), nullable=True)


# img_title = db.Column(db.String(100))
# published_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
# created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
# published = db.Column(db.Boolean, default=True)
# deleted = db.Column(db.Boolean, default=False)


# Creation du model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomComplet = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    telephone = db.Column(db.String(200), nullable=True, unique=True)
    password = db.Column(db.String(50), nullable=True, unique=True)

# //LES FONCTION POUR COMMUNIQUER AVEC LA BASE DE DONNEES ===============================
#
#
# LES MÉTHODES POUR USER==============================================
#
#
def saveUser(user: User):
    db.session.add(user)
    db.session.commit()


def getAllUsers():
    users = db.session.execute(db.text("select * from user"))
    # user = User.query.filter_by(lastname='fall').order_by(User.email).all()
    return users


def saveImageArticle(image: Image):
    db.session.add(image)
    db.session.commit()


# def de_activate(id_user: int):
# user = User.query.get(id_user)
#
# user.active = not user.active
#
# db.session.commit()

#
# LES MÉTHODES POUR ARTICLES==========================================
def getAllArticles(type_list=0):
    return (
        Article.query.filter(Article.deleted == type_list)
        .order_by(desc(Article.published_at))
        .all()
    )


def findAllArticles():
    articles = db.session.execute(f"select * from article")
    # articles = db.paginate(db.session.execute(db.text("select * from article")))
    # articles = db.session.execute(db.text("select * from article"))
    # user = User.query.filter_by(lastname='fall').order_by(User.email).all()
    return articles


def getArticles():  # Les articles publiés
    return (
        Article.query.filter(Article.published == 1, Article.deleted == 0)
        .order_by(desc(Article.published_at))
        .all()
    )


def findArticleById(id_article):
    # return User.query.filter(User.id == id_article).first()
    return Article.query.get(id_article)


# méthode pour récupérer les images d'un article#
def findImageArticleById(id_article):
    # return User.query.filter(User.id == id_article).first()
    image = db.session.execute(db.text(f"select * from image where article_id = {id_article}"))
    # Image.query.get(id_article)
    return image


def searchArticle(title):
    article = db.session.execute(db.text(f"SELECT * FROM article WHERE title LIKE '%{title}%'"))
    return article

def saveArticle(article: Article):
    db.session.add(article)
    db.session.commit()

# méthode pour la connexion d'un utilisateur
def findUserByTelephoneAndPassword(password):
    user = db.session.execute(db.text(f"select * from user where password = '{password}'"))
    return user
# def editArticle(article: Article):
# old_article = Article.query.get(article.id)
#
# old_article.content = article.content
# old_article.summary = article.summary
# old_article.published = article.published
# old_article.img_title = article.img_title
# old_article.img_url = article.img_url
# old_article.title = article.title
# db.session.commit()


# def un_published(id_article):
# article = Article.query.get(id_article)

# Tester si c'est une publication:
# if not article.published:
# article.published_at = datetime.datetime.utcnow()

# article.published = not article.published
# db.session.commit()


def un_delete(id_article):
    article = Article.query.get(id_article)

    article.deleted = not article.deleted
    db.session.commit()

def getAllShop():
    shops = db.session.execute(f"select * from shop")
    return shops
# Création des tables dans la base de données
# with app.app_context():
# db.create_all()
# User.__table__.drop(db.engine)
# db.drop_all().

# #
#
#
#
#
#
#
#
#
#
#
#
#
