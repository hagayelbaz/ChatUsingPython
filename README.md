# Chat With Python

## Overview
This project is a chat application built with Flask, SQLAlchemy, and Flask-SocketIO. It uses Docker for containerization and PostgreSQL as the database.

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

4. **Stop the containers**:
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
            ├── __init__.py
            ├── test_views.py
            └── ...
        ├── .env
        ├── requirements.txt 
        ├── docker files
        ├── README.md
        └── ...

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Flask-SocketIO
- PostgreSQL
- Docker
- Docker Compose


- TODO: test, alembic