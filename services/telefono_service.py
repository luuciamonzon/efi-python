from app import db
from repositories.telefono_repositories import TelefonoRepositories
from models import Telefono, Stock


class TelefonoService:
    def __init__(self, telefono_repository: TelefonoRepositories):
        self._telefono_repository = telefono_repository

    def get_all(self):
        return self._telefono_repository.get_all()

    def create(self, modelo, anio_fabricacion, precio, marca, tipo):
        return self._telefono_repository.create(modelo, anio_fabricacion, precio, marca, tipo)

    def get_by_id(self, id):
        return self._telefono_repository.get_by_id(id)

    def delete_with_accesorios(self, id):
        telefono = self._telefono_repository.get_by_id(id)
        
        # Reemplaza 'stocks' con 'stock'
        for stock in telefono.stock:
            stock.cantidad -= 1
            if stock.cantidad <= 0:
                db.session.delete(stock)
        
        for accesorio in telefono.accesorios:
            db.session.delete(accesorio)
        
        db.session.delete(telefono)
        db.session.commit()

    def get_accesorios_by_telefono(self, telefono_id):
        return self._telefono_repository.get_accesorios_by_telefono(telefono_id)


# Función para eliminar teléfono y actualizar stock relacionado
def delete_with_accesorios(telefono_id):
    stock_items = Stock.query.filter_by(telefono_id=telefono_id).all()
    for item in stock_items:
        item.telefono_id = None  # Asigna un nuevo telefono_id válido o elimínalo si corresponde
        db.session.add(item)

    # Elimina el teléfono
    telefono = Telefono.query.get(telefono_id)
    db.session.delete(telefono)

    db.session.commit()
