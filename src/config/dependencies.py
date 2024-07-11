from fastapi import Depends, Header
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.repository.usuario_repository import ProductRepository
from src.service.auth_service import AuthService
from src.service.product_service import ProductService

auth_service = AuthService()


def get_authenticated_user(authorization: str = Header(alias='Authorization')) -> ProductRepository:
    return auth_service.validate_token(authorization)


def get_product_repository(session: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db=session)


def get_product_service(repository: ProductRepository = Depends(get_product_repository)) -> ProductService:
    return ProductService(repository)
