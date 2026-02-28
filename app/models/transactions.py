import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer,primary_key=True)
    motif = Column(String,nullable=False)
    type = Column(String, nullable=False)
    id_mode = Column(Integer,ForeignKey("modes.id"))
    montant = Column(Integer,nullable=False)
    date = Column(Date, default=datetime.date.today())
    mode = relationship("Mode",back_populates="transactions")

class Mode(Base):
    __tablename__ = "modes"
    id = Column(Integer, primary_key=True)
    valeur = Column(String, nullable=True, unique=True)
    validite = Column(Boolean,default=True)
    transactions = relationship("Transaction",back_populates="mode")
    commandes = relationship("Commande",back_populates="mode")
