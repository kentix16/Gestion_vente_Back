import datetime

from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from app.database import Session
from app.models.commandes import Commande, Produit
from app.models.transactions import Mode

bp = Blueprint("commandes", __name__)


@bp.route("/")
def get_commandes():
    with Session() as session:
        commandes = session.query(Commande).all()
        datas = []
        for commande in commandes:
            data = {"id": commande.id,
                         "nom_client": commande.nom_client,
                         "date": commande.date.isoformat(),
                         "heure": commande.heure.strftime("%H:%M"),
                         "correspondance": commande.correspondance,
                         "id_produit": commande.id_produit,
                         "pu": commande.pu,
                         "quantite": commande.quantite,
                         "id_mode": commande.id_mode,
                         "total": commande.total,
                         "paye":commande.paye}
            if commande.livraison:
                livraison = commande.livraison
                data["livraison"]={
                    "id":livraison.id,
                    "frais":livraison.frais,
                    "livreur":{"id":livraison.livreur.id,"nom":livraison.livreur.nom}
                }
            datas.append(data)
        return jsonify(datas),201


@bp.route("/add", methods=["POST"])
def add_commande():
    print("requests : " + str(request.json))
    with Session() as session:
        nom_client = request.json.get("nom_client")
        correspondance = request.json.get("correspondance")
        id_produit = int(request.json.get("produit").get("id"))
        pu = int(request.json.get("pu"))
        quantite = int(request.json.get("quantite"))
        total = int(request.json.get("total"))
        id_mode = int(request.json.get("mode").get("id"))
        paye = bool(request.json.get("paye"))
        print("Paye :"+str(paye))
        commande = Commande(nom_client=nom_client,
                            correspondance=correspondance,
                            produit=session.query(Produit).filter(Produit.id == id_produit).first(),
                            pu=pu,
                            quantite=quantite,
                            total=total,
                            mode=session.query(Mode).filter(Mode.id == id_mode).first(),
                            paye=paye
                            )
        session.add(commande)
        session.commit()
        return jsonify(), 201


@bp.route("/getLastId")
def getLastId_commande():
    with Session() as session:
        commande = session.query(Commande).order_by(desc(Commande.id)).first()
        return jsonify({"id": commande.id,
                        "nom_client": commande.nom_client,
                        "date": commande.date.isoformat(),
                        "heure": commande.heure.strftime("%H:%M"),
                        "correspondance": commande.correspondance,
                        "aLivrer": commande.alivrer,
                        "id_produit": commande.id_produit,
                        "pu": commande.pu,
                        "quantite": commande.quantite,
                        "total": commande.total,
                        "id_mode":commande.id_mode,
                        })


@bp.route("/update", methods=["POST"])
def update_commande():
    id = int(request.json.get("id"))
    nom_client = request.json.get("nom_client")
    correspondance = request.json.get("correspondance")
    id_produit = int(request.json.get("produit").get("id"))
    pu = int(request.json.get("pu"))
    quantite = int(request.json.get("quantite"))
    total = int(request.json.get("total"))
    id_mode = int(request.json.get("mode").get("id"))
    paye = int(request.json.get("paye"))
    with Session() as session:
        commande = session.query(Commande).filter(Commande.id == id).first()
        if commande:
            commande.nom_client = nom_client
            commande.correspondance = correspondance
            commande.id_produit = id_produit
            commande.pu = pu
            commande.quantite = quantite
            commande.total = total
            commande.id_mode=id_mode
            commande.paye = bool(paye)
            print(bool(paye))
            session.commit()
            return jsonify(), 201
        return jsonify(), 500


@bp.route("/delete", methods=["POST"])
def delete_commande():
    id = int(request.json.get("id"))
    with Session() as session:
        commande = session.query(Commande).filter(Commande.id == id).first()
        session.delete(commande)
        session.commit()
        return jsonify(), 201
