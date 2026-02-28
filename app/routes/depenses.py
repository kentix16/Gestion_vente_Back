from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.database import Session
from app.models.transactions import Transaction, Mode

bp = Blueprint("depenses", __name__)


@bp.route("/depenses/")
def get_depenses():
    with Session() as session:
        depenses = session.query(Transaction).filter(Transaction.type=='DEPENSE').all()
        return jsonify([{"id": depense.id,
                         "date": depense.date.isoformat(),
                         "motif": depense.motif,
                         "montant": depense.montant,
                         "id_mode":depense.id_mode,
                         } for depense in depenses]), 200



@bp.route('/depenses/add/', methods=["POST"])
def add_depense():
    motif = request.json.get("motif")
    montant = int(request.json.get("montant"))
    mode = request.json.get("mode").get("valeur")
    with Session() as session:
        mode = session.query(Mode).filter(Mode.valeur==mode).first()
        depense = Transaction(motif=motif, montant=montant, type="DEPENSE",mode=mode)
        session.add(depense)
        session.commit()
        return jsonify(), 201


@bp.route("/depenses/getLastId/")
def get_last_id():
    with Session() as session:
        depense = session.query(Transaction).order_by(desc(Transaction.id)).first()
        return jsonify({'id': depense.id, 'date': depense.date.isoformat(),"id_mode":depense.id_mode}), 200

@bp.route("/depenses/update/",methods=["POST"])
def update_depense():
    id = int(request.json.get("id"))
    motif = request.json.get("motif")
    montant = int(request.json.get("montant"))
    with Session() as session:
        depense = session.query(Transaction).filter(Transaction.id==id,Transaction.type=='DEPENSE').first()
        if depense:
            depense.motif = motif
            depense.montant = montant
            session.commit()
            return jsonify(),201


@bp.route("/depenses/delete/", methods=["POST"])
def delete_depense():
    id = int(request.json.get("id"))
    with Session() as session:
        depense = session.query(Transaction).filter(Transaction.id == id,Transaction.type=='DEPENSE').first()
        if depense:
            session.delete(depense)
            session.commit()
            return jsonify(), 201
        return jsonify(), 401

