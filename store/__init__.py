from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


store = Flask(__name__)
db = SQLAlchemy(store)
lm = LoginManager()

def create_app():
    from .views import VIEWS as views_blueprint
    store.register_blueprint(views_blueprint)
    lm.init_app(store)
    return store
