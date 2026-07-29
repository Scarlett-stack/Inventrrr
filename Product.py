# imports
from uuid import UUID, uuid4
from rich import print as rprint


class Product:
    """
    Ce are un produs?
    item code = SKU ala cu bare, item_brand, price, id unic pentru baza de date (hash key ig?)
    """

    def __init__(self,item_name: str, item_code: str, item_brand: str, price: float, vat: float) -> None:
        self.item_name = item_name
        self.item_code = item_code
        self.item_brand = item_brand
        self._price = price
        self._vat = vat

        # quantity ar trebui sa fie optional il setam pe 0 inital
        self.quantity: int = 0
        # generam un id unic pentr baza de date
        # vezi : https://docs.python.org/3/library/uuid.html
        # folosim uuid4 pentru ca genereaza id unic garantat si nu foloseste info despre OS
        self.unique_id: UUID = uuid4()

        # la pret trebuie adaugata si TVA as vrea sa o fac mai flexibila
    
    # get and set pentru variabilele publice
    def get_item_name(self) -> str:
        return self.item_name
    

    def set_item_name(self, new_item_name: str) -> None:
        self.item_name = new_item_name

    # get and set for item code
    def get_item_code(self) -> str:
        return self.item_code
    

    def set_item_code(self, new_item_code: str) -> None:
        self.item_code = new_item_code
    

    # get and set for item brand
    def get_item_brand(self) -> str:
        return self.item_brand
    

    def set_item_brand(self, new_item_brand: str) -> None:
        self.item_brand = new_item_brand

    # getters setters for VAT
    def get_vat(self) -> float:
        return self._vat
        
    def set_vat(self, vat: float) -> None:
        self._vat = vat
        

    vat = property(get_vat, set_vat)

    # price setters
    def get_price(self) -> float:
        print("get price from property:")
        return self._price
        
    def set_price(self, price: float) -> None:
        print("set price from proerty:")
        self._price = price + price*self._vat
            

    def delete_value(self) -> None:
        # risky poate intoarce Null?
        print("delete price:")
        del self._price
        
    # folosim property, ca sa nu stam sa scriem get , set , de 7 mii de ori
    price = property(get_price, set_price, delete_value)

    # quantity setters
    def get_product_quantity(self):
        print(f"Retrieving quantity for product {self.item_name}")
        return self.quantity
    
    # overwrite existing product stock numbers
    def set_product_quantity(self, new_quantity: int) -> None:
        self.quantity = new_quantity
    
    # add to exisiting product stock numbers
    def increase_product_quantity(self, new_quantity: int) -> None:
        self.quantity += new_quantity
    

    # decrease existing quantity
    def decrease_product_quantity(self, decreased_quantity: int) -> None:
        if decreased_quantity > self.quantity:
            rprint(f"[red bold] [ERROR] cannot decrease from curret stock not enough products available! [/red bold]")
        else:
            self.quantity -= decreased_quantity
    
    # property's arguments are getx, setx, delx and a doc string.
    # nu e corect ce aic:
    # quantity = property(get_product_quantity, set_product_quantity, increase_product_qauntity, decrease_product_quantity)
        

# produs1 = Product(987123, "BVDA", 31, 0.21)
# print(produs1.item_brand, produs1.unique_id, produs1.item_code, produs1._price, produs1._vat)
# produs1.price = 21 # trebuie setat fara scor gen fix variabila aia atribuita cu propery
# print(produs1._price)

    
