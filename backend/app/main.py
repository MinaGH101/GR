from fastapi import FastAPI
from app.api.system import router as system_router

app = FastAPI(title="GeoRAG")
app.include_router(system_router)

@app.get("/")
def root():
    return {"message": "GeoRAG API is running"}


