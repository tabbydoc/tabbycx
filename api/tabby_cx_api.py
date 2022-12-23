import uvicorn
from fastapi import UploadFile, FastAPI

from html_parse.html_parser import parse
from init_api import app, PORT


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


def run_api() -> None:
    uvicorn.run(host='0.0.0.0', port=PORT)

