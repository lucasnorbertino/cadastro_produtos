from fastapi import APIRouter, Depends

from src.config.dependencies import get_authenticated_user, get_product_service
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO

from src.service.auth_service import AuthService
from src.service.product_service import ProductService

product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])

auth_service = AuthService()

# TO DO: utilizar as anotações adequadamente
# async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
#     return service.create(request)

@product_router.post('/', status_code=201, description='Criar um novo produto', response_model=ProdutoDTO)
async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
    return service.create(request)

# TO DO: implementar método para buscar produto por ID
# async def find_by_id(user_id: int, service: ProductService = Depends(get_product_service)):
#     return service.find_by_id(user_id=user_id)

@product_router.get('/{prod_id}', status_code=200, description='Buscar produto por ID', response_model=ProdutoDTO)
async def find_by_id(prod_id: int, service: ProductService = Depends(get_product_service)):
    return service.find_by_id(prod_id=prod_id)

# TO DO: implementar método para buscar todos os produtos
# async def find_all(service: ProductService = Depends(get_product_service)):
#     return service.find_all()

@product_router.get('/', status_code=200, description='Buscar todos os produtos', response_model=list[ProdutoDTO])
async def find_all(service: ProductService = Depends(get_product_service)):
    return service.find_all()

# TO DO: implementar método para atualizar produto
# async def update(user_id: int, user_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
#     return service.update(user_id, user_data)

@product_router.put('/{prod_id}', status_code=200, description='Atualizar um produto', response_model=ProdutoDTO)
async def find_by_id(prod_id: int, prod_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
    return service.update(prod_id, prod_data)

# TO DO: implementar método para deletar produto
# async def delete(user_id: int, service: ProductService = Depends(get_product_service)):
#     service.delete(user_id=user_id)

@product_router.delete('/{prod_id}', status_code=204, description='Deletar um produto')
async def find_by_id(prod_id: int, service: ProductService = Depends(get_product_service)):
    service.delete(prod_id=prod_id)