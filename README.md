# FastAPI Trade Service

A simple trade order management system built with **FastAPI**, **PostgreSQL**, **Docker**, and **GitHub Actions** for CI/CD. It supports creating and retrieving orders via REST APIs and is deployed on **AWS EC2**.

## Features

- **REST API**:
  - `POST /orders`: Create a new order
  - `GET /orders`: Retrieve all orders
- **Database**: PostgreSQL (or SQLite for local testing)
- **Docker Containerization**: Single `Dockerfile` plus `docker-compose.yml` for multi-container setup
- **CI/CD**: GitHub Actions workflow to automatically test, build, and deploy to AWS EC2
- **(Optional) WebSocket**: Ready for future implementation

---

## Repository Structure
fastapi-trade-service/
│   README.md                 # This documentation file
│   requirements.txt          # Python dependencies
│   docker-compose.yml        # Docker Compose configuration
│   Dockerfile                # Docker build file
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # GitHub Actions CI/CD workflow
│
├── app/
    ├── main.py               # FastAPI entry point (routes, logic)
    ├── database.py           # Database connection setup
    ├── models.py             # SQLAlchemy models
    ├── schemas.py            # Pydantic schemas for request/response validation
    └── init.py           # Empty file, marks app as a Python package
       

---

## 1. Getting Started

### Local Development (Using Docker Compose)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YuxiangJiang2026/fastapi-trade-service.git
   cd fastapi-trade-service

2.	**Build and run the containers:
   ```bash
   docker-compose up --build


3.	**Access the API Documentation:
	•	Open your browser and visit http://127.0.0.1:8000/docs to view the Swagger UI.
	•	Use the POST /orders endpoint to create orders and GET /orders to retrieve them.

## 2. Local Development (Without Docker)
	1.	Install dependencies:
  ```bash
  pip install -r requirements.txt
