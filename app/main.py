from operator import mod
from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.sweets import router as sweets_router

app = FastAPI(title="Incubyte Sweet Shop API")

app.include_router(auth_router)
app.include_router(sweets_router)

@app.get("/status")
def health():
    return {"status": "running"}