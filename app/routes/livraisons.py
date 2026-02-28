from flask import Blueprint, jsonify
from sqlalchemy import desc

from app.database import Session
from app.models.livraisons import Livraison

bp = Blueprint("livraisons",__name__)

@bp.route("/getLastId/")
def get_last_id_livraison():
    with Session() as session:
        livraison = session.query(Livraison).order_by(desc(Livraison.id)).first()
        if livraison:
            return jsonify(id=livraison.id),200
        return jsonify(id=None),200