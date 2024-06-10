# CRUD para gestão de produtos em uma plataforma de E-commerce

Este projeto consiste em criar um CRUD (Create, Read, Update, Delete) desenvolvido em Python para gerenciar registros de produtos em uma plataforma de e-commerce. A aplicação utiliza tecnologias como Streamlit, Pydantic, SQLAlchemy e Pandas para oferecer uma interface intuitiva e funcionalidades robustas.

## Funcionalidades

-   **Creation:** Adicione novos produtos ao banco de dados, fornecendo informações como nome, descrição, preço e categoria.
-   **Requisition:** Consulte facilmente os produtos cadastrados, filtrando por nome, categoria ou outros critérios.
-   **Update:** Atualize as informações dos produtos existentes, garantindo a precisão e a relevância dos dados.
-   **Delete:** Exclua produtos que não são mais necessários, mantendo o banco de dados organizado.

## Technologies Used

-   **[Python:](https://www.python.org/)** Principal linguagem deste projeto (version 3.12.1).
-   **[Streamlit:](https://streamlit.io/)** Biblioteca python para a criação de aplicações web de forma fácil e rapida.
-   **[Pydantic:](https://github.com/pydantic/pydantic)** Usada para validação e serialização dos dados.
-   **[SQLAlchemy:](https://www.sqlalchemy.org/)** framework ORM para manipulação de dados relacionais.
-   **[Pandas:](https://pandas.pydata.org/)** Poderosa ferramenta para manipulação e análise de dados em Python.

## Configuração e Uso

Este projeto é construido utilizando containers [Docker](https://www.docker.com/), consistindo na base de dados e as camas de backend e frontend.

### Base de Dados
A camada da base de dados consiste em uma instância configura de [PostgreSQL](https://www.postgresql.org/).

### Backend

A camada de backend contem a aplicação Python e as suas dependências.

### Frontend

O frontend contém em sua camada uma interface web com Streamlit.

### Docker Compose

Para installar e executar o build destre projeto, você pode utilizar o Docker Compose. Rode `docker-compose up --build` para criar a instância e executar a aplicação. 

## Contribuições

Contribuições são bem-vindas! Fique a vontade para reportar problemas ou sugestões, envie pull requests com as melhorias.
