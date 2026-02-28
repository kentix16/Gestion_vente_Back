from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.database import Session
from app.models.transactions import Mode

bp = Blueprint("modes", __name__)


@bp.route("/")
def get_modes():
    with Session() as session:
        modes = session.query(Mode).all()
        return jsonify([{"id": mode.id, "valeur": mode.valeur, "validite": mode.validite} for mode in modes])


@bp.route("/add", methods=["POST"])
def add_mode():
    valeur = request.json.get("valeur")
    with Session() as session:
        mode = session.query(Mode).filter(Mode.valeur == valeur).first()
        if mode: return jsonify(), 400
        mode = Mode(valeur=valeur)
        session.add(mode)
        session.commit()
        return jsonify(), 201


@bp.route("/getLastId")
def get_last_id_mode():
    with Session() as session:
        mode = session.query(Mode).order_by(desc(Mode.id)).first()
        if mode:
            return jsonify({"id": mode.id}), 200


@bp.route("/delete",methods=["POST"])
def delete_mode():
    id = int(request.json.get("id"))
    with Session() as session:
        mode = session.query(Mode).filter(Mode.id == id).first()
        if mode:
            mode.validite=False
            session.commit()
            return jsonify(), 201

@bp.route("/update", methods=["POST"])
def update_mode():
    valeur = request.json.get("valeur")
    id = int(request.json.get("id"))
    with Session() as session:
        mode = session.query(Mode).filter(Mode.id==id).first()
        mode_same_valeur = session.query(Mode).filter(Mode.valeur==valeur).first()
        if mode_same_valeur:
            mode_same_valeur.valeur = mode_same_valeur.valeur + "(Supprimé)"
            session.commit()
        if mode :
            mode.valeur=  valeur
            session.commit()
            return jsonify(),201
        return jsonify(message="Erreur"),500



