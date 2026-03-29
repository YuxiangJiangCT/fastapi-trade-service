![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

# FastAPI Trade Service

A trade order management REST API with full CI/CD pipeline — from local Docker development to automated AWS EC2 deployment.

## Why This Project

This project demonstrates production-grade backend engineering practices: containerized API development, automated testing, continuous deployment, and cloud infrastructure — the full lifecycle from `git push` to running in production.

## Architecture

```
Developer → git push → GitHub Actions CI/CD
                           ├── 1. Build & Test (pytest)
                           ├── 2. Docker Build
                           └── 3. SSH Deploy → AWS EC2
                                                  └── Docker Compose
                                                       ├── FastAPI (uvicorn)
                                                       └── PostgreSQL
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/orders` | Create a new trade order |
| `GET` | `/orders` | List all orders |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |

### Example: Create Order

```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "AAPL",
    "price": 178.50,
    "quantity": 100,
    "order_type": "buy"
  }'
```

## Quick Start

### With Docker (recommended)

```bash
git clone https://github.com/YuxiangJiangCT/fastapi-trade-service.git
cd fastapi-trade-service
docker-compose up --build
# API available at http://localhost:8000/docs
```

### Without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) runs on every push/PR to main:

| Stage | What It Does |
|-------|-------------|
| **Build & Test** | Install deps → run `pytest` suite |
| **Docker Build** | Build container image, verify it starts |
| **Deploy** | SSH into EC2 → pull latest → `docker-compose up` |

### AWS EC2 Setup

Required GitHub Secrets:
- `EC2_SSH_KEY` — Private SSH key for EC2 instance
- `EC2_KNOWN_HOSTS` — SSH known hosts entry

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | FastAPI (Python) |
| Database | PostgreSQL (prod) / SQLite (dev) |
| Server | Uvicorn |
| Container | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 (Ubuntu) |
| Docs | Auto-generated Swagger UI + ReDoc |# FastAPI Trade Service

A simple trade order management system built with **FastAPI**, **PostgreSQL**, **Docker**, and **GitHub Actions** for CI/CD. It supports creating and retrieving orders via REST APIs and is deployed on **AWS EC2**.

## Features

- **REST API**:
  - `POST /orders`: Create a new order
  - `GET /orders`: Retrieve all orders
- **Database**: PostgreSQL (or SQLite for local testing)
- **Docker Containerization**: Single `Dockerfile` plus `docker-compose.yml` for multi-container setup
- **CI/CD**: GitHub Actions workflow to automatically test, build, and deploy to AWS EC2


       

## 1. Getting Started

### Local Development (Using Docker Compose)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YuxiangJiang2026/fastapi-trade-service.git
   cd fastapi-trade-service

2. **Build and run the containers**:
   ```bash
   docker-compose up --build


3. **Access the API Documentation**:
   Open your browser and visit http://127.0.0.1:8000/docs to view the Swagger UI.
   Use the POST /orders endpoint to create orders and GET /orders to retrieve them.

## 2. Local Development (Without Docker)
1. **Install dependencies**:
  	```bash
  	pip install -r requirements.txt

2. **Run the FastAPI application**:
	```bash
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

3. **Access the docs**:
   Visit http://127.0.0.1:8000/docs in your browser.


## 2. API Documentation

FastAPI automatically generates documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Example Endpoints

#### Create an Order
- **Endpoint**: `POST /orders`
- **Request Body**:
  ```json
  {
    "symbol": "AAPL",
    "price": 150.0,
    "quantity": 10,
    "order_type": "buy"
  }

- Response Example:
  ```json
  {
  "id": 1,
  "symbol": "AAPL",
  "price": 150.0,
  "quantity": 10,
  "order_type": "buy"
}

Get All Orders
- Endpoint: GET /orders
- Response Example:

  ```json
  [
  {
    "id": 1,
    "symbol": "AAPL",
    "price": 150.0,
    "quantity": 10,
    "order_type": "buy"
  }
  ]


## 3. CI/CD with GitHub Actions
### Workflow Overview
- **Location**: `.github/workflows/ci-cd.yml`
- **Triggers**:
  - Push or pull request to the `main` branch.
- **Jobs**:
  1. **build-and-test**: Installs dependencies and runs tests using `pytest`.
  2. **docker-build**: Builds the Docker image to ensure it compiles successfully.
  3. **deploy-to-ec2**: SSHs into the AWS EC2 instance, pulls the latest code, and runs `docker-compose up -d --build` to deploy the updated version.

### AWS EC2 Deployment
1. **Setup AWS EC2**:
   - Launch an EC2 instance (**Ubuntu**).
   - Install **Docker & Docker Compose**.
   - Clone this repository onto the instance.
   
2. **GitHub Secrets**:
   - `EC2_SSH_KEY`: The **private SSH key**.
   - `EC2_KNOWN_HOSTS`: The host key for the EC2 instance (**obtain via** `ssh-keyscan 3.22.81.199`).

3. **Deployment**:
   - On **every push to `main`**, GitHub Actions will **SSH into the EC2 instance**, pull changes, and restart the Docker containers.

