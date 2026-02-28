import requests

from app.config import url_base


def init_modes():
    requests.post(url_base+"/modes/add",json={"valeur":"Espèce"})
def init_commandes():
    requests.post(url_base+"/commandes/add",json={"nom_client":"RAKOTOSON Ekena","correspondance":"028 66 147 70","produit":"ELM","pu":25000,"quantite":1,"total":25000})
def init_produit():
    requests.post(url_base+"/produits/add" ,json={"nom":"ELM","pa":25000,"pu":35000,"stock":3})
init_modes()