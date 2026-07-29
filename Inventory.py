from rich import print as rprint
from Product import Product
from typing import Dict
from uuid import UUID
class Inventory:
    # dex cu produse si stocul lor
    def __init__(self):
        # for now empty and private
        # key este product name (again)
        # value e Product pentru ca vrem sa fie rapid nu ca o lista
        self._inventory_dict: Dict[UUID, Product] = {}
    

    def get_full_inventory(self) -> Dict[UUID, Product] :
        print("Retrieving product list and stock...")
        return self._inventory_dict
    

    def view_full_inventory(self):
        for unique_id, product in self._inventory_dict.items():
            rprint(f"item uuid: {unique_id} -- quantity: {product.quantity}")

    
    def add_product_entry_to_inventory(self, new_product: Product):
        print(f"[DEBUG] produs unique_id:{new_product.unique_id}")
        # insert are ca prim argument o pozitie in dict
        self._inventory_dict[new_product.unique_id] = new_product
        rprint(f"[green bold] Success! Product {new_product.unique_id} has been added to inventory[/green bold]")
    
    
    # stergere produs
    def delete_product_entry_from_inventory(self, product: Product):
        """
        requires: product name as string
        action: remove product by name from inventory
        returns: just prints message
        """
        if product.unique_id not in self._inventory_dict.keys():
            # keys() retunreaza un set
            print(f"product name: {product.unique_id}")
            rprint(f"[blue bold] Warning! Product {product.unique_id} is not in inventory! [/blue bold]")
        else:
            del self._inventory_dict[product.unique_id]
            rprint(f"[green bold]Success! Product {product.unique_id} has been deleted from inventory [/green bold]")
    

    #update la stock, folosind metoda din clasa Produs
    def update_product_stock_from_inventory(self, product: Product, stock_number: int):
        """
        requires: product object, new stock number to overwrite old one
        action: overwrite current inventory with new number given as arg
        returns: just prints message
        """
        # check if product exists
        # if not just add a new entry in dict for it 
        if product.unique_id not in self._inventory_dict.keys():
            self.add_product_entry_to_inventory(product)
            # nu facem update de canttate aici , preferam control separat
        self._inventory_dict[product.unique_id].set_product_quantity(stock_number)

    
    # cresc stocul pt un anumit produs
    def increase_product_stock_from_inventory(self, product: Product, addition: int):
        """
        requires: product, how much to increase current stock with
        action: increases current stock with addition number
        returns: nothing
        """

        if addition <= 0:
            rprint("[yellow bold] [WARN] Can't increase stock with negative numbers [/yellow bold]")
        else:
            self._inventory_dict[product.unique_id].increase_product_quantity(addition)
    

    # scad stocul pt un anumit produs
    def decrease_product_stock_from_inventory(self, product: Product, decrease: int):
        self._inventory_dict[product.unique_id].decrease_product_quantity(decrease)
    
#check
# p1 = Product("produs 1",987123, "BVDA", 31, 0.21)
# p2 = Product("produs 2", 987124, "BVDA", 32, 0.21)

# inventar = Inventory()

# inventar.add_product_entry_to_inventory(p1)
# inventar.add_product_entry_to_inventory(p2)

# inventar.delete_product_entry_from_inventory(p1)

# inventar.view_full_inventory()

# inventar.update_product_stock_from_inventory(p2, 15)

# print(f"stock produs {p2.unique_id} este -- {p2.quantity}")

# inventar.decrease_product_stock_from_inventory(p2, 12)

# print(f"stock produs {p2.unique_id} este -- {p2.quantity}")

# inventar.increase_product_stock_from_inventory(p2, 4)
# print(f"stock produs {p2.unique_id} este -- {p2.quantity}")


