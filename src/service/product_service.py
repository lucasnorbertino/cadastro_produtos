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
        prod = Product(**data.model_dump())
        try:
            created = self.repository.save(prod)
            return TypeAdapter(ProdutoDTO).validate_python(created)
        except IntegrityError as e:
            logger.error(f'Erro ao criar o produto: {data.model_dump()}')
            raise HTTPException(status_code=409, detail=f'Produto já existe na base: {e.args[0]}')

    def _read(self, prod_id: int) -> Product:
        prod = self.repository.read(prod_id)
        if prod is None:
            logger.error(f'Produto {prod_id} não encontrado.')
            raise HTTPException(status_code=404, detail=f'Produto {prod_id} não encontrado.')
        return prod

    def find_by_id(self, prod_id: int) -> ProdutoDTO:
        logger.info(f'Buscando produto com ID {prod_id}')
        return TypeAdapter(ProdutoDTO).validate_python(self._read(prod_id))

    def find_all(self) -> list[ProdutoDTO]:
        logger.info('Buscando todos os produtos')
        produtos = self.repository.find_all()
        return [TypeAdapter(ProdutoDTO).validate_python(prod) for prod in produtos]

    def update(self, prod_id: int, prod_data: ProdutoUpdateDTO) -> ProdutoDTO:
        logger.info(f'Atualizando produto com ID {prod_id}')
        prod = self._read(prod_id)
        prod_data = prod_data.model_dump(exclude_unset=True)
        for key, value in prod_data.items():
            setattr(prod, key, value)
        prod_updated = self.repository.save(prod)
        logger.info(f'Produto {prod_id} atualizado: {prod_updated}')
        return TypeAdapter(ProdutoDTO).validate_python(prod_updated)

    def delete(self, prod_id: int) -> int:
        logger.info(f'Deletando produto com ID {prod_id}')
        prod = self._read(prod_id)
        self.repository.delete(prod)
        logger.info(f'Produto {prod_id} deletado.')
        return prod_id