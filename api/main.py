from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

from src.app.routes import model_training

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

api.include_router(model_training.router, prefix="/model-training", tags=["model-training"])

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
