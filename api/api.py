from fastapi import FastAPI, File, UploadFile, HTTPException
from api.functions import *
import os

app = FastAPI()

@app.get("/ip")
async def get_ip():
            x = ip()
            return x

@app.post("/sharing/upload")
async def sharing_upload_file(file: UploadFile):
    try:
        os.makedirs("files", exist_ok=True)
        file_path = os.path.join("files", file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        return {"status": 200,"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error, file not saved: {str(e)}")


@app.post("/encrypt/upload")
async def sharing_upload_file(file: UploadFile):
    try:
        os.makedirs("files", exist_ok=True)
        file_path = os.path.join("files", file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        return {"status": 200,"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error, file not saved: {str(e)}")