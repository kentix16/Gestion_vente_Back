from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.database import Session
from app.models.livraisons import Livreur

bp = Blueprint("livreurs", __name__)


@bp.route("/")
def get_livreurs():
    with Session() as session:
        livreurs = session.query(Livreur).all()
        return jsonify(
            [{"id": livreur.id, "nom": livreur.nom, "validite": livreur.validite} for livreur in livreurs])


@bp.route("/add", methods=["POST"])
def add_livreur():
    nom = request.json.get("nom")
    with Session() as session:
        livreur = session.query(Livreur).filter(Livreur.nom == nom).first()
        if livreur: return jsonify(), 400
        livreur = Livreur(nom=nom)
        session.add(livreur)
        session.commit()
        return jsonify(), 201


@bp.route("/getLastId")
def get_last_livreur():
    with Session() as session:
        livreur = session.query(Livreur).order_by(desc(Livreur.id)).first()
        if livreur:
            return jsonify({"id": livreur.id}), 200


@bp.route("/delete", methods=["POST"])
def delete_livreur():
    id = int(request.json.get("id"))
    with Session() as session:
        livreur = session.query(Livreur).filter(Livreur.id == id).first()
        if livreur:
            livreur.validite = False
            session.commit()
            return jsonify(), 201


@bp.route("/update", methods=["POST"])
def update_livreur():
    nom = request.json.get("nom")
    id = int(request.json.get("id"))
    with Session() as session:
        livreur = session.query(Livreur).filter(Livreur.id == id).first()
        livreur_same_nom = session.query(Livreur).filter(Livreur.nom == nom).first()
        if livreur_same_nom:
            livreur_same_nom.valeur = livreur_same_nom.nom + "(Supprimé)"
            session.commit()
        if livreur:
            livreur.nom = nom
            session.commit()
            return jsonify(), 201
        return jsonify(message="Erreur"), 500
