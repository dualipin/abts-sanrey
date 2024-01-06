from fastapi import FastAPI
import models.producto as prod

app = FastAPI()

@app.get("/")
def index():
    return {'message': 'Hello, World!'}