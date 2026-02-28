from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import DATABASE_URL


Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
from sqlalchemy import event
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

Session = sessionmaker(bind=engine)

def init_db():
    from app.models.commandes import Commande,Produit,Adresse_Mac
    from app.models.livraisons import Livraison,Livreur
    from app.models.transactions import Transaction
    Base.metadata.create_all(bind=engine)
import os, sys

