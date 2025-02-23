from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal, engine, Base
from .models import Order
from .schemas import OrderCreate, OrderOut

app = FastAPI(
    title="Trade Service",
    description="A simple REST API for trade orders",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.post("/orders", response_model=OrderOut)
def create_order(order: OrderCreate):
    db: Session = SessionLocal()
    db_order = Order(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()
    return db_order

@app.get("/orders", response_model=List[OrderOut])
def get_orders():
    db: Session = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders