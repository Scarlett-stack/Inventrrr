# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

# noi folosim o extensie speciala pt flask a lui sql alchemy 
# altfel ar fi fost cam naspa codul
# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#installation


# declaram metaclasa pe care o folosim
# ideea e ca e un fel de sablon pt sqlalchemy
class Base(DeclarativeBase):
    # aici se pot defini chestii valabile pt toate tabelele din db
    # gen format de nume, metode comune, metadate ca gen engine stocare sql etc
    # deocamdata lasam asa
    # https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#native-support-for-dataclasses-mapped-as-orm-models
    pass

db = SQLAlchemy(model_class=Base)

# definim metode pentru a le apela in contextul instantei de flask pe obiectul db

def init_db(app: Flask):
    # init db cu aplicatia flask
    db.init_app(app)


def create_tables():
    # creaza tabelele din bd
    db.create_all()


def get_database_url():
    # pentru folosiri ulterioare
    # getenv are optiune 2 ca default in caz ca variabila data ca arg nu exista
    return os.getenv(
        "DATABASE_URL",
        "postgresql://localhost/inventory_db"
    )


