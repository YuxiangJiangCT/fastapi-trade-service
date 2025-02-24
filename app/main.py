from fastapi import FastAPI, HTTPException, WebSocket
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal, engine, Base
from .models import Order
from .schemas import OrderCreate, OrderOut

app = FastAPI(
    title="Trade Service",
    description="A simple REST API for trade orders + WebSocket",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.post("/orders", response_model=OrderOut)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    await manager.broadcast(f"New order created: {db_order.symbol}")
    return db_order

@app.get("/orders", response_model=List[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message from client: {data}")
    except:
        manager.disconnect(websocket)
