from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.sweets import router as sweets_router

app = FastAPI(title="Sweet Shop API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(sweets_router, prefix="/api/sweets", tags=["sweets"])

@app.get("/status")
def status():
    return {"status": "ok"}
