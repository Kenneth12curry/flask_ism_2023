import os

APP_NAME = "Expat-Dakar"

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "expat.sqlite")

SECRET_KEY = "WriteHereYourSecretKey"
