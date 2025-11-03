class Product():
    def __init__(self,name,category,price,quantity,available=False):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.available=available

    def update_product(self,name=None,category=None,price=None,quantity=None):
        if name:
            self.name=name
        if category:
            self.category=category
        if category:
            self.price=price
        if category:
            self.quantity=quantity
        
        return f"Articulo {self.name} actualizado."
    
    def mark_unvailable(self):
        self.available=True
        return f"Articulo {self.name} marcado como no disponible."

    def __str__(self):
        return f"Nombre: {self.name} || Categoria: {self.category} \n Precio{self.price} \n Cantidad: {self.quantity}    Disponibilidad:{self.available} \n================================================= "


    @staticmethod
    def to_dict(self):
        return {
        "name": self.name,
        "category":self.category,
        "price": self.price,
        "quantity": self.quantity,
        "available": self.available
        }
        
    def from_dict(data):
        return Product(data.get("name"),
                        data.get("category"),
                        data.get("price"),
                        data.get("quantity"),
                        data.get("available")
                    )
        
        
class InventoryManager():