# API de Cadastro de Produtos

## Descrição

Esta API é destinada ao cadastro e gerenciamento de produtos. 

A estrutura inicial, incluindo a modelagem, os DTOs, autenticação e logs, já está pronta. 

Os alunos serão responsáveis por implementar os services e anotar os controllers para completar a funcionalidade da API.


## Tarefas dos Alunos

### Controllers

Os alunos devem anotar os métodos da API em `controller/product_controller.py`. Os métodos esperados são:

- `POST /products`: Criar um novo produto
- `GET /products/{id}`: Obter um produto pelo ID
- `GET /products`: Listar todos os produtos
- `PUT /products/{id}`: Atualizar um produto existente
- `DELETE /products/{id}`: Deletar um produto

### Services

Os alunos devem implementar a lógica de negócios e interação com o banco de dados em `service/product_service.py`. As funções esperadas são:

- `create(data: ProdutoCreateDTO) -> ProdutoDTO`: Criar um novo produto
- `find_by_id(user_id: int) -> ProdutoDTO`: Retornar um produto pelo ID
- `find_all() -> list[ProdutoDTO]`: Retornar todos os produtos
- `update(user_id: int, user_data: ProdutoUpdateDTO) -> ProdutoDTO`: Atualizar um produto existente
- `delete(user_id: int) -> int`: Deletar um produto


Para fazer essa atividade é necessário fazer um fork ou criar um novo repositório.