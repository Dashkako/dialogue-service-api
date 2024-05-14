import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate_mock")
async def root():
    time.sleep(15)
    return {'message': "I generate some phrase"}
