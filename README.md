CRUD API with FastAPI: Digital Warehouse Manager

Summary:
A RESTful API built with FastAPI and SQLAlchemy. 
Ready for production and deployed on Render.
Link: https://crud-api-qta6.onrender.com - root
      https://crud-api-qta6.onrender.com/docs - swaggerUI for backend interactions

Purpose:
Scalable backend service that allows external clients to create, retrieve, update, and delete data from a database.

API Endpoints:
Methods:
- POST /items/ (creates a new item)
- GET /items/ (retrieves all items)
- GET /items/{item_id} (retrieves one item)
- PUT /items/{item_id} (updates an existing item)
- DELETE /items/{item_id} (deletes an existing item)

Feautures:
- CRUD operations for Items (Create, Read, Update, Delete)  
- Auto‑generated, interactive API docs in /docs.
- Uses SQLite for local development (later I may expand the project by connecting to postgresql).  
- Deployed on Render with CI/CD from GitHub
- Unit tests written with pytest in tests folder

Tech that was used in the developmemt process:
- FastAPI
- SQLAlchemy
- SQLite
- Render
- pytest
- python

How to set up locally:
- pip install -r requirements.txt
- uvicorn app.main:app --reload
- open http://localhost:8000/docs