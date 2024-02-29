# SQLAlchemy ORM Helper for FastAPI

## Overview

This is a simple FastAPI application integrated with SQLAlchemy ORM, designed to provide a foundation for building web applications with database functionality. The purpose of this project is to offer a basic structure and helper functions for handling SQLAlchemy operations within a FastAPI project.

## Features

- **FastAPI Integration**: Utilizes the FastAPI framework for building web APIs.
- **SQLAlchemy ORM**: Leverages SQLAlchemy for database operations and ORM functionality.
- **Simple Structure**: Provides a straightforward project structure for easy understanding and customization.

## Requirements
All dependencies located in `req.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/sqlalchemy_orm_helper_FastAPI.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd sqlalchemy_orm_helper_FastAPI
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Configure the database connection:**

    Open the `database/db_config.py` file and update the `db_url` as per your database configuration.

    ```python
    class DatabaseConfig(BaseSettings):
        db_url: str = "sqlite:///./your_db_name.db"
    ```

## Usage

1. **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

    The API will be accessible at `http://127.0.0.1:8000`.

2. **Explore the API:**

    Open the Swagger documentation at `http://127.0.0.1:8000/docs` to explore and test the API.

## Contributing

Feel free to contribute by submitting bug reports, feature requests, or pull requests. Contributions are welcome!

