from fastapi.encoders import jsonable_encoder
from bson import ObjectId  # ✅ Add this
from fastapi import APIRouter, UploadFile, File
from app.services.parser import parse_resume
from app.utils.helpers import collection

router = APIRouter()

@router.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    parsed_data = parse_resume(file.file)  # extract data from uploaded file

    result = collection.insert_one(parsed_data)  # save to MongoDB
    parsed_data["_id"] = str(result.inserted_id)  # convert ObjectId to string

    return {"parsed": parsed_data}  # JSON-safe now
