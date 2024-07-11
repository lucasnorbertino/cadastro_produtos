from sqlalchemy.orm import Session

from src.domain.model.models import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()

    def read(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def find_all(self):
        return self.db.query(Product).all()
