from fastapi import FastAPI, File, UploadFile,Form
from pydantic import BaseModel
from helper import Files
app = FastAPI()

def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

@app.post("/uploadfile/", status_code=201)
async def create_upload_file(file1: UploadFile = File(...), file2: UploadFile= File(...)):

    contents1 = await file1.read()
    contents2 = await file2.read()
    save_file(file1.filename, contents1)
    save_file(file2.filename, contents2)
    res = Files(file1, file2)
    if res:
        return {"Result": res}
    else:
        return {"Error": "Some Error"}
