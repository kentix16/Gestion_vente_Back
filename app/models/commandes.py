import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean, UniqueConstraint, Table, Time
from sqlalchemy.orm import relationship

from app.database import Base

class Produit(Base):
    __tablename__ = "produits"
    id = Column(Integer,primary_key=True)
    nom = Column(String,nullable=False,index=True,unique=True)
    description = Column(String,nullable=True)
    pa = Column(Integer)
    pu = Column(Integer,nullable=False)
    stock = Column(Integer)
    validite = Column(Boolean,default=True)
    commandes = relationship("Commande",back_populates="produit")


class Commande(Base):
    __tablename__ = "commandes"
    id = Column(Integer, primary_key=True)
    nom_client = Column(String,nullable=True)
    correspondance = Column(String)
    id_produit = Column(Integer,ForeignKey("produits.id"))
    pu = Column(Integer)
    quantite = Column(Integer,default=1)
    total = Column(Integer, nullable=False)
    date = Column(Date,default=datetime.date.today())
    heure =Column(Time,nullable=True,default=datetime.datetime.now().time())
    alivrer = Column(Boolean,default=False)
    id_mode = Column(Integer, ForeignKey("modes.id"))
    paye = Column(Boolean,default=False)
    note = Column(String, nullable=True)
    produit = relationship("Produit",back_populates="commandes")
    livraison = relationship("Livraison",back_populates="commande",uselist=False)
    mode = relationship("Mode",back_populates="commandes")




class Adresse_Mac(Base):
    __tablename__='adresse_mac'
    id = Column(Integer,primary_key=True)
    value = Column(String)






