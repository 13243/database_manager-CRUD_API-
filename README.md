CRUD API with FastAPI: Digital Warehouse Manager

Summary: A RESTful API built with FastAPI and SQLAlchemy. Ready for production and deployed on Render.
Live Demo: https://crud-api-qta6.onrender.com
Swagger UI: https://crud-api-qta6.onrender.com/docs

Purpose:
Scalable backend service that allows external clients to create, retrieve, update, and delete data from a database.

API Endpoints:
      POST /items/ - Create a new item
      GET /items/ - Retrieve all items
      GET /items/{item_id} - Retrieve one item
      PUT /items/{item_id} - Update an existing item
      DELETE /items/{item_id} - Delete an existing item
      
Features:
      Full CRUD operations for Items (Create, Read, Update, Delete)
      Auto-generated interactive API docs at /docs
      SQLite for local development (PostgreSQL ready)
      Deployed on Render with CI/CD from GitHub
      Unit tests written with pytest in tests/
      Dockerized for easy containerized deployment

Tech Stack:
      FastAPI - Web framework
      SQLAlchemy - ORM
      SQLite - Database (development)
      Render - Deployment platform
      pytest - Testing
      Python 3.12
      Docker - Containerization

How to Set Up Locally:
      Option 1: Traditional (Without Docker)
            Run:
                  pip install -r requirements.txt
                  uvicorn app.main:app --reload
                  
                  Open http://localhost:8000/docs in your browser.

Option 2: Using Docker (Recommended)
      Prerequisites:
            Docker Desktop installed and running
            WSL2 enabled (Windows) or Docker Engine (Linux/macOS)
      Steps:
            1. Clone the repository:
            git clone https://github.com/13243/database_manager-CRUD_API.git
            cd database_manager-CRUD_API

            2. Build the Docker image:
            docker build -t fastapi-app .
            
            3. Run the container:
            docker run -d -p 8000:8000 --env-file .env --name my-fastapi fastapi-app
            
            Note: If you don't have a .env file, omit the --env-file .env flag.

4. Access the API:
Open http://localhost:8000/docs in your browser.
Useful Docker Commands:
      docker ps - See running containers
      docker logs my-fastapi - View application logs
      docker stop my-fastapi - Stop the container
      docker start my-fastapi - Start a stopped container
      docker rm my-fastapi - Remove the container

Docker Compose (Optional)
For easier management, you can use docker-compose.
      Create a docker-compose.yml file with the following content:
            version: '3.8'
            services:
              api:
                build: .
                container_name: fastapi-api
                ports:
                  - "8000:8000"
                environment:
                  - DATABASE_URL=sqlite:///./test.db
                volumes:
                  - .:/app
                  - ./test.db:/app/test.db
                command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
      Then run:
      docker-compose up -d

Testing
      Run the test suite with:
      pytest (in environemnt with pytest), or
      docker exec -it my-fastapi pytest (for docker execution of tests)

Deployment
      Render: The app is deployed at https://crud-api-qta6.onrender.com
      Docker: The app can be deployed to any container platform.
