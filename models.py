# aici gasesti definitii de tabele deocamdata doar inventory
from database import db
from typing import Dict, Any
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer, DateTime
import datetime

# Model e Base dar e mai elegant sa il punem ca atribut
class InventoryTable(db.Model):
    # mosteneste Base
    # tablename se declara cu dunder (double underscore)
    # asa stie sqlalchemy orm ca asta e o var speciala care e numele la tabel
    __tablename__ = "inventory_table"

    # coloanele
    # Despre mapping: https://docs.sqlalchemy.org/en/21/orm/mapping_styles.html
    # in legacy mode se foloseste .Column nu o sa folosim asa ceva ci direct functie
    # arg in ordine: custom atttribute name, type, primary key flag, nullable flag (allow or not NULL)
    # tipuri de date: https://docs.sqlalchemy.org/en/21/core/type_basics.html
    # Mapped si Annotated sunt constructori generici ca in haskell 
    product_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    product_code: Mapped[str] = mapped_column(String(64))
    product_brand: Mapped[str] = mapped_column(String(64))
    product_price: Mapped[float] = mapped_column(Float)
    product_name: Mapped[str] = mapped_column(String(100), unique=True)
    # TODO: asigura-te ca nu scade sub 0
    product_quantity: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def convert_to_dict(self) -> Dict[str, Any]:
        # vezi ca e un pic diferit de ce avem noi la inventar
        # am acel updated_at 
        # TODO: adaugat updated at in clasa Inventory
        # TODO : ADAUGAT DESCRIERE PRODUSE SI FISA TEHNICA 
        return {
            "uuid": self.product_id,
            "code": self.product_code,
            "brand": self.product_brand,
            "price": self.product_price,
            "name": self.product_name,
            "quantity": self.product_quantity,
            "updated_at": self.updated_at
        }

    # ca sa dea print frumos
    def __repr__(self):
        return f"<Inventory product: {self.product_name} -- quantity: {self.product_quantity} -- price: {self.product_price}"