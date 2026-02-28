from fastapi import FastAPI

different_app = FastAPI()

@different_app.get("/")
def read_root():
    return {"message": "Бонжур, ёпта"}