from fastapi import FastAPI


app = FastAPI(title="Sweet Shop API")



@app.get("/health")
def health():
    return {"status": "ok"}



