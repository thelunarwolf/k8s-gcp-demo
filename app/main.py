import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": {
            "SECRET_ONE": os.environ.get('SECRET_ONE', "SECRET_1"),
            "SECRET_TWO": os.environ.get('SECRET_TWO', "SECRET_2"),
            "CONFIG_ONE": os.environ.get('CONFIG_ONE', "CONFIG_1"),
            "CONFIG_TWO": os.environ.get('CONFIG_TWO', "CONFIG_2"),
        }
    }

