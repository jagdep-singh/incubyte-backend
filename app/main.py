from operator import mod
from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.sweets import router as sweets_router

app = FastAPI(title="Sweet Shop API")

app.include_router(auth_router)
app.include_router(sweets_router)

@app.get("/health")
def health():
    return {"status": "ok"}