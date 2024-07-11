from fastapi import APIRouter, status, Header

from src.domain.dto.dtos import TokenResponse
from src.service.auth_service import AuthService

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

auth_service = AuthService()


@auth_router.post('/token', status_code=status.HTTP_201_CREATED, response_model=TokenResponse)
async def get_token(secret: str = Header(alias="secret")):
    return auth_service.create_access_token(secret_key=secret)


@auth_router.get('/validate', status_code=status.HTTP_200_OK)
async def validate(authorization: str = Header(alias='Authorization')):
    return auth_service.validate_token(authorization)
