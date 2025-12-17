from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/data", StaticFiles(directory="/data"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bye")
async def root():
    return {"message": "bye"}
