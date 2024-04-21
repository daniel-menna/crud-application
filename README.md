# Product Management CRUD for E-commerce

This project consists of a CRUD (Create, Read, Update, Delete) developed in Python for managing product registrations on an e-commerce platform. The application uses technologies like Streamlit, Pydantic, SQLAlchemy, and Pandas to offer an intuitive interface and robust functionalities.

## Features

-   **Creation:** Add new products to the database, providing information such as name, description, price, and category.
-   **Requisition:** Easily query registered products, filtering by name, category, or other criteria.
-   **Update:** Update information of existing products, ensuring the accuracy and relevance of data.
-   **Delete:** Delete products that are no longer needed, keeping the database organized.

## Technologies Used

-   **[Python:](https://www.python.org/)** Main programming language of the project (version 3.12.1).
-   **[Streamlit:](https://streamlit.io/)** Library for creating web interfaces in Python quickly and easily.
-   **[Pydantic:](https://github.com/pydantic/pydantic)** Used for data validation and serialization.
-   **[SQLAlchemy:](https://www.sqlalchemy.org/)** ORM framework for relational database manipulation.
-   **[Pandas:](https://pandas.pydata.org/)** Powerful tool for data analysis and manipulation in Python.

## Configuration and Usage

The project is containerized with [Docker](https://www.docker.com/), consisting of database, backend and frontend layers.

### Database
The database layer includes a configured instance of [PostgreSQL](https://www.postgresql.org/).

### Backend

The backend layer contains the Python application and its dependencies.

### Frontend

The frontend layer contains the Streamlit web interface.

### Docker Compose

To install and build all three layers of the application, you can use Docker Compose. Simply run `docker-compose up --build` to build and start the containers. 

## Contribution

Contributions are welcome! Feel free to open issues reporting problems or suggestions, and to send pull requests with improvements.