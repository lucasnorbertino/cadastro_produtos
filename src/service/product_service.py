import logging
from sqlalchemy.exc import IntegrityError
from pydantic import TypeAdapter
from fastapi import HTTPException
from src.domain.model.models import Product
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
from src.repository.usuario_repository import ProductRepository

logger = logging.getLogger('fastapi')

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create(self, data: ProdutoCreateDTO) -> ProdutoDTO:
        logger.info('Criando produto')
        user = Product(**data.model_dump())
        try:
            created = self.usuario_repository.save(user)
            return TypeAdapter(ProdutoDTO).validate_python(created)
        except IntegrityError as e:
            logger.error(f'Erro ao criar o produto: {data.model_dump()}')
            raise HTTPException(status_code=409, detail=f'Produto já existe na base: {e.args[0]}')

    def _read(self, user_id: int) -> Product:
        prod = self.usuario_repository.read(user_id)
        if prod is None:
            self.logger.error(f'Produto {user_id} não encontrado.')
            raise HTTPException(status_code=404, detail=f'Produto {user_id} não encontrado.')
        return prod

    def find_by_id(self, user_id: int) -> ProdutoDTO:
        logger.info(f'Buscando produto com ID {user_id}')
        return TypeAdapter(ProdutoDTO).validate_python(self._read(user_id))

    def find_all(self) -> list[ProdutoDTO]:
        logger.info('Buscando todos os usuarios')
        produtos = self.usuario_repository.find_all()
        return [TypeAdapter(ProdutoDTO).validate_python(prod) for prod in produtos]

    def update(self, user_id: int, prod_data: ProdutoUpdateDTO) -> ProdutoDTO:
        logger.info(f'Atualizando produto com ID {user_id}')
        prod = self._read(user_id)
        prod_data = prod_data.model_dump(exclude_unset=True)
        for key, value in prod_data.items():
            setattr(prod, key, value)
        prod_updated = self.usuario_repository.save(prod)
        logger.info(f'Produto {user_id} atualizado: {prod_updated}')
        return TypeAdapter(ProdutoDTO).validate_python(prod_updated)

    def delete(self, user_id: int) -> int:
        logger.info(f'Deletando produto com ID {user_id}')
        prod = self._read(user_id)
        self.usuario_repository.delete(prod)
        logger.info(f'Produto {user_id} deletado.')
        return user_id