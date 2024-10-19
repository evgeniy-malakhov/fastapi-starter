from fastapi import FastAPI

from src.api.v1.endpoints import user

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/health")
async def root():
    return {"status": "online"}