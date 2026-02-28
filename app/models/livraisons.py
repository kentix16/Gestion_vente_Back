from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Livraison(Base):
    __tablename__ = "livraisons"
    id = Column(Integer, primary_key=True)
    frais = Column(Integer)
    adresse = Column(String)
    id_commande = Column(Integer,ForeignKey("commandes.id"))
    id_livreur = Column(Integer,ForeignKey("livreurs.id"))
    commande = relationship("Commande",back_populates="livraison")
    livreur = relationship("Livreur",back_populates="livraisons")


class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String,unique=True,nullable=False)
    validite = Column(Boolean, default=True)
    livraisons = relationship("Livraison",back_populates="livreur")


