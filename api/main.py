from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from html_parse.html_parser import parse

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "No upload file sent"}
    else:
        tables = parse(file)
        return {"filename": file.filename}
