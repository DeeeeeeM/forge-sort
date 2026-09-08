from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="ForgeSort API")

class HealthCheck(BaseModel):
    status: str
        
@app.get("/health")
def health_check():
    return{"status": "healthy"} 

