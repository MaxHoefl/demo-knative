import uvicorn
from fastapi import FastAPI, Depends
from loguru import logger

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)
