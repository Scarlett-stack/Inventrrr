from csv import Error
from itertools import product
import profile
import datetime
import os
from tokenize import String

from flask import Flask, render_template, request, url_for
from database import db, init_db, create_tables, get_database_url
from decouple import config
from models import InventoryTable
from Product import Product
from Inventory import Inventory

from forms.ProductForm import ProductForm


# testare db
app = Flask(__name__)

# config csrf secret key wtf forms
SECRET_KEY: str = os.urandom(32)
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

# BULLSHIT TRB SCOASA SAU FACUTA CA LUMEA
# @app.errorhandler(Exception)
# def handle_exception(err: Error):
#     path=request.path
#     return path


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
    # TODO : refacut cu formular ca lumea  DONE
    # TODO : adaugat template pentru pagina asta DONE
    form = ProductForm()
    # declaram un obiect de tip Product fix cum am randurile in db
    # si pun campurile din Product accesate prin form
    # si asa adaug la db

    if form.validate_on_submit():
        product = Product(
                 form.product_name.data,
                 form.product_code.data,
                 form.product_brand.data,
                 form.product_price.data,
                 vat=0.21
            )

        product_for_db = InventoryTable(
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
        # TODO repara redirectul asta ca afiseaza doar / dupa submit
        return url_for("about") # primeste numele functiei

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



# tinem aplicatia in runnning
if __name__=="__main__":
    app.run(debug=True)