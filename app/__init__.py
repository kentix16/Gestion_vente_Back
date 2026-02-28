from flask import Flask
from app.database import init_db
from app.routes import produits, depenses, modes,commandes,livreurs,livraisons


def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(produits.bp,url_prefix="/produits")
    app.register_blueprint(depenses.bp, url_prefix="/transactions")
    app.register_blueprint(modes.bp, url_prefix="/modes")
    app.register_blueprint(commandes.bp, url_prefix="/commandes")
    app.register_blueprint(livreurs.bp, url_prefix="/livreurs")
    app.register_blueprint(livraisons.bp, url_prefix="/livraisons")

    return app

