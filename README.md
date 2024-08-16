# Microservice Energy

## Visão Geral

Este projeto é um sistema de gerenciamento de fornecedores de energia que permite aos usuários informar seu consumo mensal de energia e escolher o fornecedor mais adequado. O backend é construído com Django e o frontend com React. O sistema utiliza GraphQL para consultas e integrações com o banco de dados PostgreSQL.

## Requisitos

- Python 3.11 ou superior
- Node.js 18.x ou superior
- PostgreSQL 13 ou superior
- Docker (opcional, para containerização)
- AWS S3 (opcional, para armazenamento de mídia)

## Estrutura do Projeto

- `backend/`: Contém o código fonte do Django.
  - `supplier/`: Aplicativo Django para gerenciar fornecedores.
  - `core/`: Aplicativo Django para configuração e funcionalidades gerais.
- `frontend/`: Contém o código fonte do React.
- `docker/`: Arquivos de configuração do Docker e Docker Compose.
- `tests/`: Testes automatizados para o Django e o GraphQL.

## Configuração do Ambiente

### Backend

1. **Clone o Repositório**

   ```bash
   git clone [https://github.com/username/energy-supplier-management](https://github.com/MeninoNias/ms-energy).git
   cd ms=energy
   ```
2. **Instale Dependências do Python**
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. **Configure o .env**
   ```bash
     SECRET_KEY=
     DEBUG=
     ENVIRONMENT=local
     PROJECT_NAME=
     DB_NAME=
     DB_USER=
     DB_PASSWORD=
     DB_HOST=
     DB_PORT=
   ```
4. **Execute as Migrações**
   ```bash
    python manage.py migrate
   ```
5. **Inicie o Servidor de Desenvolvimento**
   ```bash
    python manage.py runserver
   ```
6. **Testes**
   ```bash
    python manage.py test
   ```

## GraphQL

O sistema usa GraphQL para consultas. O endpoint GraphQL está disponível em /graphql/.

#Exemplos de Consultas
   ```graphql
   query {
    suppliers(minKwhLimit: 10000) {
        publicId
        name
        cnpj
        logo
        originState
        costPerKwh
        minimumKwhLimit
        totalClients
        averageRating
    }
}
   ```
