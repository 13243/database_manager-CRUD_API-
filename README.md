CRUD API with FastAPI: Digital Warehouse Manager

Summary: A RESTful API built with FastAPI and SQLAlchemy. Ready for production and deployed on Render.
Live Demo: https://crud-api-qta6.onrender.com
Swagger UI: https://crud-api-qta6.onrender.com/docs

Purpose:
Scalable backend service that allows external clients to create, retrieve, update, and delete data from a database.

API Endpoints:
- POST /items/ - Create a new item
- GET /items/ - Retrieve all items
- GET /items/{item_id} - Retrieve one item
- PUT /items/{item_id} - Update an existing item
- DELETE /items/{item_id} - Delete an existing item

Features:
- Full CRUD operations for Items (Create, Read, Update, Delete)
- Auto-generated interactive API docs at /docs
- PostgreSQL database with persistent storage (production-ready)
- Deployed on Render with CI/CD from GitHub
- Unit tests written with pytest in tests/
- Dockerized for easy containerized deployment
- Docker Compose for one-command local development

Tech Stack:
- FastAPI - Web framework
- SQLAlchemy - ORM
- PostgreSQL - Database (production-ready)
- Render - Deployment platform
- pytest - Testing
- Python 3.12
- Docker & Docker Compose - Containerization

How to Set Up Locally:

Option 1: Traditional (Without Docker)
pip install -r requirements.txt
uvicorn app.main:app --reload

Open http://localhost:8000/docs in your browser.

Option 2: Using Docker Compose (Recommended)
docker-compose up -d

Open http://localhost:8000/docs in your browser.

The Docker Compose setup automatically starts both the FastAPI app and a PostgreSQL database container, with persistent data storage.

Testing
pytest

Or inside the Docker container:
docker-compose exec app pytest

Deployment
- Render: The app is deployed at https://crud-api-qta6.onrender.com
- Docker: The app can be deployed to any container platform using the provided Dockerfile and docker-compose.yml.