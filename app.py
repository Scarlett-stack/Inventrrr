from csv import Error
from itertools import product
import profile
import datetime
import os
from statistics import quantiles
from tokenize import String
from sqlalchemy import select, delete, update
from sqlalchemy.sql.expression import Update

from flask import Flask, redirect, render_template, request, url_for
from database import db, init_db, create_tables, get_database_url
from decouple import config
from models import InventoryTable
from Product import Product
from Inventory import Inventory

from forms.ProductForm import ProductForm


# testare db
app = Flask(__name__)

# config csrf secret key wtf forms
SECRET_KEY: bytes = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# config sqlite database
# trebuie ghilimele in arg de la config
app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URI")
# app trebuie sa stie la ce baza de date din memorie se conecteaza
# baza de date trebuie creata in terminalul de la postgres
# init db
init_db(app)

with app.app_context():
    create_tables()

global_inventory = Inventory()

# [] TODO : Proper error handling
# BULLSHIT TRB SCOASA SAU FACUTA CA LUMEA
# @app.errorhandler(Exception)
# def handle_exception(err: Error):
#     path=request.path
#     return path

def update_global_inventory(product_id, action):
    """
    requires: uuid4 as product id, a string aka action with possible values being: delete, update, insert, overwrite
    action: updates the globally available dictionary of the inventory database
    returns: nothing
    """
    global global_inventory
    # daca sterg din db?
    # daca adaug in db? 
    # daca editez in db?
    # are sens sa fac copiere la toata baza de date?
    # NU ARE SENS. Daca ai nevoie de un dictionar pt toata baza de date il copiem direct on demand
    # deocamdata nu il folosim nocaieri si ce avem nevoie putem extrage direct din db
    # [] TODO: evaluate necessity of additional global inventory Inventory type object
    pass


@app.route("/")
def about():
    # flask intra in templates automat
    # daca ii dai templates/about.html m el cauta templates/templates/..
    return render_template("about.html")

@app.route("/hello_test")
def hello_test():
    return "<p>Merge frate</p>"

@app.route("/get-products", methods=["GET"])
def get_products():
    # aceste listinguri trebuie puse in templates iar fisierel css trebuie puse in static
    # https://www.reddit.com/r/flask/comments/4f80qp/comment/d26okyk/
    # ok acum zice Type Error
    # stakc zice ca e la return buba?
    products = db.session.execute(db.select(InventoryTable).order_by(InventoryTable.product_name)).scalars().all()
    print("PRODUSE")
    print(products)
    # asta cauti
    # https://flask-sqlalchemy.readthedocs.io/en/stable/queries/
    return render_template("get_products_listing.html.jinja", inventory=products)


@app.route("/product/add", methods=["GET", "POST"])
def add_product():
    # TODO [x]: refacut cu formular ca lumea  DONE
    # TODO [x] : adaugat template pentru pagina asta DONE
    form = ProductForm()
    # declaram un obiect de tip Product fix cum am randurile in db
    # si pun campurile din Product accesate prin form
    # si asa adaug la db

    # TODO [] : Change if logic to avoid str | None pylance error
    if form.validate_on_submit():
        product = Product(
                form.product_name.data,
                form.product_code.data,
                form.product_brand.data,
                form.product_price.data,
                vat=0.21
            )

        product_for_db = InventoryTable(
                # converteste automat la string
                product_id = product.unique_id,
                product_code = product.item_code,
                product_brand = product.item_brand,
                product_price = product.price,
                product_name = product.item_name,
                product_quantity = form.product_quantity.data
            )

        global_inventory.add_product_entry_to_inventory(product)
        db.session.add(product_for_db)
        db.session.commit()
        # TODO [x] repara redirectul asta ca afiseaza doar / dupa submit
        # fiind ca e values tip any e arg pozitional adica trb nume=val in apel
        # de asemenea trebuie dat urlul la redirect altfel iti afoseaza direct linkul!
        return redirect(url_for("success_product_add", product_id=product.unique_id))
        # primeste numele functiei

    # fallback intaorce din nou formularul
    # si e si ce se afoseaza prima data inaine de a completa
    return render_template("add-product-template.html.jinja", form=form)
    
    # product1: Product = Product("pulbere", "898011", "bvda", 31.99, 0.21)
    # print("dEBUG!!")
    # product_for_db: InventoryTable = InventoryTable(
    #     product_id = product1.unique_id,
    #     product_code = product1.item_code,
    #     product_brand = product1.item_brand,
    #     product_price = product1.price,
    #     product_name = product1.item_name,
    #     product_quantity = 50,
    #     updated_at= datetime.datetime.now()
    # )
    # print(f"din add prodcut: {global_inventory.__sizeof__()}")
    # global_inventory.add_product_entry_to_inventory(product1)
    # db.session.add(product_for_db)
    # db.session.commit()

@app.route("/success/<string:product_id>")
def success_product_add(product_id: str):
    # se aplica pe baza de date postgres
    # parametrul e cheia primara
    # exista si metoda get , asta cu 404 da abort imediat ce primeste 404
    product: InventoryTable = InventoryTable.query.get_or_404(product_id)
    # facem template 
    return f'Product {product.product_id} {product.product_name} added succesfuly'


# nu toat ebrowserele suporta delete simplu si nici put
# cel mai sigur e sa faci cu post, e un pic counterintuitive dar ar trb sa mearga
# cel mai corect e sa faci cu ajax sau jquery yucks
# https://stackoverflow.com/questions/61506681/python-flask-delete-request
# https://stackoverflow.com/questions/2392922/what-is-wrong-with-using-get-to-remove-content
# nu folosim get, este ceva cu crawlere care pot face get si sa iti stearga produsele 

@app.route("/products/<string:product_id>", methods=['POST'])
def delete_product(product_id):
    # primim id adica cheia primara
    # selectam dupa cheia primara
    # https://docs.sqlalchemy.org/en/21/tutorial/data_select.html
    """
    To SELECT from individual columns using a Core approach, Column objects are 
    accessed from the Table.c accessor and can be sent directly; 
    the FROM clause will be inferred as the set of all Table and other 
    FromClause objects that are represented by those columns:
    """
    # oricum nu trebuie sa facem select inainte putem da delete direct
    # in sql daca iti aduci aminte de la bd
    # ai delete , drop si truncate
    # www.datacamp.com/tutorial/sql-delete?utm_cid=23340058068&utm_aid=192632749329&utm_campaign=230119_1-ps-dscia~dsa-tofu~sql_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9226348-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~emea-en~dsa~tofu~tutorial~sql&gad_source=1&gad_campaignid=23340058068&gclid=Cj0KCQjw4orUBhCjARIsAIbF3qx1tLkXv0fWseJgvWOAQo5RElEOFOSlqmACn0MNYhwuLSj4cEiV7gsaAob0EALw_wcB
    # dam delete ca sa stergem randul respectiv 
    # stmt_select = select(InventoryTable).filter_by(product_id=product_id)
    # stmt_delete = delete(InventoryTable).where(InventoryTable.c.product_id == product_id)
    # .c se folosete doar la tabelele sql core (Table) nu de tip ORM (db.Model)! 

    # * IMPORTANT  https://flask-sqlalchemy.readthedocs.io/en/stable/models/
    # la tine uuid e string in db
    db.session.execute(db.delete(InventoryTable).where(InventoryTable.product_id == product_id))
    db.session.commit()

    return redirect(url_for("get_products"))

    # trebuie scos si din global inventory?

    # pentru a modifica in frontend ne ducem in teplateul de jinja care afis
    # toate produsele
    # https://stackoverflow.com/questions/51514488/python-flask-pass-jinja-variable-to-backend
    # trash button: https://stackoverflow.com/questions/67327422/delete-row-from-html-table-on-icon-click-using-flask-python-and-sqlite
    # din pacatae trb ajax sau bootstrap abandonam lasam pt siteul main asta


@app.route("/update/<string:product_id>", methods=["POST"])
def update_product(product_id: str):
    # TODO de terminat logica update inplace din tabel
    # update server side
    # update in place
    # uite cum face cu statment: https://docs.sqlalchemy.org/en/21/tutorial/orm_related_objects.html
    # oareputem face un updte mai desteot adica doar pe campurile schimbate?
    # SAU putem sa facem cate o metoda de update pt fiecare camp din formular?
    # de semenea pylance se supara ca nu faci validare de input aici
    # daia zice ca nu poti converti float| none la float
    # TODO [] add field validation logic in update function
    product_name: str = str(request.form.get("product_name"))
    product_brand: str = str(request.form.get("product_brand"))
    product_price: float = float(request.form.get("product_price"))
    product_quantity: int = int(request.form.get("product_quantity"))
    product_code: str = str(request.form.get("product_code"))

    # more about statements:
    # https://docs.sqlalchemy.org/en/21/tutorial/data_update.html#the-update-sql-expression-construct
    stmt: Update = (
        update(InventoryTable)
        .where(InventoryTable.product_id == product_id)
        .values(
            product_code = product_code,
            product_brand = product_brand,
            product_price = product_price,
            product_name = product_name,
            product_quantity = product_quantity
        )
    )

    db.session.execute(stmt)

    # updated at ar trb sa se bage pe default deci sa se updateze automat?
    db.session.commit()
    # deci daca apelam functia direct o sa fie ceva dubios la refresh
    # in sesnul ca se pot pierde datele din formular
    # de aia facem render template again
    return redirect(url_for("get_products"))



# tinem aplicatia in runnning
if __name__=="__main__":
    app.run(debug=True)