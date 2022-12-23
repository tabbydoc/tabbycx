import uvicorn
from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware

from manager import TabbyCxManager

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


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
        manager = TabbyCxManager()
        tables = manager.parse_html(file)
        return {"filename": file.filename, "tables": tables}


def run_api() -> None:
    uvicorn.run("tabby_cx_api:app", host='0.0.0.0', port=PORT)
