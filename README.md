# Chat With Python

## Overview
This project is a chat application built with Flask, SQLAlchemy, and Flask-SocketIO. It uses Docker for containerization and PostgreSQL as the database.

## TL;DR
- Clone the repository
- Create a `.env` file in the root directory of your project and add the required environment variables
- Run `docker-compose up --build`
- Access the application at `http://localhost:5000`

## Prerequisites
- Docker
- Docker Compose

## Setup

### Environment Variables
Create a `.env` file in the root directory of your project and add the following environment variables:
* `SECRET_KEY` - A secret key for your application
* `DATABASE_URL` - The URL for your PostgreSQL database
* `POSTGRES_USER` - The username for your PostgreSQL database
* `POSTGRES_PASSWORD` - The password for your PostgreSQL database
* `POSTGRES_DB` - The name of your PostgreSQL database

### Build and Run the Application
1. First, ensure Docker is running on your machine.
2. **Build and start the containers**:
    ```sh
    docker-compose up --build
    ```

3. **Access the application**:
    Open your web browser and go to `http://localhost:5000`.
4. **Test the application**:
    Open a separate terminal window and run:
    ```sh
    docker-compose exec web python -m pytest
    ```
5. **Alembic usage**:
    - To create a new migration, run:
        ```sh
        docker-compose exec web alembic revision --autogenerate -m "migration message"
        ```
    - To apply the migration, run:
        ```sh
        docker-compose exec web alembic upgrade head
        ```
    - To downgrade the migration, run:
        ```sh
        docker-compose exec web alembic downgrade -1
        ```
6. **Stop the containers**:
    ```sh
    docker-compose down
    ```


## Project Structure

    ├── chat-with-python
        ├── alembic
        ├── app 
            │ ├── static
            │ │   ├── css
            │ │   └── script
            │ ├── templates
            │ │   ├── html (templates) files
            │ ├── __init__.py
            │ ├── views.py 
            │ ├── models.py
            │ └── ...
        ├── tests
            ├── conftest.py
            └── ...
        ├── .env
        ├── requirements.txt 
        ├── docker files
        ├── README.md
        └── ...

## About
This project is a chat with AI application built with Flask, SQLAlchemy, and Flask-SocketIO. It uses Docker for containerization and PostgreSQL as the database.

- User can send messages to the server and get responses from the server (AI).
- All the messages saved in the database for later use.
- The database also has a `conversation` table, which is used so the AI can respond based on previous conversations.
- For now, the client-server communication is via WebSockets.
- The test simply checks if the `/ask` endpoint return a 200 status code.

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Flask-SocketIO
- PostgreSQL
- Docker
- Docker Compose
