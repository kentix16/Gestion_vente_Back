from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.database import Session
from app.models.commandes import Produit

bp = Blueprint("produits", __name__)


@bp.route("/")
def get_produits():
    with Session() as session:
        produits = session.query(Produit).all()
        return jsonify([{"id": produit.id,"pa":produit.pa, "nom": produit.nom, "description": produit.description, "pu": produit.pu,
                         "stock": produit.stock,"validite":produit.validite} for produit in produits]), 200


@bp.route("/add", methods=["POST"])
def add_produit():
    print(request.json)
    nom = request.json.get("nom")
    description = request.json.get("description")
    pa = int(request.json.get("pa"))
    pu = int(request.json.get("pu"))
    stock = int(request.json.get("stock"))
    with Session() as session:
        produit = Produit(nom=nom, description=description,pa=pa, pu=pu, stock=stock)
        try:
            session.add(produit)
            session.commit()
            return jsonify(message="Produit ajouté avec succès"), 200
        except Exception as e:
            print(e)
            return jsonify(message="Une erreur s'est produite"), 400


@bp.route("/update", methods=["POST"])
def update_produit():
    nom = request.json.get("nom")
    description = request.json.get("description")
    pu = int(request.json.get("pu"))
    pa = int(request.json.get("pa"))
    id = int(request.json.get("id"))
    with Session() as session:
        print("nom : " + nom)
        produit = session.query(Produit).filter(Produit.id == id).first()
        produit.nom = nom
        produit.pa = pa
        produit.description = description
        produit.pu = pu
        session.commit()
        return jsonify(), 201


@bp.route("/delete", methods=["POST"])
def delete_produit():
    id = request.json.get("id")
    with Session() as session:
        try:
           produit =  session.query(Produit).filter(Produit.id == id).first()
           if produit:
               produit.validite = False
               session.commit()
               return jsonify(), 201
        except Exception as e:
            print(e)
            return jsonify(message="une erreur est survenue"), 500


@bp.route("/getLastId")
def get_last_id():
    with Session() as session:
        produit = session.query(Produit).order_by(desc(Produit.id)).first()
        return jsonify(id=produit.id), 200

@bp.route("/updateStock",methods=["POST"])
def update_stock_produit():
    id = request.json.get("id")
    updated = int(request.json.get("updated"))
    with Session() as session:
        produit=session.query(Produit).filter(Produit.id==id).first()
        if produit:
            produit.stock+=updated
            session.commit()
            return  jsonify(),201
        return jsonify(),401