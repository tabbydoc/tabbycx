import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


PORT = 3000

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run_api() -> None:
    uvicorn.run("init_api:app", host='0.0.0.0', port=PORT)
