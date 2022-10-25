from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from html_parse.html_parser import parse

from fastapi.middleware.cors import CORSMiddleware

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
        tables = parse(file)
        json_tables = []
        for table in tables:
            json_tables.append(table.to_dict())
        return {"filename": file.filename, "tables": json_tables}
