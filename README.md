# FastAPI Trade Service

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

