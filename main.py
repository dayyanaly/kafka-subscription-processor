from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Dict, Generator
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
import json
import asyncio

load_dotenv()  # Load environment variables from .env file

# Load credentials for Database 1 from environment variables
DB1_HOST = os.getenv("DB1_HOST")
DB1_PORT = int(os.getenv("DB1_PORT"))
DB1_USER = os.getenv("DB1_USER")
DB1_PASSWORD = os.getenv("DB1_PASSWORD")
DB1_DATABASE = os.getenv("DB1_DATABASE")

# Load credentials for Database 2 from environment variables
DB2_HOST = os.getenv("DB2_HOST")
DB2_PORT = int(os.getenv("DB2_PORT"))
DB2_USER = os.getenv("DB2_USER")
DB2_PASSWORD = os.getenv("DB2_PASSWORD")
DB2_DATABASE = os.getenv("DB2_DATABASE")

# Kafka server and topic details
KAFKA_SERVER = os.getenv("KAFKA_SERVER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Connect to Database 1 and Database 2 securely
engine1 = create_engine(f"postgresql://{DB1_USER}:{DB1_PASSWORD}@{DB1_HOST}:{DB1_PORT}/{DB1_DATABASE}", pool_size=5, max_overflow=10)
engine2 = create_engine(f"postgresql://{DB2_USER}:{DB2_PASSWORD}@{DB2_HOST}:{DB2_PORT}/{DB2_DATABASE}", pool_size=5, max_overflow=10)

# Define SessionLocal factories for both databases
SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine1)
SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)

Base = declarative_base()

# Define SubscriptionStatus model
class SubscriptionStatus(Base):
    __tablename__ = "subscription_status"

    email = Column(String, primary_key=True)
    status = Column(String, nullable=False)

# Create tables in both databases
Base.metadata.create_all(bind=engine1)
Base.metadata.create_all(bind=engine2)

# Dependency to get a session for Database 1
def get_db1_session() -> Generator[Session, None, None]:
    try:
        db = SessionLocal1()
        yield db
    finally:
        db.close()

# Dependency to get a session for Database 2
def get_db2_session() -> Generator[Session, None, None]:
    try:
        db = SessionLocal2()
        yield db
    finally:
        db.close()

# Initialize FastAPI app
app = FastAPI()

# Kafka Consumer setup
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="fastapi-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# Function to consume Kafka messages and update database
async def consume_and_update_db():
    for message in consumer:
        data = message.value
        email = data.get("email")
        status = data.get("status")

        if email and status:
            with SessionLocal2() as session:
                subscription_status = session.query(SubscriptionStatus).filter_by(email=email).first()
                if subscription_status:
                    subscription_status.status = status
                else:
                    subscription_status = SubscriptionStatus(email=email, status=status)
                    session.add(subscription_status)
                session.commit()

# Background task to consume Kafka messages
async def startup_event():
    asyncio.create_task(consume_and_update_db())

app.add_event_handler("startup", startup_event)

# FastAPI endpoints
@app.post("/subscription_status", response_model=Dict[str, str])
def create_subscription_status(email: str, status: str, db: Session = Depends(get_db1_session)):
    try:
        subscription_status = SubscriptionStatus(email=email, status=status)
        db.add(subscription_status)
        db.commit()
        return {"message": "Subscription status created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create subscription status: {e}")

@app.get("/subscription_status/{email}", response_model=Dict[str, str])
def read_subscription_status(email: str, db: Session = Depends(get_db1_session)):
    try:
        subscription_status = db.query(SubscriptionStatus).filter_by(email=email).first()
        if subscription_status:
            return {"email": email, "status": subscription_status.status}
        else:
            raise HTTPException(status_code=404, detail="Subscription status not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read subscription status: {e}")

@app.put("/subscription_status/{email}", response_model=Dict[str, str])
def update_subscription_status(email: str, status: str, db: Session = Depends(get_db1_session)):
    try:
        subscription_status = db.query(SubscriptionStatus).filter_by(email=email).first()
        if subscription_status:
            subscription_status.status = status
            db.commit()
            return {"message": "Subscription status updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Subscription status not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update subscription status: {e}")

@app.delete("/subscription_status/{email}", response_model=Dict[str, str])
def delete_subscription_status(email: str, db: Session = Depends(get_db1_session)):
    try:
        subscription_status = db.query(SubscriptionStatus).filter_by(email=email).first()
        if subscription_status:
            db.delete(subscription_status)
            db.commit()
            return {"message": "Subscription status deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Subscription status not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete subscription status: {e}")
