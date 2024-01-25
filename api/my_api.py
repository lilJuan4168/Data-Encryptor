from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from api.functions import *
import os

app = FastAPI()

@app.get("/ip")
async def get_ip():
            x = ip()
            return x

@app.get("/gen_key")
async def gen_key(my_pwd):
    my_key = create_key(my_pwd)
    return StreamingResponse(my_key, media_type='application/octet-stream', headers={'Content-Disposition': 'attachment; filename="password.pickle"'})

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
async def sharing_upload_file(key, file: UploadFile):
    try:
        data = data_encrypt(key, file)
        return FileResponse(media_type="multipart/form-data", filename=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error, file not saved: {str(e)}")